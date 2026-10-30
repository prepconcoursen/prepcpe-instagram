import json, subprocess, sys, os
posts = json.load(open('posts.json')); durs = json.load(open('out/durations.json'))
X = 0.4; FPS = 30
def run(c):
    r = subprocess.run(c, capture_output=True, text=True)
    if r.returncode: print(r.stderr[-1500:]); sys.exit(1)

from PIL import Image
def zoom_clip(img, clip, frames, zoom_in):
    """Zoom lent de 3 %, rééchantillonné au sous-pixel (resize avec boîte flottante) : pas de saccade."""
    src = Image.open(img).convert('RGB'); W, H = 1080, 1920
    src = src.resize((2 * W, 2 * H), Image.LANCZOS)
    p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '19', '-pix_fmt', 'yuv420p', clip], stdin=subprocess.PIPE)
    for k in range(frames):
        u = k / max(1, frames - 1); z = 1 + 0.03 * (u if zoom_in else 1 - u)
        w, h = 2 * W / z, 2 * H / z; l, t = (2 * W - w) / 2, (2 * H - h) / 2
        p.stdin.write(src.resize((W, H), Image.LANCZOS, box=(l, t, l + w, t + h)).tobytes())
    p.stdin.close()
    if p.wait(): print('ffmpeg clip error'); sys.exit(1)
os.makedirs('video', exist_ok=True)
only = [int(a) for a in sys.argv[1:]]
for p in posts:
    n = p['n']
    if only and n not in only: continue
    d = durs[str(n)]; k = len(d); clips = []
    for i, dur in enumerate(d):
        img = f'out/p{n:02d}/s{i+1}.png'; clip = f'video/tmp_{n:02d}_{i+1}.mp4'
        frames = int((dur + X) * FPS)
        zoom_clip(img, clip, frames, i % 2 == 0)
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
    if os.environ.get('MUET_ONLY'):
        for c in clips: os.remove(c)
        print(n, f'{total:.1f}s muet'); continue
    final = f'video/prepcpe_{n:02d}.mp4'
    af = f"atrim=0:{total:.2f},afade=t=in:d=0.4,afade=t=out:st={total-1.8:.2f}:d=1.8,loudnorm=I={os.environ.get('LOUD','-17')}:TP=-1.5:LRA=7"
    run(['ffmpeg', '-y', '-i', muet, '-i', f'audio/m{n:02d}.wav', '-filter_complex', f'[1:a]{af},aresample=44100[a]', '-map', '0:v', '-map', '[a]', '-t', f'{total:.2f}', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '160k', '-ac', '2', '-movflags', '+faststart', final])
    for c in clips: os.remove(c)
    print(n, f'{total:.1f}s', os.path.getsize(final) // 1024, 'Ko')
