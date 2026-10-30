"""Refait la musique des Reels 3 à 14 du lot 2 avec la palette de music4.py, sur les vidéos muettes existantes.
Usage : python3 remix_lot02.py (depuis tools/) ; écrit ../lot-02/prepcpe_NN.mp4."""
import os, subprocess, music4
M = {
 3: dict(style="ambient", root=52, prog="c", timbre="string", melody="bell", breath=0.28, texture="air", cut=850, seed=503),
 4: dict(style="pluck", bpm=84, root=57, prog="min_a", seed=504, step=0.5, octs=[0, 1], shaker=True, pad=0.003),
 5: dict(style="piano", bpm=72, root=62, prog="maj_c", seed=505, step=0.5, octs=[0, 1]),
 6: dict(style="pulse", bpm=100, root=55, prog="min_a", seed=506, cut=1800),
 7: dict(bpm=80, root=59, prog="maj_b", seed=507, lead=True),
 8: dict(style="piano", bpm=56, root=50, prog="min_b", seed=508, step=1.0, octs=[0, 1, 2], pattern=[0, 2, 1, 3], pad=0.006, room=0.5),
 9: dict(style="pluck", bpm=96, root=60, prog="maj_c", seed=509, step=0.5, octs=[0, 1], shaker=True),
 10: dict(style="ambient", root=55, prog="d", timbre="warm", melody="kalimba", breath=0.36, texture="air", cut=700, seed=510, minor=False, mstep=2.2),
 11: dict(style="pulse", bpm=108, root=62, prog="maj_a", seed=511, cut=2000),
 12: dict(style="piano", bpm=62, root=53, prog="min_a", seed=512, step=0.75, octs=[0, 1, 2], pad=0.005, room=0.45),
 13: dict(bpm=90, root=64, prog="maj_a", seed=513, lead=True),
 14: dict(style="ambient", root=57, prog="b", timbre="glass", melody="felt", breath=0.25, texture="none", cut=1000, seed=514, minor=False),
}
os.makedirs('audio', exist_ok=True)
for n, p in M.items():
    wav = f'audio/r{n:02d}.wav'; music4.render(p, out=wav)
    muet = f'../lot-02/muet/prepcpe_{n:02d}_muet.mp4'
    d = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', muet]))
    af = f"atrim=0:{d:.2f},afade=t=in:d=0.4,afade=t=out:st={d-1.8:.2f}:d=1.8,loudnorm=I=-17:TP=-1.5:LRA=7"
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', muet, '-i', wav, '-filter_complex', f'[1:a]{af},aresample=44100[a]', '-map', '0:v', '-map', '[a]',
                    '-t', f'{d:.2f}', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '160k', '-ac', '2', '-movflags', '+faststart', f'../lot-02/prepcpe_{n:02d}.mp4'], check=True)
    print(n, p.get('style', 'lofi'), round(d, 1))
