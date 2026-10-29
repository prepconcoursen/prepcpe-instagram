// Rend les diapositives de chaque Reel en PNG 1080x1920 (Playwright).
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const logoRaw = fs.readFileSync(path.join(__dirname, 'logo.svg'), 'utf8').replace('width="46" height="46"', 'width="100%" height="100%"');
const posts = JSON.parse(fs.readFileSync(path.join(__dirname, 'posts.json'), 'utf8'));
const OUT = path.join(__dirname, 'out');

const STYLES = {
  s1: { bg: '#000091', fg: '#ffffff', acc: '#d1ab55', muted: 'rgba(255,255,255,.72)', card: 'rgba(255,255,255,.10)', cardfg: '#fff', logoBg: '#000091', logoFg: '#fff', flag: 'linear-gradient(90deg,#000091 33%,#fff 33% 66%,#e1000f 66%)' },
  s2: { bg: '#f6f7f9', fg: '#1d2430', acc: '#000091', muted: '#5d6878', card: '#ffffff', cardfg: '#1d2430', logoBg: '#000091', logoFg: '#fff', flag: 'linear-gradient(90deg,#000091 33%,#dde2e8 33% 66%,#e1000f 66%)' },
  s3: { bg: '#14181e', fg: '#e6e9ee', acc: '#8585f6', muted: '#9aa5b4', card: '#1c222a', cardfg: '#e6e9ee', logoBg: '#000091', logoFg: '#fff', flag: 'linear-gradient(90deg,#8585f6 33%,#2d3540 33% 66%,#e1000f 66%)' },
  s4: { bg: '#faf3e3', fg: '#1d2430', acc: '#c4161c', muted: '#6b5f4b', card: '#ffffff', cardfg: '#1d2430', logoBg: '#000091', logoFg: '#fff', flag: 'linear-gradient(90deg,#000091 33%,#fff 33% 66%,#e1000f 66%)' },
};

const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

function css(st) {
  return `*{margin:0;box-sizing:border-box}
:root{--logo-bg:${st.logoBg};--logo-gold:#d1ab55;--logo-fg:${st.logoFg}}
body{width:1080px;height:1920px;background:${st.bg};color:${st.fg};font-family:Inter,sans-serif;position:relative;overflow:hidden}
.flag{position:absolute;top:0;left:0;right:0;height:16px;background:${st.flag}}
.wrap{position:absolute;left:80px;right:80px;top:190px;bottom:380px;display:flex;flex-direction:column;justify-content:center}
.kicker{font-size:34px;font-weight:700;letter-spacing:5px;text-transform:uppercase;color:${st.acc};margin-bottom:34px}
h1{font-size:100px;line-height:1.06;font-weight:800;letter-spacing:-1px}
h2{font-size:78px;line-height:1.12;font-weight:800;margin-bottom:52px}
.note{font-size:40px;margin-top:48px;color:${st.muted}}
.item{display:flex;gap:30px;align-items:flex-start;margin-bottom:40px;font-size:54px;line-height:1.28}
.small .item{font-size:45px;margin-bottom:28px}
.num{flex:0 0 74px;height:74px;border-radius:50%;background:${st.acc};color:${st.bg === '#000091' ? '#000091' : '#fff'};font-weight:800;font-size:38px;display:flex;align-items:center;justify-content:center}
.small .num{flex-basis:62px;height:62px;font-size:32px}
.bar{flex:0 0 12px;align-self:stretch;border-radius:6px;background:${st.acc}}
.tag{flex:0 0 96px;font-weight:800;color:${st.acc};font-size:44px}
.card{background:${st.card};color:${st.cardfg};border-radius:30px;padding:44px 50px;margin-bottom:30px;font-size:52px;line-height:1.28;font-weight:600}
.opt{display:flex;gap:28px;align-items:center}
.opt b{flex:0 0 78px;height:78px;border-radius:50%;background:${st.acc};color:${st.bg === '#000091' ? '#000091' : '#fff'};font-size:42px;display:flex;align-items:center;justify-content:center}
.letter{width:300px;height:300px;border-radius:50%;background:${st.acc};color:${st.bg === '#000091' ? '#000091' : '#fff'};font-size:200px;font-weight:800;display:flex;align-items:center;justify-content:center;margin:0 0 50px}
.year{font-family:Georgia,serif;font-size:76px;font-weight:700;color:${st.acc};flex:0 0 230px;line-height:1}
.tl{border-left:8px solid ${st.acc};padding-left:36px;margin-left:10px}
.tl .item{margin-bottom:46px;align-items:center}
.col h3{font-size:36px;letter-spacing:4px;color:${st.acc};margin-bottom:18px}
.col .card{font-size:41px;padding:30px 40px}
.col li{margin-bottom:12px;list-style:none;padding-left:32px;position:relative}
.col li:before{content:"";position:absolute;left:0;top:18px;width:14px;height:14px;border-radius:50%;background:${st.acc}}
.scene .card{font-size:52px;line-height:1.35}
.foot{position:absolute;left:80px;right:80px;bottom:300px;display:flex;justify-content:space-between;align-items:center;font-size:32px;font-weight:600;color:${st.muted}}
.foot .l{display:flex;gap:18px;align-items:center}.foot .lg{width:58px;height:58px;display:inline-block}
.cta{align-items:center;text-align:center}
.cta .biglogo{width:300px;height:300px;margin-bottom:40px}
.cta h1{font-family:Georgia,serif;font-size:120px}
.cta .ln{font-size:48px;font-weight:600;margin-top:20px;line-height:1.3}
.cta .url{background:${st.acc};color:${st.bg === '#000091' ? '#000091' : '#fff'};font-size:50px;font-weight:800;padding:30px 50px;border-radius:26px;margin-top:70px}
.cta .note{font-size:46px;font-weight:700;color:${st.fg}}`;
}

