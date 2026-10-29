"""Fonds sonores ambiants originaux (nappes chaudes, respiration lente, quelques notes éparses), sans paroles.
Style de référence : « fond seul moderne » de Tanguy (très doux, sombre, sans batterie). Usage : python3 music3.py (lit posts.json)."""
import numpy as np, wave, json, os
from scipy.signal import lfilter, fftconvolve
from music import hz, SR

CH = {'sus2': [0, 2, 7, 14], 'add9': [0, 4, 7, 14], 'm9': [0, 3, 7, 10, 14], 'maj7': [0, 4, 7, 11], 'm7': [0, 3, 7, 10],
      'sus4': [0, 5, 7, 10], 'lyd': [0, 4, 7, 11, 18], 'm6': [0, 3, 7, 9], 'maj': [0, 4, 7, 12]}
PROG = {  # 4 accords de ~8 s : (décalage, type)
    'a': [(0, 'm9'), (-7, 'sus2'), (-4, 'maj7'), (-2, 'add9')],
    'b': [(0, 'add9'), (-3, 'm7'), (-5, 'sus2'), (-7, 'lyd')],
    'c': [(0, 'm7'), (-2, 'maj7'), (3, 'add9'), (-4, 'sus4')],
    'd': [(0, 'sus2'), (5, 'maj7'), (-4, 'm9'), (-2, 'sus4')],
    'e': [(0, 'lyd'), (-5, 'add9'), (-7, 'm7'), (-3, 'sus2')],
}
PENTA = [0, 2, 4, 7, 9, 12, 14, 16, 19]
PENTA_M = [0, 3, 5, 7, 10, 12, 15, 17, 19]

def lp(x, fc, n=1):
    a = np.exp(-2 * np.pi * fc / SR)
    for _ in range(n): x = lfilter([1 - a], [1, -a], x)
    return x

def add(buf, i, sig):
    j = min(len(buf), i + len(sig))
    if 0 <= i < len(buf): buf[i:j] += sig[:j - i]

def voice(f, tt, timbre, rng):
    ph = rng.random() * 6.28
    if timbre == 'warm': h = [(k, 1 / k) for k in range(1, 7)]
    elif timbre == 'glass': h = [(1, 1), (2, .3), (3, .12), (5, .05)]
    elif timbre == 'organ': h = [(1, 1), (2, .5), (3, .35), (4, .15), (6, .1)]
    else: h = [(k, 1 / k ** 1.3) for k in range(1, 9)]  # 'string'
    return sum(a * np.sin(2 * np.pi * f * k * tt + ph * k) for k, a in h)

def render(p, seconds=34, out='track.wav'):
    rng = np.random.default_rng(p['seed']); N = int(SR * seconds); T = np.arange(N) / SR
    root = p['root']; prog = PROG[p.get('prog', 'a')]; minor = p.get('minor', True); timbre = p.get('timbre', 'warm')
    seg = seconds / 4; pad = np.zeros(N)
    cut = p.get('cut', 800)
    for c in range(4):
        off, q = prog[c]; base = root + off
        t0 = c * seg - 1.5; i0 = max(0, int(t0 * SR)); n = min(N - i0, int((seg + 3) * SR))
        if n <= 0: continue
        tt = np.arange(n) / SR
        ev = np.clip(tt / 2.0, 0, 1) * np.clip((seg + 3 - tt) / 2.0, 0, 1)
        if c == 0: ev = np.clip(tt / 3.0 + 0.0, 0, 1) * np.clip((seg + 3 - tt) / 2.0, 0, 1)
        buf = np.zeros(n)
        for k, iv in enumerate(CH[q]):
            for det in (-0.12, 0.0, 0.14):
                buf += (0.9 if k == 0 else 0.6) * voice(hz(base + iv - 12 + (0 if k else 0)) * 2 ** (det / 12), tt, timbre, rng)
        buf += 0.55 * np.sin(2 * np.pi * hz(base - 24 if base - 24 >= 28 else base - 12) * tt)  # fondamentale grave
        pad[i0:i0 + n] += buf * ev * 0.02
    pad = lp(pad, cut * 1.4, 2)
    rate = p.get('breath', 0.33)
    pad *= 0.78 + 0.22 * np.sin(2 * np.pi * rate * T + rng.random() * 6.28)
    mel = np.zeros(N); inst = p.get('melody', 'bell'); sc = PENTA_M if minor else PENTA
    if inst != 'none':
        step = p.get('mstep', 3.0); t = 2.5
        while t < seconds - 3:
            if rng.random() < p.get('mdens', 0.6):
                m = root + 12 + sc[int(rng.integers(0, 7))]; ln = int(SR * 2.4); tt = np.arange(ln) / SR; f = hz(m)
                if inst == 'bell': s = (np.sin(2 * np.pi * f * tt) + .35 * np.sin(2 * np.pi * f * 2.76 * tt) * np.exp(-tt * 3) + .15 * np.sin(2 * np.pi * f * 5.4 * tt) * np.exp(-tt * 6)) * np.exp(-tt * 1.6)
                elif inst == 'kalimba': s = (np.sin(2 * np.pi * f * tt) + .25 * np.sin(2 * np.pi * f * 3.9 * tt) * np.exp(-tt * 12)) * np.exp(-tt * 3.2)
                else: s = (np.sin(2 * np.pi * f * tt) + .4 * np.sin(4 * np.pi * f * tt) * np.exp(-tt * 5) + .1 * np.sin(6 * np.pi * f * tt) * np.exp(-tt * 9)) * np.exp(-tt * 1.4)  # felt
                add(mel, int(t * SR), 0.05 * s * np.minimum(1, tt / 0.01))
            t += step * (1 + 0.5 * rng.random())
    mel = lp(mel, p.get('mcut', 2600))
    de = int(0.5 * SR); ech = np.zeros(N); ech[de:] = 0.35 * mel[:-de]
    dry = pad + mel + ech
    ir_n = int(SR * 3.0); ir = rng.normal(0, 1, ir_n) * np.exp(-np.arange(ir_n) / SR * 1.8); ir = lp(ir, 2200); ir /= np.abs(ir).sum() ** 0.5 * 12
    wet = fftconvolve(dry, ir)[:N]
    mix = dry * 0.75 + wet
    tex = p.get('texture', 'air')
    if tex == 'air': mix += lp(rng.normal(0, 1, N), 600, 2) * 0.004 * (0.6 + 0.4 * np.sin(2 * np.pi * 0.11 * T))
    elif tex == 'rain':
        for _ in range(int(seconds * 14)):
            i = int(rng.integers(0, N - 100)); mix[i:i + 60] += rng.normal(0, 0.004, 60) * np.exp(-np.arange(60) / 8)
    if p.get('heart'):
        for t in np.arange(1.0, seconds - 2, p['heart']):
            ln = int(SR * .5); tt = np.arange(ln) / SR
            add(mix, int(t * SR), 0.07 * np.sin(2 * np.pi * (46 + 30 * np.exp(-tt * 18)) * tt) * np.exp(-tt * 7))
    mix = lp(mix, 5500)
    mix = mix / (np.max(np.abs(mix)) + 1e-9) * 0.8
    with wave.open(out, 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix * 32767).astype('<i2').tobytes())

if __name__ == '__main__':
    posts = json.load(open('posts.json')); os.makedirs('audio', exist_ok=True)
    for q in posts:
        render(q['music'], out=f"audio/m{q['n']:02d}.wav"); print(q['n'], q['music'])
