"""Palette musicale élargie pour les Reels (lot 4 et suivants) : un style très différent par Reel.
Styles : lofi (music.py), ambient (music3.py), piano, pluck (cordes pincées), pulse (pulsation électronique douce).
Usage : python3 music4.py (lit posts.json, champ music = dict(style=..., ...))."""
import numpy as np, wave, json, os
from scipy.signal import lfilter
import music, music3
from music import hz, SR, add, PROGS, QUAL, PENTA_MAJ, PENTA_MIN

def lp(x, fc, n=1):
    a = np.exp(-2 * np.pi * fc / SR)
    for _ in range(n): x = lfilter([1 - a], [1, -a], x)
    return x

def finish(mix, rng, out, seconds, room=0.3):
    N = len(mix)
    ir_n = int(SR * 2.2); ir = rng.normal(0, 1, ir_n) * np.exp(-np.arange(ir_n) / SR * 2.4); ir = lp(ir, 3000)
    ir /= np.abs(ir).sum() ** 0.5 * 12
    from scipy.signal import fftconvolve
    mix = mix + room * fftconvolve(mix, ir)[:N]
    mix = lp(mix, 6500)
    mix = mix / (np.max(np.abs(mix)) + 1e-9) * 0.8
    with wave.open(out, 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix * 32767).astype('<i2').tobytes())

def chord_notes(p, b):
    prog = PROGS[p['prog']]; off, q = prog[b % 4]; base = p['root'] + off
    return base, [base + iv for iv in QUAL[q]]

def piano_note(f, dur, vel):
    n = int(SR * dur); t = np.arange(n) / SR
    env = np.minimum(1, t / 0.004) * np.exp(-t * 1.7)
    s = np.sin(2 * np.pi * f * t) + .5 * np.sin(4 * np.pi * f * t) * np.exp(-t * 2) + .25 * np.sin(6 * np.pi * f * t) * np.exp(-t * 3.5) + .1 * np.sin(8 * np.pi * f * t) * np.exp(-t * 6)
    return vel * env * s

def pluck_note(f, dur, vel):
    n = int(SR * dur); t = np.arange(n) / SR
    s = sum((1 / k) * np.sin(2 * np.pi * f * k * t) * np.exp(-t * (3 + 2.5 * k)) for k in range(1, 9))
    return vel * np.minimum(1, t / 0.002) * s

def arp_track(p, seconds, rng, note, step, vel, octs, pad_amt):
    N = int(SR * seconds); beat = 60 / p['bpm']; bar = 4 * beat
    mix = np.zeros(N); pad = np.zeros(N)
    for b in range(int(seconds / bar) + 1):
        base, notes = chord_notes(p, b); t0 = b * bar
        order = list(p.get('pattern', [0, 1, 2, 3, 2, 1]))
        k = 0; t = t0
        while t < t0 + bar - 1e-6:
            if rng.random() < p.get('density', 0.9):
                idx = order[k % len(order)]; m = notes[idx % len(notes)] + 12 * octs[(k // len(order) + idx) % len(octs)]
                add(mix, int((t + rng.normal(0, 0.004)) * SR), note(hz(m), 2.4, vel * (0.8 + 0.4 * rng.random())))
            k += 1; t += step * beat
        if pad_amt:
            n = int(bar * SR) + SR; tt = np.arange(n) / SR
            env = np.clip(tt / 1.2, 0, 1) * np.clip((bar + 1 - tt) / 1.2, 0, 1)
            add(pad, int(t0 * SR), pad_amt * env * sum(np.sin(2 * np.pi * hz(m - 12) * tt) for m in notes[:3]))
    return mix, lp(pad, 900)

def render(p, seconds=34, out='track.wav'):
    st = p.get('style', 'lofi'); rng = np.random.default_rng(p['seed'])
    if st == 'lofi': return music.render(p, seconds, out)
    if st == 'ambient': return music3.render(p, seconds, out)
    N = int(SR * seconds); beat = 60 / p['bpm']
    if st in ('piano', 'pluck'):
        note = piano_note if st == 'piano' else pluck_note
        mix, pad = arp_track(p, seconds, rng, note, p.get('step', 0.5), 0.12 if st == 'piano' else 0.1, p.get('octs', [0, 1]), p.get('pad', 0.004))
        base_mix = mix + pad
        if p.get('shaker'):
            for t in np.arange(0, seconds, beat / 2):
                n = int(SR * .04); tt = np.arange(n) / SR; nz = rng.normal(0, 1, n); nz -= lp(nz, 5000)
                add(base_mix, int(t * SR), 0.012 * nz * np.exp(-tt * 80))
        return finish(base_mix, rng, out, seconds, p.get('room', 0.35))
    if st == 'pulse':
        mix = np.zeros(N); bass = np.zeros(N); perc = np.zeros(N); bar = 4 * beat
        for b in range(int(seconds / bar) + 1):
            base, notes = chord_notes(p, b); t0 = b * bar
            for s in range(8):
                t = t0 + s * beat / 2
                if rng.random() < 0.85:
                    m = notes[(s * 3) % len(notes)] + 12; n = int(SR * 0.35); tt = np.arange(n) / SR
                    sq = np.sign(np.sin(2 * np.pi * hz(m) * tt)) * 0.5 + np.sin(2 * np.pi * hz(m) * tt)
                    add(mix, int(t * SR), 0.05 * sq * np.exp(-tt * 9) * np.minimum(1, tt / 0.004))
            for s in range(4):
                t = t0 + s * beat; n = int(SR * beat); tt = np.arange(n) / SR
                bn = base - 24 if base - 24 >= 28 else base - 12
                add(bass, int(t * SR), 0.2 * np.sin(2 * np.pi * hz(bn) * tt) * np.exp(-tt * 4) * np.minimum(1, tt / 0.01))
                n = int(SR * .25); tt = np.arange(n) / SR; f = 50 + 80 * np.exp(-tt * 30)
                add(perc, int(t * SR), 0.28 * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 10))
                n = int(SR * .03); tt = np.arange(n) / SR; nz = rng.normal(0, 1, n); nz -= lp(nz, 6000)
                add(perc, int((t + beat / 2) * SR), 0.05 * nz * np.exp(-tt * 90))
        mix = lp(mix, p.get('cut', 1800), 2)
        return finish(mix + bass + perc, rng, out, seconds, p.get('room', 0.3))
    raise SystemExit('style inconnu ' + st)

if __name__ == '__main__':
    posts = json.load(open('posts.json')); os.makedirs('audio', exist_ok=True)
    for q in posts:
        render(q['music'], out=f"audio/m{q['n']:02d}.wav"); print(q['n'], q['music'].get('style', 'lofi'), q['music'].get('bpm'), q['music']['root'])