function inner(sl) {
  const k = sl.kicker ? `<div class="kicker">${esc(sl.kicker)}</div>` : '';
  switch (sl.kind) {
    case 'cover':
      return `<div class="wrap">${k}<h1>${esc(sl.title)}</h1>${sl.note ? `<div class="note">${esc(sl.note)}</div>` : ''}</div>`;
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
      return `<div class="wrap">${k}<h2 style="font-size:64px">${esc(sl.title)}</h2>${sl.options.map((o, i) => `<div class="card opt"><b>${'ABC'[i]}</b><span>${esc(o)}</span></div>`).join('')}</div>`;
    case 'answer':
      return `<div class="wrap">${k}<div class="letter">${esc(sl.letter)}</div><h2 style="margin-bottom:34px">${esc(sl.title)}</h2>${sl.lines.map(t => `<div class="item"><div class="bar"></div><div>${esc(t)}</div></div>`).join('')}</div>`;
    case 'timeline':
      return `<div class="wrap">${k}<h2>${esc(sl.title)}</h2><div class="tl">${sl.items.map(([y, t]) => `<div class="item"><div class="year">${esc(y)}</div><div style="font-size:42px">${esc(t)}</div></div>`).join('')}</div></div>`;
    case 'compare': {
      const col = ([h, ls]) => `<div class="col"><h3>${esc(h)}</h3><div class="card"><ul>${ls.map(l => `<li>${esc(l)}</li>`).join('')}</ul></div></div>`;
      return `<div class="wrap">${k}<h2 style="margin-bottom:30px;font-size:60px">${esc(sl.title)}</h2>${col(sl.left)}${col(sl.right)}</div>`;
    }
    case 'cta':
      return `<div class="wrap cta"><div class="biglogo">${logoRaw}</div><h1>${esc(sl.title)}</h1>${sl.lines.map(l => `<div class="ln">${esc(l)}</div>`).join('')}<div class="url">${esc(sl.url)}</div><div class="note" style="margin-top:44px">${esc(sl.note)}</div></div>`;
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
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  const durs = {};
  for (const post of posts) {
    const st = STYLES[post.style];
    const dir = path.join(OUT, 'p' + String(post.n).padStart(2, '0'));
    fs.mkdirSync(dir, { recursive: true });
    durs[post.n] = [];
    for (let i = 0; i < post.slides.length; i++) {
      const sl = post.slides[i];
      const foot = `<div class="foot"><div class="l"><span class="lg">${logoRaw}</span>@prep_concours_cpe</div><div>${post.fiche ? 'Fiche ' + post.fiche : ''}</div></div>`;
      await p.setContent(`<style>${css(st)}</style><body><div class="flag"></div>${inner(sl)}${sl.kind === 'cta' ? '' : foot}</body>`);
      await p.waitForTimeout(60);
      await p.screenshot({ path: path.join(dir, `s${i + 1}.png`) });
      durs[post.n].push(Number(duration(sl).toFixed(2)));
    }
  }
  fs.writeFileSync(path.join(OUT, 'durations.json'), JSON.stringify(durs));
  await b.close();
  console.log('ok', Object.values(durs).map(d => d.reduce((a, b) => a + b, 0).toFixed(1)).join(' '));
})();
