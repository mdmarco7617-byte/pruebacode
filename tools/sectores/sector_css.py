# -*- coding: utf-8 -*-
# CSS comun a todas las paginas de sector. Todo acotado bajo .vsx.
# El color del sector llega por variables en el atributo style del
# contenedor (--s, --s-dark, --s-light, --s-soft, --s-rgb).
CSS = r"""
<style>
.vsx{
  --ink:#1a1a1a; --text:#333; --muted:#5f6673; --border:#ebe6ea;
  --r:18px; --r-lg:26px;
  --sh-s:0 1px 2px rgba(20,16,24,.06);
  --sh-m:0 16px 36px -16px rgba(20,16,24,.22);
  --sh-l:0 30px 60px -28px rgba(20,16,24,.30);
  --max:1180px; --ease:cubic-bezier(.16,1,.3,1);
  font-family:'DM Sans',system-ui,-apple-system,"Segoe UI",sans-serif;
  color:var(--text);font-size:17px;line-height:1.65;
  -webkit-font-smoothing:antialiased;overflow-x:hidden;
}
.vsx *,.vsx *::before,.vsx *::after{box-sizing:border-box}
.vsx :where(h1,h2,h3,h4){font-family:'Manrope','DM Sans',sans-serif;color:var(--ink);
  line-height:1.15;letter-spacing:-.022em;font-weight:700;margin:0}
.vsx :where(p,ul,ol,figure){margin:0;padding:0}
.vsx :where(li){list-style:none}
.vsx :where(a){color:inherit;text-decoration:none}
.vsx :where(img){display:block;max-width:100%;height:auto}
.vsx svg{display:block}
.vsx-wrap{max-width:var(--max);margin:0 auto}
.vsx-sec{padding:96px 24px;position:relative}
.vsx-sec--soft{background:var(--s-soft)}
.vsx-head{max-width:740px;margin:0 auto 56px;text-align:center}
.vsx-head h2{font-size:clamp(29px,3.8vw,42px);margin:0 0 16px;text-wrap:balance}
.vsx-head p{font-size:18px;color:var(--muted)}
.vsx-eyebrow{display:inline-flex;align-items:center;gap:8px;margin:0 0 16px;
  font-family:'Manrope',sans-serif;font-size:12.5px;font-weight:800;letter-spacing:.14em;
  text-transform:uppercase;color:var(--s-dark)}
.vsx-eyebrow::before{content:'';width:22px;height:2px;border-radius:2px;background:var(--s)}

/* ---------- botones ---------- */
.vsx-btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;
  font-family:'Manrope',sans-serif;font-size:15.5px;font-weight:700;padding:15px 28px;
  border-radius:999px;border:1px solid transparent;cursor:pointer;
  transition:transform .25s var(--ease),box-shadow .25s var(--ease),background .2s,border-color .2s}
.vsx-btn svg{width:17px;height:17px;transition:transform .25s var(--ease)}
.vsx-btn:hover svg{transform:translateX(3px)}
.vsx-btn--p{background:linear-gradient(135deg,var(--s),var(--s-dark));color:#fff;
  box-shadow:0 12px 26px -12px rgba(var(--s-rgb),.8)}
.vsx-btn--p:hover{transform:translateY(-3px);box-shadow:0 20px 36px -14px rgba(var(--s-rgb),.85)}
.vsx-btn--g{background:#fff;color:var(--ink);border-color:var(--border);box-shadow:var(--sh-s)}
.vsx-btn--g:hover{transform:translateY(-3px);box-shadow:var(--sh-m);border-color:var(--s-light)}
.vsx-btn--w{background:#fff;color:var(--ink)}
.vsx-btn--w:hover{transform:translateY(-3px);box-shadow:0 20px 36px -16px rgba(0,0,0,.5)}
.vsx-btn--o{background:transparent;color:#fff;border-color:rgba(255,255,255,.35)}
.vsx-btn--o:hover{background:rgba(255,255,255,.1);transform:translateY(-3px)}
.vsx a:focus-visible,.vsx summary:focus-visible{outline:3px solid var(--s);outline-offset:3px;border-radius:12px}
.vsx-ctas{display:flex;flex-wrap:wrap;gap:14px;margin-top:32px}

/* ---------- hero ---------- */
.vsx-hero{padding:34px 24px 96px;position:relative;isolation:isolate;overflow:hidden}
.vsx-hero::before{content:'';position:absolute;inset:-12% -6%;z-index:-1;pointer-events:none;
  background:radial-gradient(560px 340px at 6% 18%,rgba(var(--s-rgb),.13),transparent 70%),
             radial-gradient(520px 360px at 94% 82%,rgba(var(--s-rgb),.10),transparent 70%);
  animation:vsxAur 18s ease-in-out infinite alternate}
@keyframes vsxAur{to{transform:translate3d(-2.5%,1.5%,0) scale(1.06)}}
.vsx-crumb{max-width:var(--max);margin:0 auto 34px;font-size:13.5px;color:var(--muted)}
.vsx-crumb ol{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.vsx-crumb li{display:flex;align-items:center;gap:8px}
.vsx-crumb li+li::before{content:'›';color:#b9b0b6}
.vsx-crumb a:hover{color:var(--s-dark);text-decoration:underline}
.vsx-crumb [aria-current]{color:var(--ink);font-weight:600}
.vsx-hero-grid{max-width:var(--max);margin:0 auto;display:grid;
  grid-template-columns:1.05fr .95fr;gap:60px;align-items:center}
.vsx-tag{display:inline-flex;align-items:center;gap:10px;padding:7px 16px 7px 8px;margin:0 0 20px;
  border-radius:999px;background:#fff;border:1px solid var(--s-light);box-shadow:var(--sh-s);
  font-family:'Manrope',sans-serif;font-size:13px;font-weight:700;color:var(--s-dark)}
.vsx-tag i{width:28px;height:28px;border-radius:50%;display:grid;place-items:center;
  background:linear-gradient(135deg,var(--s),var(--s-dark));color:#fff}
.vsx-tag svg{width:16px;height:16px}
.vsx-hero h1{font-size:clamp(33px,4.7vw,54px);margin:0 0 22px;text-wrap:balance}
.vsx-hero h1 em{font-style:normal;background:linear-gradient(120deg,var(--s),var(--s-dark));
  -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}
.vsx-lead{font-size:19px;max-width:580px}
.vsx-lead strong{color:var(--ink)}
.vsx-chips{display:flex;flex-wrap:wrap;gap:10px;margin-top:30px}
.vsx-chips li{display:flex;align-items:center;gap:7px;padding:7px 14px;border-radius:999px;
  background:var(--s-soft);font-size:13.5px;font-weight:600;color:var(--s-dark)}
.vsx-chips svg{width:15px;height:15px}
.vsx-media{position:relative}
.vsx-media>img{border-radius:var(--r-lg);box-shadow:var(--sh-l);aspect-ratio:3/2;object-fit:cover;width:100%}
.vsx-media::before{content:'';position:absolute;z-index:-1;inset:auto -22px -22px auto;width:62%;height:62%;
  border-radius:var(--r-lg);background:linear-gradient(135deg,rgba(var(--s-rgb),.22),rgba(var(--s-rgb),.06))}
.vsx-hero-copy{animation:vsxUp .8s var(--ease) both}
.vsx-media{animation:vsxUp .9s .12s var(--ease) both}
@keyframes vsxUp{from{opacity:0;transform:translateY(26px)}to{opacity:1;transform:none}}

/* ---------- tarjetas de problema ---------- */
.vsx-g4{display:grid;grid-template-columns:repeat(4,1fr);gap:22px}
.vsx-pain{background:#fff;border:1px solid var(--border);border-radius:var(--r);padding:28px 24px;
  box-shadow:var(--sh-s);transition:transform .28s var(--ease),box-shadow .28s var(--ease),border-color .28s}
.vsx-pain:hover{transform:translateY(-5px);box-shadow:var(--sh-m);border-color:var(--s-light)}
.vsx-pain i{width:46px;height:46px;border-radius:13px;display:grid;place-items:center;margin-bottom:18px;
  background:var(--s-soft);color:var(--s-dark)}
.vsx-pain svg{width:22px;height:22px}
.vsx-pain h3{font-size:17.5px;margin:0 0 8px}
.vsx-pain p{font-size:15px;color:var(--muted)}
.vsx-summary{max-width:860px;margin:44px auto 0;padding:24px 30px;border-radius:var(--r);
  background:#fff;border:1px solid var(--s-light);border-left:4px solid var(--s);
  font-size:16.5px;box-shadow:var(--sh-s)}
.vsx-summary strong{color:var(--ink)}

/* ---------- los 4 servicios ---------- */
.vsx-svcs{display:grid;grid-template-columns:repeat(2,1fr);gap:26px}
.vsx-svc{position:relative;background:#fff;border:1px solid var(--border);border-radius:var(--r-lg);
  padding:36px 34px 32px;box-shadow:var(--sh-s);display:flex;flex-direction:column;overflow:hidden;
  transition:transform .3s var(--ease),box-shadow .3s var(--ease),border-color .3s}
.vsx-svc::before{content:'';position:absolute;left:0;right:0;top:0;height:4px;
  background:linear-gradient(90deg,var(--s),var(--s-light));opacity:.9}
.vsx-svc:hover{transform:translateY(-6px);box-shadow:var(--sh-l);border-color:var(--s-light)}
.vsx-svc-top{display:flex;align-items:center;gap:16px;margin-bottom:18px}
.vsx-svc-ico{width:58px;height:58px;flex:0 0 auto;border-radius:16px;display:grid;place-items:center;color:#fff;
  background:linear-gradient(135deg,var(--s),var(--s-dark));box-shadow:0 10px 22px -10px rgba(var(--s-rgb),.8);
  transition:transform .3s var(--ease)}
.vsx-svc:hover .vsx-svc-ico{transform:scale(1.07) rotate(-5deg)}
.vsx-svc-ico svg{width:28px;height:28px}
.vsx-svc-n{font-family:'Manrope',sans-serif;font-size:12px;font-weight:800;letter-spacing:.14em;
  text-transform:uppercase;color:var(--s-dark)}
.vsx-svc h3{font-size:22px;margin:4px 0 0;line-height:1.25}
.vsx-svc>p{font-size:16px;margin-bottom:18px}
.vsx-svc ul{display:grid;gap:10px;margin-bottom:22px}
.vsx-svc li{display:flex;gap:10px;font-size:15px;line-height:1.5}
.vsx-svc li svg{width:18px;height:18px;flex:0 0 auto;margin-top:2px;color:var(--s)}
.vsx-svc-res{margin-top:auto;padding:14px 16px;border-radius:12px;background:var(--s-soft);
  font-size:14.5px;color:var(--ink)}
.vsx-svc-res b{color:var(--s-dark)}
.vsx-svc-link{display:inline-flex;align-items:center;gap:7px;margin-top:18px;align-self:flex-start;
  font-family:'Manrope',sans-serif;font-size:14.5px;font-weight:700;color:var(--s-dark)}
.vsx-svc-link svg{width:15px;height:15px;transition:transform .25s var(--ease)}
.vsx-svc:hover .vsx-svc-link svg{transform:translateX(4px)}
.vsx-also{margin:46px auto 0;max-width:900px;text-align:center}
.vsx-also p{font-size:15px;color:var(--muted);margin-bottom:14px}
.vsx-also ul{display:flex;flex-wrap:wrap;justify-content:center;gap:10px}
.vsx-also a{display:inline-flex;align-items:center;gap:8px;padding:9px 16px;border-radius:999px;
  background:#fff;border:1px solid var(--border);font-size:14px;font-weight:600;color:var(--ink);
  transition:border-color .2s,transform .2s var(--ease),box-shadow .2s}
.vsx-also a:hover{border-color:var(--s);transform:translateY(-2px);box-shadow:var(--sh-m)}
.vsx-also a::after{content:'→';color:var(--s-dark)}

/* ---------- cifras ---------- */
.vsx-dark{background:var(--ink);color:#fff;padding:92px 24px;position:relative;isolation:isolate;overflow:hidden}
.vsx-dark::before{content:'';position:absolute;inset:0;z-index:-1;
  background:radial-gradient(640px 360px at 15% 0%,rgba(var(--s-rgb),.30),transparent 68%),
             radial-gradient(520px 320px at 90% 100%,rgba(var(--s-rgb),.20),transparent 68%)}
.vsx-dark .vsx-head h2{color:#fff}
.vsx-dark .vsx-head p{color:rgba(255,255,255,.66)}
.vsx-dark .vsx-eyebrow{color:var(--s-light)}
.vsx-stat{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.11);border-radius:var(--r);
  padding:30px 22px;text-align:center;transition:transform .28s var(--ease),background .28s,border-color .28s}
.vsx-stat:hover{transform:translateY(-5px);background:rgba(255,255,255,.08);border-color:rgba(var(--s-rgb),.55)}
.vsx-stat-t{display:inline-block;margin:0 0 16px;padding:5px 11px;border-radius:999px;font-family:'Manrope',sans-serif;
  font-size:11px;font-weight:800;letter-spacing:.09em;text-transform:uppercase;background:rgba(var(--s-rgb),.24);color:#fff}
.vsx-stat-n{font-family:'Manrope',sans-serif;font-size:clamp(36px,4.3vw,48px);font-weight:800;line-height:1;
  letter-spacing:-.03em;font-variant-numeric:tabular-nums;
  background:linear-gradient(120deg,#fff,var(--s-light));-webkit-background-clip:text;background-clip:text;
  -webkit-text-fill-color:transparent;color:transparent}
.vsx-stat-u{font-size:.55em;margin-left:3px}
.vsx-stat-l{font-size:14.5px;color:rgba(255,255,255,.82);margin-top:14px}
.vsx-stat-s{font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;font-weight:600;
  color:rgba(255,255,255,.45);margin-top:12px}
.vsx-dark .vsx-src{max-width:900px;margin:44px auto 0;text-align:center;font-size:13px;color:rgba(255,255,255,.55)}
.vsx-dark .vsx-src a{color:rgba(255,255,255,.8);text-decoration:underline;text-underline-offset:3px}

/* ---------- un dia cualquiera ---------- */
.vsx-day{display:grid;grid-template-columns:.9fr 1.1fr;gap:56px;align-items:center}
.vsx-day-media{position:relative}
.vsx-day-media img{border-radius:var(--r-lg);box-shadow:var(--sh-l);aspect-ratio:4/5;object-fit:cover;width:100%}
.vsx-day-media figcaption{position:absolute;left:18px;bottom:18px;right:18px;padding:14px 16px;border-radius:14px;
  background:rgba(255,255,255,.92);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);
  font-size:13.5px;color:var(--ink);box-shadow:var(--sh-m)}
.vsx-tl{position:relative;display:grid;gap:18px}
.vsx-tl::before{content:'';position:absolute;left:23px;top:14px;bottom:14px;width:2px;
  background:linear-gradient(var(--s),var(--s-light))}
.vsx-tl li{position:relative;display:grid;grid-template-columns:48px 1fr;gap:18px;align-items:start}
.vsx-tl-i{position:relative;z-index:1;width:48px;height:48px;border-radius:50%;display:grid;place-items:center;
  background:#fff;border:2px solid var(--s);color:var(--s-dark);box-shadow:0 6px 16px -8px rgba(var(--s-rgb),.7)}
.vsx-tl-i svg{width:21px;height:21px}
.vsx-tl div{background:#fff;border:1px solid var(--border);border-radius:14px;padding:14px 18px;
  box-shadow:var(--sh-s);font-size:15px;transition:transform .25s var(--ease),box-shadow .25s}
.vsx-tl li:hover div{transform:translateX(4px);box-shadow:var(--sh-m)}
.vsx-tl b{color:var(--ink);font-family:'Manrope',sans-serif}
.vsx-note{margin-top:18px;font-size:13px;color:var(--muted);font-style:italic}

/* ---------- pasos ---------- */
.vsx-steps{display:grid;grid-template-columns:repeat(3,1fr);gap:26px;counter-reset:st}
.vsx-step{position:relative;background:#fff;border:1px solid var(--border);border-radius:var(--r);
  padding:34px 28px 30px;box-shadow:var(--sh-s);transition:transform .28s var(--ease),box-shadow .28s}
.vsx-step:hover{transform:translateY(-5px);box-shadow:var(--sh-m)}
.vsx-step::before{counter-increment:st;content:'0' counter(st);display:block;margin-bottom:16px;
  font-family:'Manrope',sans-serif;font-size:40px;font-weight:800;line-height:1;letter-spacing:-.04em;
  background:linear-gradient(120deg,var(--s),var(--s-light));-webkit-background-clip:text;background-clip:text;
  -webkit-text-fill-color:transparent;color:transparent}
.vsx-step h3{font-size:19px;margin:0 0 10px}
.vsx-step p{font-size:15.5px;color:var(--muted)}
.vsx-step strong{color:var(--ink)}

/* ---------- faq ---------- */
.vsx-faq{max-width:880px;margin:0 auto}
.vsx-faq details{background:#fff;border:1px solid var(--border);border-radius:14px;margin-bottom:14px;
  box-shadow:var(--sh-s);transition:box-shadow .25s,border-color .25s}
.vsx-faq details:hover,.vsx-faq details[open]{border-color:var(--s-light);box-shadow:var(--sh-m)}
.vsx-faq summary{display:flex;align-items:center;gap:16px;padding:21px 26px;cursor:pointer;list-style:none}
.vsx-faq summary::-webkit-details-marker{display:none}
.vsx-faq summary h3{flex:1;font-size:17px;line-height:1.4}
.vsx-faq summary i{flex:0 0 auto;width:28px;height:28px;border-radius:50%;display:grid;place-items:center;
  background:var(--s-soft);color:var(--s-dark);transition:transform .3s var(--ease),background .25s,color .25s}
.vsx-faq summary svg{width:14px;height:14px}
.vsx-faq details[open] summary i{transform:rotate(45deg);background:var(--s);color:#fff}
.vsx-faq .a{padding:0 26px 24px;font-size:15.5px}
.vsx-faq .a p+p{margin-top:12px}
.vsx-faq .a strong{color:var(--ink)}
.vsx-faq .a a{color:var(--s-dark);font-weight:600;text-decoration:underline;text-underline-offset:3px}

/* ---------- cierre ---------- */
.vsx-cta{max-width:var(--max);margin:0 auto;border-radius:var(--r-lg);padding:66px 48px;text-align:center;color:#fff;
  position:relative;isolation:isolate;overflow:hidden;background:linear-gradient(135deg,var(--s-dark),#2a0f1e 120%)}
.vsx-cta::before{content:'';position:absolute;inset:0;z-index:-1;
  background:radial-gradient(520px 300px at 85% -10%,rgba(255,255,255,.18),transparent 70%)}
.vsx-cta h2{color:#fff;font-size:clamp(27px,3.6vw,40px);margin:0 0 14px;text-wrap:balance}
.vsx-cta p{max-width:620px;margin:0 auto;color:rgba(255,255,255,.82);font-size:17.5px}
.vsx-cta .vsx-ctas{justify-content:center}
.vsx-cta small{display:block;margin-top:26px;font-size:14px;color:rgba(255,255,255,.66)}
.vsx-cta small a{color:#fff;font-weight:600}
.vsx-rel{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:10px}
.vsx-rel a{display:flex;align-items:center;gap:14px;padding:18px 20px;border-radius:16px;background:#fff;
  border:1px solid var(--border);box-shadow:var(--sh-s);font-family:'Manrope',sans-serif;font-weight:700;
  font-size:15px;color:var(--ink);transition:transform .25s var(--ease),box-shadow .25s,border-color .25s}
.vsx-rel a:hover{transform:translateY(-4px);box-shadow:var(--sh-m);border-color:var(--s-light)}
.vsx-rel i{width:40px;height:40px;flex:0 0 auto;border-radius:12px;display:grid;place-items:center;
  background:var(--s-soft);color:var(--s-dark)}
.vsx-rel svg{width:20px;height:20px}
.vsx-rel span{flex:1}
.vsx-rel a::after{content:'→';color:var(--s-dark)}

/* ---------- aparicion al hacer scroll ---------- */
.vsx.vsx-js .vsx-rv{opacity:0;transform:translateY(20px);transition:opacity .7s var(--ease),transform .7s var(--ease)}
.vsx.vsx-js .vsx-rv.vsx-in{opacity:1;transform:none}

/* ---------- responsive ---------- */
@media (max-width:1080px){
  .vsx-hero-grid,.vsx-day{grid-template-columns:1fr;gap:46px}
  .vsx-media{max-width:620px;width:100%;margin:0 auto}
  .vsx-day-media{max-width:460px;width:100%;margin:0 auto}
  .vsx-g4{grid-template-columns:repeat(2,1fr)}
}
@media (max-width:860px){
  .vsx-svcs,.vsx-steps,.vsx-rel{grid-template-columns:1fr}
  .vsx-sec,.vsx-dark{padding-top:70px;padding-bottom:70px}
  .vsx-cta{padding:52px 24px}
}
@media (max-width:560px){
  .vsx{font-size:16px}
  .vsx-sec,.vsx-hero,.vsx-dark{padding-left:18px;padding-right:18px}
  .vsx-g4{grid-template-columns:1fr}
  .vsx-ctas .vsx-btn{width:100%}
  .vsx-svc{padding:28px 22px 24px}
  .vsx-tl li{gap:12px}
  .vsx-faq summary{padding:18px}
  .vsx-faq .a{padding:0 18px 20px}
}
@media (prefers-reduced-motion:reduce){
  .vsx *,.vsx *::before,.vsx *::after{animation:none!important;transition-duration:.001ms!important}
  .vsx .vsx-rv{opacity:1!important;transform:none!important}
}
</style>
"""
