"""Morceaux « deep house mélodique » originaux, sans paroles (numpy/scipy) : pads, sub, kick doux, arpège, sidechain.
Référence de style : tempo ~120, basses riches, montée progressive. Usage : python3 music2.py (lit posts.json)."""
import numpy as np, wave, json, os
from scipy.signal import lfilter
from music import PROGS, QUAL, hz, SR

def lp(x, fc, n=1):
    a = np.exp(-2 * np.pi * fc / SR)
    for _ in range(n): x = lfilter([1 - a], [1, -a], x)
    return x

def hp(x, fc): return x - lp(x, fc)

def add(buf, i, sig):
    if i < 0: sig = sig[-i:]; i = 0
    j = min(len(buf), i + len(sig))
    if i < len(buf) and j > i: buf[i:j] += sig[:j - i]

def render(params, seconds=34, out='track.wav'):
    rng = np.random.default_rng(params['seed'])
    bpm = params['bpm']; beat = 60 / bpm; bar = 4 * beat
    root = params['root']; prog = PROGS[params['prog']]; minor = params['prog'].startswith('min')
    N = int(SR * seconds); T = np.arange(N) / SR
    pad = np.zeros(N); sub = np.zeros(N); kick = np.zeros(N); hats = np.zeros(N); clap = np.zeros(N); arp = np.zeros(N); duck = np.ones(N)
    nbars = int(seconds / bar) + 1
    sixt = beat / 4
    for b in range(nbars):
        off, qual = prog[b % 4]; base = root + off
        notes = [base + iv for iv in QUAL[qual]] + [base + 14]
        t0 = b * bar; i0 = int(t0 * SR); n = min(int(bar * SR * 1.02), N - i0)
        if n <= 0: break
        tt = np.arange(n) / SR
        env = np.minimum(1, tt / 0.5) * np.minimum(1, (bar * 1.02 - tt) / 0.5)
        for m in notes:
            for det in (-0.09, 0.0, 0.1):
                f = hz(m - 12) * 2 ** (det / 12); ph = rng.random() * 6.28
                w_ = np.sin(2 * np.pi * f * tt + ph) + 0.5 * np.sin(4 * np.pi * f * tt + ph) + 0.25 * np.sin(6 * np.pi * f * tt + ph)
                pad[i0:i0 + n] += 0.035 * env * w_
        if b >= 1:
            bn = base - 24 if base - 24 >= 28 else base - 12
            for step in range(8):
                if step % 2 == 1 or step == 0:
                    ts = t0 + step * beat / 2; ln = int(SR * beat * 0.42); t = np.arange(ln) / SR
                    e = np.minimum(1, t / 0.008) * np.exp(-t * 3.5)
                    add(sub, int(ts * SR), 0.32 * e * (np.sin(2 * np.pi * hz(bn) * t) + 0.18 * np.sin(4 * np.pi * hz(bn) * t)))
        for bi in range(4):
            ts = t0 + bi * beat; i = int(ts * SR)
            if b >= 2 and i < N:
                ln = int(SR * 0.3); t = np.arange(ln) / SR
                f = 48 + 100 * np.exp(-t * 32)
                add(kick, i, 0.55 * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 8))
                d = min(int(SR * 0.28), N - i)
                duck[i:i + d] = np.minimum(duck[i:i + d], 0.35 + 0.65 * (np.arange(d) / int(SR * 0.28)) ** 0.8)
                if bi in (1, 3):
                    ln = int(SR * 0.18); t = np.arange(ln) / SR
                    add(clap, i, 0.10 * hp(rng.normal(0, 1, ln), 1200) * np.exp(-t * 22))
            if b >= 1:
                for s4 in range(4):
                    i2 = int((ts + s4 * sixt + (0.012 if s4 % 2 else 0)) * SR); op = s4 == 2
                    ln = int(SR * (0.16 if op else 0.04)); t = np.arange(ln) / SR
                    v = (0.05 if op else 0.025) * (0.7 + 0.6 * rng.random())
                    add(hats, i2, v * hp(rng.normal(0, 1, ln), 7000) * np.exp(-t * (28 if op else 90)))
        if b >= 2:
            tones = [x + 12 for x in notes] + [x + 24 for x in notes[:3]]
            seq = rng.choice(len(tones), 16)
            for s in range(16):
                if rng.random() < 0.72:
                    ts = t0 + s * sixt; ln = int(SR * 0.33); t = np.arange(ln) / SR; f = hz(tones[int(seq[s])])
                    pl = (np.sin(2 * np.pi * f * t) + 0.4 * np.sin(4 * np.pi * f * t) * np.exp(-t * 14) + 0.2 * np.sin(6 * np.pi * f * t) * np.exp(-t * 20)) * np.exp(-t * 9) * np.minimum(1, t / 0.003)
                    add(arp, int(ts * SR), (0.09 if s % 4 == 0 else 0.06) * pl)
    pad = (lp(pad, 900, 2) * 0.6 + lp(pad, 2600) * 0.4) * (0.55 + 0.45 * np.clip(T / 6, 0, 1))
    mel = (pad + arp) * duck
    d = int(beat * 0.75 * SR); e1 = np.zeros(N); e1[d:] = 0.33 * arp[:-d]; e2 = np.zeros(N); e2[2 * d:] = 0.15 * arp[:-2 * d]
    mix = mel + sub * duck + kick + clap + hats + e1 * duck + e2
    rev = np.zeros(N)
    for dl, g in ((0.037, .25), (0.061, .2), (0.097, .15)):
        k = int(dl * SR); rev[k:] += g * lp(mel[:-k], 3000)
    mix = lp(mix + 0.6 * rev, 9000) + lp(rng.normal(0, 0.002, N), 5000)
    mix = np.tanh(mix * 1.3) / 1.3
    mix = mix / (np.max(np.abs(mix)) + 1e-9) * 0.85
    with wave.open(out, 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix * 32767).astype('<i2').tobytes())

if __name__ == '__main__':
    posts = json.load(open('posts.json')); os.makedirs('audio', exist_ok=True)
    for p in posts:
        render(p['music'], out=f"audio/m{p['n']:02d}.wav"); print(p['n'], p['music'])
