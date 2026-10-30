// Rend les diapositives de chaque Reel en PNG 1080x1920 (Playwright). Design A : éditorial bold (crème, bleu, corail).
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const logoRaw = fs.readFileSync(path.join(__dirname, 'logo.svg'), 'utf8').replace('width="46" height="46"', 'width="100%" height="100%"');
const posts = JSON.parse(fs.readFileSync(path.join(__dirname, 'posts.json'), 'utf8'));
const OUT = path.join(__dirname, 'out');

// s1 bleu (accent doré), s2 crème (accent rouge), s3 nuit (accent doré), s4 doré (accent bleu)
const STYLES = {
  s1: { bg: '#000091', fg: '#f3ede1', acc: '#d1ab55', muted: 'rgba(243,237,225,.78)', card: 'rgba(255,255,255,.10)', cardfg: '#f3ede1', cardb: 'rgba(243,237,225,.45)', onacc: '#000091', logoBg: '#f3ede1', logoFg: '#000091', logoGold: '#d1ab55' },
  s2: { bg: '#f3ede1', fg: '#0a0a5c', acc: '#e1000f', muted: '#55557f', card: '#ffffff', cardfg: '#0a0a5c', cardb: '#0a0a5c', onacc: '#fff', logoBg: '#000091', logoFg: '#fff', logoGold: '#d1ab55' },
  s3: { bg: '#07074a', fg: '#f3ede1', acc: '#d1ab55', muted: 'rgba(243,237,225,.75)', card: 'rgba(255,255,255,.08)', cardfg: '#f3ede1', cardb: 'rgba(243,237,225,.4)', onacc: '#07074a', logoBg: '#f3ede1', logoFg: '#07074a', logoGold: '#d1ab55' },
  s4: { bg: '#d1ab55', fg: '#0a0a5c', acc: '#000091', muted: '#3a3320', card: '#ffffff', cardfg: '#0a0a5c', cardb: '#0a0a5c', onacc: '#fff', logoBg: '#000091', logoFg: '#fff', logoGold: '#d1ab55' },
};

const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

