"""Générateur de morceaux lofi originaux, sans paroles (numpy). Un morceau par Reel."""
import numpy as np, wave, json, sys
SR = 44100

PROGS = {
    # (demi-tons depuis la tonique, qualité)
    'maj_a': [(0, 'maj7'), (9, 'm7'), (2, 'm7'), (7, 'dom7')],
    'maj_b': [(2, 'm7'), (7, 'dom7'), (0, 'maj7'), (5, 'maj7')],
    'maj_c': [(0, 'maj7'), (4, 'm7'), (9, 'm7'), (5, 'maj7')],
    'min_a': [(0, 'm7'), (5, 'm7'), (10, 'dom7'), (3, 'maj7')],
    'min_b': [(0, 'm7'), (8, 'maj7'), (3, 'maj7'), (10, 'dom7')],
}
QUAL = {'maj7': [0, 4, 7, 11], 'm7': [0, 3, 7, 10], 'dom7': [0, 4, 7, 10]}
PENTA_MAJ = [0, 2, 4, 7, 9]
PENTA_MIN = [0, 3, 5, 7, 10]

def hz(m): return 440.0 * 2 ** ((m - 69) / 12)

def lowpass(x, fc):
    a = np.exp(-2 * np.pi * fc / SR); y = np.empty_like(x); s = 0.0
    for i in range(len(x)):
        s = (1 - a) * x[i] + a * s; y[i] = s
    return y

def add(buf, i, sig):
    if i < 0:
        sig = sig[-i:]; i = 0
    j = min(len(buf), i + len(sig))
    if i < len(buf) and j > i: buf[i:j] += sig[:j - i]

def epiano(f, dur, vel):
    n = int(SR * dur); t = np.arange(n) / SR
    env = np.minimum(1, t / 0.006) * np.exp(-t * 2.6)
    tine = np.sin(2 * np.pi * f * t) + 0.35 * np.sin(2 * np.pi * 2 * f * t + 0.5) * np.exp(-t * 7) + 0.12 * np.sin(2 * np.pi * 3 * f * t) * np.exp(-t * 11)
    trem = 1 + 0.12 * np.sin(2 * np.pi * 4.3 * t)
    return vel * env * tine * trem

def render(params, seconds=34, out='track.wav'):
    rng = np.random.default_rng(params['seed'])
    bpm = params['bpm']; beat = 60 / bpm
    root = params['root']; prog = PROGS[params['prog']]
    minor = params['prog'].startswith('min')
    N = int(SR * seconds)
    chords = np.zeros(N); bass = np.zeros(N); drums = np.zeros(N); lead = np.zeros(N)
    swing = 0.08 * beat
    bar = 4 * beat
    nbars = int(seconds / bar) + 1
    scale = PENTA_MIN if minor else PENTA_MAJ
    for b in range(nbars):
        off, qual = prog[b % 4]
        base = root + off
        notes = [base + iv for iv in QUAL[qual]]
        # voicing : tierces et septième au-dessus de la fondamentale, une octave plus haut
        voic = [n + 12 if n < root + 3 else n for n in notes]
        t0 = b * bar
        # accord joué sur les temps 1 et 3 avec léger décalage (« humanisé »)
        for hit, dt in ((0, 0), (2.5, 0)):
            ts = t0 + hit * beat + rng.normal(0, 0.006)
            for k, n in enumerate(voic):
                add(chords, int(ts * SR) + int(k * 0.011 * SR), epiano(hz(n), 1.9, 0.17 if hit == 0 else 0.12))
        # basse
        bn = base - 12 if base - 12 >= 36 else base
        for hit in (0, 1.5, 2.5):
            ts = t0 + hit * beat
            n = int(SR * beat * 1.1); t = np.arange(n) / SR
            env = np.minimum(1, t / 0.01) * np.exp(-t * 3.2)
            add(bass, int(ts * SR), 0.22 * env * (np.sin(2 * np.pi * hz(bn) * t) + 0.25 * np.sin(2 * np.pi * 2 * hz(bn) * t)))
        # batterie
        for step in range(8):
            ts = t0 + step * beat / 2 + (swing if step % 2 else 0) + rng.normal(0, 0.004)
            i = int(ts * SR)
            if step in (0, 3 if params['seed'] % 2 else 4) or (step == 6 and rng.random() < 0.4):
                n = int(SR * 0.28); t = np.arange(n) / SR
                f = 45 + 90 * np.exp(-t * 28)
                add(drums, i, 0.38 * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9))
            if step in (2, 6):
                n = int(SR * 0.22); t = np.arange(n) / SR
                nz = rng.normal(0, 1, n); nz = nz - lowpass(nz, 1500)
                add(drums, i, 0.12 * (0.7 * nz + 0.5 * np.sin(2 * np.pi * 190 * t)) * np.exp(-t * 17))
            n = int(SR * 0.05); t = np.arange(n) / SR
            hv = (0.035 if step % 2 == 0 else 0.022) * (0.7 + 0.6 * rng.random())
            nz = rng.normal(0, 1, n); nz = nz - lowpass(nz, 6000)
            add(drums, i, hv * nz * np.exp(-t * 70))
        # mélodie : notes rares sur la gamme pentatonique
        if params.get('lead'):
            pos = 0
            while pos < 4 * 2:
                if rng.random() < 0.55:
                    deg = scale[int(rng.integers(0, len(scale)))]
                    oct_ = 12 * int(rng.choice([1, 1, 2]))
                    m = root + 12 + deg + oct_ - (12 if oct_ == 24 and deg > 5 else 0)
                    ts = t0 + pos * beat / 2
                    n = int(SR * 0.9); t = np.arange(n) / SR
                    f = hz(m)
                    sig = (np.sin(2 * np.pi * f * t) + 0.2 * np.sin(2 * np.pi * 2 * f * t)) * np.exp(-t * 4.5) * np.minimum(1, t / 0.01)
                    add(lead, int(ts * SR), 0.13 * sig)
                    pos += int(rng.choice([2, 3, 4]))
                else:
                    pos += 1
    mix = chords + bass + drums + lead
    mix = lowpass(lowpass(lowpass(mix, 4300), 4300), 4300)
    # écho léger sur l'ensemble
    d = int(0.36 * beat / 0.4 * SR / 2)
    echo = np.zeros_like(mix); echo[d:] = 0.28 * mix[:-d]
    mix = mix + echo
    # craquements de vinyle et souffle
    crack = np.zeros(N)
    for _ in range(int(seconds * 7)):
        i = int(rng.integers(0, N - 200)); crack[i:i + 40] += rng.normal(0, 0.05, 40) * np.exp(-np.arange(40) / 6)
    hiss = lowpass(rng.normal(0, 0.004, N), 3500)
    mix = mix + crack + hiss
    mix = mix / (np.max(np.abs(mix)) + 1e-9) * 0.85
    pcm = (mix * 32767).astype('<i2')
    with wave.open(out, 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
    return float(np.sqrt(np.mean(mix ** 2)))

if __name__ == '__main__':
    posts = json.load(open('posts.json'))
    import os
    os.makedirs('audio', exist_ok=True)
    for p in posts:
        r = render(p['music'], out=f"audio/m{p['n']:02d}.wav")
        print(p['n'], p['music']['bpm'], p['music']['root'], p['music']['prog'], round(r, 3))
