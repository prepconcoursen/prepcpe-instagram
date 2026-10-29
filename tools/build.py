import json, subprocess, sys, os
posts = json.load(open('posts.json')); durs = json.load(open('out/durations.json'))
X = 0.4; FPS = 30
def run(c):
    r = subprocess.run(c, capture_output=True, text=True)
    if r.returncode: print(r.stderr[-1500:]); sys.exit(1)
os.makedirs('video', exist_ok=True)
only = [int(a) for a in sys.argv[1:]]
for p in posts:
    n = p['n']
    if only and n not in only: continue
    d = durs[str(n)]; k = len(d); clips = []
    for i, dur in enumerate(d):
        img = f'out/p{n:02d}/s{i+1}.png'; clip = f'video/tmp_{n:02d}_{i+1}.mp4'
        frames = int((dur + X) * FPS)
        z = f"1+0.03*on/{frames}" if i % 2 == 0 else f"1.03-0.03*on/{frames}"
        vf = f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps={FPS},format=yuv420p"
        run(['ffmpeg', '-y', '-framerate', str(FPS), '-loop', '1', '-t', f'{dur + X:.2f}', '-i', img, '-vf', vf, '-frames:v', str(frames), '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', clip])
        clips.append(clip)
    inp = []; [inp.extend(['-i', c]) for c in clips]
    f = ''; prev = '[0:v]'; off = 0.0
    for i in range(1, k):
        off += d[i - 1]; out = f'[v{i}]'
        f += f"{prev}[{i}:v]xfade=transition=fade:duration={X}:offset={off:.2f}{out};"; prev = out
    total = sum(d) + X  # dernière diapo : sa durée + marge de fondu
    total = sum(d)
    muet = f'video/prepcpe_{n:02d}_muet.mp4'
    run(['ffmpeg', '-y', *inp, '-filter_complex', f.rstrip(';') if k > 1 else '[0:v]null[v1]', '-map', prev if k > 1 else '[v1]', '-t', f'{total:.2f}', '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p', '-r', str(FPS), '-an', '-movflags', '+faststart', muet])
    final = f'video/prepcpe_{n:02d}.mp4'
    af = f"atrim=0:{total:.2f},afade=t=in:d=0.4,afade=t=out:st={total-1.8:.2f}:d=1.8,loudnorm=I=-17:TP=-1.5:LRA=7"
    run(['ffmpeg', '-y', '-i', muet, '-i', f'audio/m{n:02d}.wav', '-filter_complex', f'[1:a]{af},aresample=44100[a]', '-map', '0:v', '-map', '[a]', '-t', f'{total:.2f}', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '160k', '-ac', '2', '-movflags', '+faststart', final])
    for c in clips: os.remove(c)
    print(n, f'{total:.1f}s', os.path.getsize(final) // 1024, 'Ko')