function css(st) {
  return `*{margin:0;box-sizing:border-box}
:root{--logo-bg:${st.logoBg};--logo-gold:${st.logoGold};--logo-fg:${st.logoFg}}
body{width:1080px;height:1920px;background:${st.bg};color:${st.fg};font-family:'Inter Display',Inter,sans-serif;position:relative;overflow:hidden}
.mono{font-family:'JetBrains Mono',monospace;font-weight:700;letter-spacing:2px;text-transform:uppercase;font-size:26px}
.top{position:absolute;left:70px;right:70px;top:120px;display:flex;justify-content:space-between;align-items:center;color:${st.fg}}
.brand{display:flex;gap:16px;align-items:center}.brand i{width:56px;height:56px;display:block}
.wrap{position:absolute;left:70px;right:70px;top:250px;bottom:400px;display:flex;flex-direction:column;justify-content:center}
.kicker{display:inline-block;align-self:flex-start;font-family:'JetBrains Mono',monospace;font-weight:700;font-size:28px;letter-spacing:3px;text-transform:uppercase;color:${st.acc};border:3px solid ${st.acc};border-radius:999px;padding:10px 26px;margin-bottom:40px}
h1{font-size:150px;line-height:.95;font-weight:900;letter-spacing:-6px;text-transform:uppercase}
h2{font-size:84px;line-height:1.02;font-weight:900;letter-spacing:-2.5px;margin-bottom:52px}
.note{font-size:42px;font-weight:600;margin-top:50px;color:${st.muted}}
.stk{position:absolute;right:70px;top:300px;width:210px;height:210px;border-radius:50%;background:${st.acc};color:${st.onacc};font-weight:900;font-size:40px;line-height:1.05;display:flex;align-items:center;justify-content:center;text-align:center;transform:rotate(-12deg);box-shadow:0 12px 0 rgba(0,0,0,.14);text-transform:uppercase}
.item{display:flex;gap:30px;align-items:flex-start;margin-bottom:40px;font-size:54px;line-height:1.22;font-weight:600}
.small .item{font-size:45px;margin-bottom:28px}
.num{flex:0 0 76px;height:76px;border-radius:50%;background:${st.acc};color:${st.onacc};font-weight:900;font-size:40px;display:flex;align-items:center;justify-content:center}
.small .num{flex-basis:62px;height:62px;font-size:32px}
.bar{flex:0 0 14px;align-self:stretch;border-radius:7px;background:${st.acc}}
.tag{flex:0 0 120px;font-weight:900;color:${st.acc};font-size:56px;letter-spacing:-1px}
.card{background:${st.card};color:${st.cardfg};border:4px solid ${st.cardb};border-radius:30px;padding:40px 48px;margin-bottom:30px;font-size:50px;line-height:1.25;font-weight:700;box-shadow:10px 10px 0 rgba(0,0,0,.14)}
.opt{display:flex;gap:28px;align-items:center}
.opt b{flex:0 0 82px;height:82px;border-radius:50%;background:${st.acc};color:${st.onacc};font-size:46px;font-weight:900;display:flex;align-items:center;justify-content:center}
.letter{width:300px;height:300px;border-radius:50%;background:${st.acc};color:${st.onacc};font-size:210px;font-weight:900;display:flex;align-items:center;justify-content:center;margin:0 0 50px;transform:rotate(-8deg);box-shadow:0 14px 0 rgba(0,0,0,.14)}
.year{font-size:100px;font-weight:900;letter-spacing:-4px;color:${st.acc};flex:0 0 270px;line-height:1}
.tl{border-left:10px solid ${st.acc};padding-left:36px;margin-left:10px}
.tl .item{margin-bottom:46px;align-items:center}
.col h3{font-family:'JetBrains Mono',monospace;font-size:32px;letter-spacing:3px;color:${st.acc};margin-bottom:16px}
.col .card{font-size:40px;padding:28px 40px}
.col li{margin-bottom:12px;list-style:none;padding-left:34px;position:relative}
.col li:before{content:"";position:absolute;left:0;top:16px;width:16px;height:16px;border-radius:50%;background:${st.acc}}
.scene .card{font-size:50px;line-height:1.3}
.cta{align-items:flex-start}
.cta .biglogo{width:260px;height:260px;margin-bottom:40px}
.cta h1{font-size:190px}
.cta .ln{font-size:52px;font-weight:700;margin-top:18px;line-height:1.25}
.cta .url{background:${st.acc};color:${st.onacc};font-size:52px;font-weight:900;padding:30px 52px;border-radius:999px;margin-top:64px}
.cta .note{font-size:44px;font-weight:800;color:${st.fg}}`;
}

function titleSize(t) { const w = Math.max(...String(t).split(/\s+/).map(x => x.length)); return w <= 8 ? 150 : w <= 10 ? 128 : w <= 12 ? 108 : 92; }

