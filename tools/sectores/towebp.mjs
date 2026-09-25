import { chromium } from 'playwright';
import fs from 'fs';
// uso: node towebp.mjs entrada.jpg salida-base anchos(csv) calidad
const [src, base, widths, q, cropL = '0', ratio = '0'] = process.argv.slice(2);
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox'] });
const p = await b.newPage();
await p.setContent('<img id="s" src="data:image/jpeg;base64,' + fs.readFileSync(src).toString('base64') + '">');
await p.waitForFunction(() => { const i = document.getElementById('s'); return i.complete && i.naturalWidth > 0; });
const [nw, nh] = await p.evaluate(() => { const i = document.getElementById('s'); return [i.naturalWidth, i.naturalHeight]; });
console.log(`  origen ${nw}x${nh}`);
for (const w of widths.split(',').map(Number)) {
  const r = await p.evaluate(([w, q, cl, rt]) => {
    const i = document.getElementById('s'); const sx = Math.round(i.naturalWidth * cl), sw = i.naturalWidth - sx;
    let sy = 0, sh = i.naturalHeight;
    if (rt > 0) { sh = Math.round(sw / rt); sy = Math.round((i.naturalHeight - sh) / 2); }
    const h = Math.round(sh * w / sw);
    const c = document.createElement('canvas'); c.width = w; c.height = h;
    const x = c.getContext('2d'); x.imageSmoothingQuality = 'high'; x.drawImage(i, sx, sy, sw, sh, 0, 0, w, h);
    return { d: c.toDataURL('image/webp', q), h };
  }, [w, Number(q), Number(cropL), eval(ratio)]);
  const buf = Buffer.from(r.d.split(',')[1], 'base64');
  fs.writeFileSync(`${base}-${w}.webp`, buf);
  console.log(`  ${base.split('/').pop()}-${w}.webp  ${w}x${r.h}  ${(buf.length/1024).toFixed(0)} KB`);
}
await b.close();