function inner(sl) {
  const k = sl.kicker ? `<div class="kicker">${esc(sl.kicker)}</div>` : '';
  switch (sl.kind) {
    case 'cover':
      return `<div class="stk">${esc((sl.kicker || 'Prep\'CPE').split('·')[0].trim())}</div><div class="wrap">${k}<h1 style="font-size:${titleSize(sl.title)}px">${esc(sl.title)}</h1>${sl.note ? `<div class="note">${esc(sl.note)}</div>` : ''}</div>`;
    case 'list': {
      const num = sl.numbered !== false;
      const items = sl.lines.map((t, i) => {
        const lead = sl.tags ? `<div class="tag">${esc(sl.tags[i] || '')}</div>` : num ? `<div class="num">${i + 1}</div>` : `<div class="bar"></div>`;
        const text = sl.tags ? esc(t.replace(/^M\d : /, '')) : esc(t);
        return `<div class="item">${lead}<div>${text}</div></div>`;
      }).join('');
      return `<div class="wrap ${sl.small ? 'small' : ''}">${k}<h2>${esc(sl.title)}</h2>${items}</div>`;
    }
    case 'scene':
      return `<div class="wrap scene">${k}<h2>${esc(sl.title)}</h2>${sl.lines.map(t => `<div class="card">${esc(t)}</div>`).join('')}</div>`;
    case 'quiz':
      return `<div class="wrap">${k}<h2 style="font-size:66px">${esc(sl.title)}</h2>${sl.options.map((o, i) => `<div class="card opt"><b>${'ABC'[i]}</b><span>${esc(o)}</span></div>`).join('')}</div>`;
    case 'answer':
      return `<div class="wrap">${k}<div class="letter">${esc(sl.letter)}</div><h2 style="margin-bottom:34px">${esc(sl.title)}</h2>${sl.lines.map(t => `<div class="item"><div class="bar"></div><div>${esc(t)}</div></div>`).join('')}</div>`;
    case 'timeline':
      return `<div class="wrap">${k}<h2>${esc(sl.title)}</h2><div class="tl">${sl.items.map(([y, t]) => `<div class="item"><div class="year">${esc(y)}</div><div style="font-size:42px">${esc(t)}</div></div>`).join('')}</div></div>`;
    case 'compare': {
      const col = ([h, ls]) => `<div class="col"><h3>${esc(h)}</h3><div class="card"><ul>${ls.map(l => `<li>${esc(l)}</li>`).join('')}</ul></div></div>`;
      return `<div class="wrap">${k}<h2 style="margin-bottom:30px;font-size:62px">${esc(sl.title)}</h2>${col(sl.left)}${col(sl.right)}</div>`;
    }
    case 'cta':
      return `<div class="wrap cta" style="top:200px"><div class="biglogo">${logoRaw}</div><h1>${esc(sl.title)}</h1>${sl.lines.map(l => `<div class="ln">${esc(l)}</div>`).join('')}<div class="url">${esc(sl.url)}</div><div class="note" style="margin-top:44px">${esc(sl.note)}</div></div>`;
  }
  return '';
}

function charCount(sl) {
  let t = (sl.title || '') + (sl.note || '') + (sl.lines || []).join('') + (sl.options || []).join('');
  if (sl.items) t += sl.items.map(i => i.join('')).join('');
  if (sl.left) t += sl.left[1].join('') + sl.right[1].join('');
  return t.length;
}

function duration(sl) {
  const n = charCount(sl);
  if (sl.kind === 'cover') return Math.max(3.0, Math.min(4.2, 2.2 + n * 0.02));
  if (sl.kind === 'cta') return 3.6;
  let d = 2.6 + n * 0.034;
  if (sl.kind === 'quiz') d += 2.4;
  return Math.max(3.4, Math.min(9.5, d));
}

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 3 });
  const durs = {};
  for (const post of posts) {
    const st = STYLES[post.style];
    const dir = path.join(OUT, 'p' + String(post.n).padStart(2, '0'));
    fs.mkdirSync(dir, { recursive: true });
    durs[post.n] = [];
    for (let i = 0; i < post.slides.length; i++) {
      const sl = post.slides[i];
      const head = `<div class="top"><div class="brand"><i>${logoRaw}</i><span class="mono">@prep_concours_cpe</span></div><span class="mono">${post.fiche ? 'Fiche ' + post.fiche : ''}</span></div>`;
      await p.setContent(`<style>${css(st)}</style><body>${sl.kind === 'cta' ? '' : head}${inner(sl)}</body>`);
      await p.waitForTimeout(60);
      await p.screenshot({ path: path.join(dir, `s${i + 1}.png`) });
      durs[post.n].push(Number(duration(sl).toFixed(2)));
    }
  }
  fs.writeFileSync(path.join(OUT, 'durations.json'), JSON.stringify(durs));
  await b.close();
  console.log('ok', Object.values(durs).map(d => d.reduce((a, b) => a + b, 0).toFixed(1)).join(' '));
})();
