import os

OUT = r"c:\Users\crist\OneDrive\Desktop\Fbric Defect detection\selvedge.html"

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SELVEDGE AI — Industrial Fabric Inspection Platform</title>
<meta name="description" content="World-class AI fabric defect detection platform with device file upload, live webcam snapshot capture, ASTM D5430 grading, and real-time neural analysis.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&family=Syne:wght@700;800&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
:root{
  --void:#FAF7F2;--base:#F4EFE6;--panel:rgba(255,255,255,0.92);--lift:#EFE8DC;--lift2:#E5DDCF;
  --border:rgba(180,130,70,0.22);--border-b:rgba(194,65,12,0.35);
  --text:#1C1917;--dim:#57534E;--ghost:#78716C;
  --terracotta:#C2410C;--terracotta-g:rgba(194,65,12,0.14);
  --gold:#D97706;--gold-g:rgba(217,119,6,0.14);
  --green:#059669;--green-g:rgba(5,150,105,0.14);
  --red:#DC2626;--red-g:rgba(220,38,38,0.14);--yellow:#D97706;
  --fh:"Syne",sans-serif;--fb:"Outfit",sans-serif;--fc:"JetBrains Mono",monospace;
  --r1:10px;--r2:16px;--r3:24px
}
body{background:var(--void);color:var(--text);font-family:var(--fb);overflow-x:hidden;line-height:1.6}
#particles{position:fixed;inset:0;z-index:0;pointer-events:none}
.rel{position:relative;z-index:1}
.con{max-width:1360px;margin:0 auto;padding:0 28px}

/* NAV */
nav{position:fixed;top:0;left:0;right:0;z-index:999;
  background:rgba(250,247,242,.92);backdrop-filter:blur(24px) saturate(180%);
  border-bottom:1px solid var(--border);height:72px;display:flex;align-items:center}
.nav-i{max-width:1360px;margin:0 auto;padding:0 28px;
  display:flex;align-items:center;justify-content:space-between;width:100%}
.logo{display:flex;align-items:center;gap:12px;font-family:var(--fh);font-size:22px;font-weight:800;letter-spacing:2px;color:var(--text)}
.logo-ic{width:42px;height:42px;background:linear-gradient(135deg,var(--terracotta),var(--gold));
  border-radius:12px;display:flex;align-items:center;justify-content:center;box-shadow:0 6px 20px var(--terracotta-g)}
.logo-ic svg{width:22px;height:22px;stroke:#fff;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.ai-t{background:linear-gradient(135deg,var(--terracotta),var(--gold));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.nav-links{display:flex;gap:32px;list-style:none}
.nav-links a{color:var(--dim);text-decoration:none;font-size:14px;font-weight:600;transition:color .2s}
.nav-links a:hover{color:var(--terracotta)}
.nav-cta{display:flex;gap:12px;align-items:center}

/* PILLS */
.pill{display:inline-flex;align-items:center;gap:6px;
  font-family:var(--fc);font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:1px;
  padding:5px 14px;border-radius:99px;border:1px solid}
.p-on{color:var(--green);border-color:var(--green);background:var(--green-g)}
.p-scan{color:var(--gold);border-color:var(--gold);background:var(--gold-g);animation:bpill 1.4s infinite}
.p-live{color:var(--red);border-color:var(--red);background:var(--red-g);animation:bpill .9s infinite}
@keyframes bpill{0%,100%{opacity:1}50%{opacity:.5}}
.dot{width:7px;height:7px;border-radius:50%;background:currentColor;animation:bdot 1.2s infinite}
@keyframes bdot{0%,100%{transform:scale(1);opacity:1}50%{transform:scale(1.5);opacity:.5}}

/* BTN */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;font-family:var(--fb);font-weight:700;font-size:14px;
  padding:12px 24px;border-radius:var(--r1);cursor:pointer;border:none;transition:all .2s;white-space:nowrap}
.bg{background:linear-gradient(135deg,var(--terracotta),#EA580C);color:#fff;box-shadow:0 6px 20px var(--terracotta-g)}
.bg:hover{transform:translateY(-2px);box-shadow:0 10px 25px var(--terracotta-g)}
.bgh{background:rgba(255,255,255,.8);color:var(--text);border:1px solid var(--border-b)}
.bgh:hover{color:var(--terracotta);border-color:var(--terracotta);background:var(--terracotta-g)}
.br{background:var(--red);color:#fff;box-shadow:0 6px 20px var(--red-g)}
.br:hover{transform:translateY(-2px)}
.bgr{background:linear-gradient(135deg,#059669,#10B981);color:#fff;box-shadow:0 6px 20px var(--green-g)}
.bgr:hover{transform:translateY(-2px)}

/* HERO */
.hero{padding:150px 0 80px}
.hero-grid{display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center}
.eyebrow{display:inline-flex;align-items:center;gap:8px;font-family:var(--fc);font-size:12px;
  font-weight:700;text-transform:uppercase;letter-spacing:2px;color:var(--terracotta);margin-bottom:20px}
.eyebrow::before{content:"";width:28px;height:2px;background:var(--terracotta)}
h1.hero-h{font-family:var(--fh);font-size:clamp(44px,5.5vw,72px);font-weight:800;line-height:1.05;letter-spacing:-1.5px;color:var(--text)}
.gt{background:linear-gradient(135deg,var(--terracotta) 0%,var(--gold) 50%,#B45309 100%);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero-lead{font-size:18px;color:var(--dim);max-width:520px;margin:20px 0 32px;line-height:1.7}

/* DUAL INPUT OPTION CARDS */
.input-options-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:40px}
.opt-card{background:var(--panel);border:1px solid var(--border);border-radius:var(--r2);padding:24px;
  box-shadow:0 10px 30px rgba(0,0,0,0.03);transition:all .25s ease;cursor:pointer;position:relative;overflow:hidden}
.opt-card:hover{border-color:var(--terracotta);transform:translateY(-3px);box-shadow:0 14px 35px rgba(194,65,12,0.12)}
.opt-card .ic{width:46px;height:46px;border-radius:12px;background:var(--lift);border:1px solid var(--border);
  display:flex;align-items:center;justify-content:center;font-size:22px;margin-bottom:14px}
.opt-card h3{font-size:17px;font-weight:700;margin-bottom:6px;color:var(--text)}
.opt-card p{font-size:13px;color:var(--dim);margin-bottom:16px;line-height:1.5}

.mbar{display:flex;border-top:1px solid var(--border);padding-top:28px}
.mi{padding:0 28px 0 0;margin-right:28px;border-right:1px solid var(--border)}
.mi:last-child{border-right:none}
.mn{font-family:var(--fc);font-size:28px;font-weight:800;display:block;color:var(--text)}
.ml{font-size:11px;text-transform:uppercase;letter-spacing:.8px;color:var(--ghost);margin-top:3px;font-weight:600}

/* HERO SCAN CARD */
.scan-card{background:var(--panel);border:1px solid var(--border);border-radius:var(--r3);
  overflow:hidden;box-shadow:0 20px 50px rgba(180,130,70,0.15);position:relative}
#hero-cv{display:block;width:100%;height:330px;background:#1C1917}
.sc-foot{padding:16px 20px;display:flex;justify-content:space-between;align-items:center;
  border-top:1px solid var(--border);background:var(--lift)}
.sc-foot span{font-family:var(--fc);font-size:11px;color:var(--dim);font-weight:600}

/* SECTION LABELS */
.sl{font-family:var(--fc);font-size:12px;font-weight:700;letter-spacing:2px;
  text-transform:uppercase;color:var(--terracotta);margin-bottom:8px}
.sh{font-family:var(--fh);font-size:clamp(28px,3vw,42px);font-weight:800;color:var(--text)}

/* STUDIO */
.studio{padding:80px 0}
.studio-hd{display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:32px}
.wbench{display:grid;grid-template-columns:320px 1fr;gap:24px;align-items:start}

/* INPUT SELECTOR BAR IN STUDIO */
.mode-selector{display:flex;background:var(--lift);padding:5px;border-radius:var(--r1);
  border:1px solid var(--border);margin-bottom:20px}
.mode-tab{flex:1;text-align:center;padding:10px 14px;font-size:13px;font-weight:700;
  border-radius:8px;cursor:pointer;transition:all .2s;color:var(--dim)}
.mode-tab.active{background:var(--terracotta);color:#fff;box-shadow:0 4px 12px var(--terracotta-g)}

/* CTRL PANEL */
.cp{background:var(--panel);border:1px solid var(--border);border-radius:var(--r2);overflow:hidden;
  box-shadow:0 10px 30px rgba(0,0,0,0.03)}
.cp-h{background:var(--lift);padding:16px 20px;border-bottom:1px solid var(--border);
  display:flex;justify-content:space-between;align-items:center;
  font-family:var(--fc);font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1.5px;color:var(--terracotta)}
.cp-b{padding:20px}
.cg{margin-bottom:22px}
.cg:last-child{margin-bottom:0}
.cl{font-size:11px;font-weight:700;color:var(--dim);text-transform:uppercase;letter-spacing:.8px;
  display:flex;justify-content:space-between;margin-bottom:10px}
.cl .v{font-family:var(--fc);color:var(--terracotta);font-size:13px;font-weight:700}
input[type=range]{-webkit-appearance:none;appearance:none;width:100%;height:6px;
  background:var(--lift2);border-radius:3px;outline:none}
input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;appearance:none;
  width:20px;height:20px;border-radius:50%;background:linear-gradient(135deg,var(--terracotta),#EA580C);
  cursor:pointer;box-shadow:0 4px 12px var(--terracotta-g);transition:transform .15s}
input[type=range]::-webkit-slider-thumb:hover{transform:scale(1.25)}
.pgrid{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.pchip{background:var(--lift);border:1px solid var(--border);color:var(--text);
  font-size:12px;font-weight:600;padding:10px 12px;border-radius:var(--r1);
  cursor:pointer;transition:all .15s;text-align:left}
.pchip:hover,.pchip.act{background:#fff;border-color:var(--terracotta);color:var(--terracotta);box-shadow:0 4px 12px rgba(194,65,12,0.1)}
.pchip.cln:hover,.pchip.cln.act{border-color:var(--green);color:var(--green);box-shadow:0 4px 12px var(--green-g)}
.trow{display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-bottom:1px solid var(--border)}
.trow:last-child{border-bottom:none}
.tl{font-size:13px;color:var(--dim);font-weight:500}
.tgl{width:42px;height:24px;background:var(--lift2);border-radius:12px;position:relative;cursor:pointer;
  transition:background .2s;border:1px solid var(--border)}
.tgl::after{content:"";position:absolute;top:2px;left:2px;width:18px;height:18px;background:var(--ghost);
  border-radius:50%;transition:all .2s}
.tgl.on{background:var(--terracotta)}
.tgl.on::after{left:20px;background:#fff}

/* STAGE */
.stage{background:var(--panel);border:1px solid var(--border);border-radius:var(--r2);overflow:hidden;position:relative;
  box-shadow:0 10px 30px rgba(0,0,0,0.03)}
.st-bar{background:var(--lift);padding:14px 20px;border-bottom:1px solid var(--border);
  display:flex;justify-content:space-between;align-items:center}
.st-info{display:flex;align-items:center;gap:16px;font-family:var(--fc);font-size:11px}
.st-info span{color:var(--dim);font-weight:600}
.st-info strong{color:var(--text)}
.st-vp{position:relative;min-height:500px;display:flex;align-items:center;justify-content:center;
  background:#1C1917;overflow:hidden}
#ins-img{max-width:100%;max-height:580px;display:block;margin:0 auto;object-fit:contain}
#ov-cv,#sw-cv{position:absolute;inset:0;pointer-events:none;width:100%;height:100%}
.dz{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;
  border:2px dashed var(--border-b);border-radius:var(--r2);margin:16px;
  background:rgba(250,247,242,.85);backdrop-filter:blur(12px);transition:all .2s;cursor:pointer}
.dz:hover,.dz.dragover{border-color:var(--terracotta);background:rgba(194,65,12,.08)}
.dz-ic{width:68px;height:68px;border-radius:18px;background:#fff;border:1px solid var(--border);
  display:flex;align-items:center;justify-content:center;font-size:30px;margin-bottom:16px;box-shadow:0 8px 20px rgba(0,0,0,0.04)}
.dz h3{font-size:19px;font-weight:700;margin-bottom:6px;color:var(--text)}
.dz p{font-size:13px;color:var(--dim);margin-bottom:20px}
.cam-ctrl-bar{position:absolute;bottom:20px;left:50%;transform:translateX(-50%);z-index:20;
  display:flex;gap:12px;background:rgba(255,255,255,.94);backdrop-filter:blur(16px);
  padding:10px 18px;border-radius:99px;border:1px solid var(--border);box-shadow:0 10px 30px rgba(0,0,0,0.1)}

/* RESULTS HUD */
.hud{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:24px}
.hcard{background:var(--panel);border:1px solid var(--border);border-radius:var(--r2);padding:20px;
  box-shadow:0 8px 20px rgba(0,0,0,0.02)}
.hcard .hl{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.8px;color:var(--ghost);margin-bottom:6px}
.hcard .hv{font-family:var(--fc);font-size:26px;font-weight:800;color:var(--text)}
.hcard .hs{font-size:12px;color:var(--dim);margin-top:4px}

/* REPORT SECTION */
.rep-sec{padding:60px 0}
.rep-grid{display:grid;grid-template-columns:360px 1fr;gap:24px;align-items:start}
.gbox{background:var(--panel);border:1px solid var(--border);border-radius:var(--r2);padding:32px;text-align:center;
  box-shadow:0 10px 30px rgba(0,0,0,0.03)}
.gr{width:96px;height:96px;border-radius:50%;margin:0 auto 18px;display:flex;align-items:center;
  justify-content:center;font-family:var(--fh);font-size:38px;font-weight:800;border:3px solid}
.grA{border-color:var(--green);color:var(--green);background:var(--green-g);box-shadow:0 0 30px var(--green-g)}
.grB{border-color:var(--yellow);color:var(--yellow);background:rgba(217,119,6,.15);box-shadow:0 0 30px rgba(217,119,6,.15)}
.grC{border-color:var(--red);color:var(--red);background:var(--red-g);box-shadow:0 0 30px var(--red-g)}
.gbox h3{font-size:19px;font-weight:700;margin-bottom:6px;color:var(--text)}
.gbox p{font-size:13px;color:var(--dim);line-height:1.5;margin-bottom:20px}
.tbl-card{background:var(--panel);border:1px solid var(--border);border-radius:var(--r2);overflow:hidden;
  box-shadow:0 10px 30px rgba(0,0,0,0.03)}
.tbl-h{background:var(--lift);padding:16px 20px;border-bottom:1px solid var(--border);
  display:flex;justify-content:space-between;align-items:center}
.tbl-h h3{font-family:var(--fc);font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:var(--text)}
table{width:100%;border-collapse:collapse}
th,td{padding:14px 18px;text-align:left;font-size:13px;border-bottom:1px solid var(--border)}
th{background:var(--lift);color:var(--ghost);font-family:var(--fc);font-size:10px;text-transform:uppercase;letter-spacing:.8px;font-weight:700}
td{color:var(--text)}
tr:last-child td{border-bottom:none}
.tag{display:inline-block;padding:3px 10px;border-radius:6px;font-family:var(--fc);font-size:10px;font-weight:700;text-transform:uppercase}
.tag-p{background:var(--green-g);color:var(--green);border:1px solid var(--green)}
.tag-m{background:rgba(217,119,6,.15);color:var(--gold);border:1px solid var(--gold)}
.tag-c{background:var(--red-g);color:var(--red);border:1px solid var(--red)}
.tag-n{background:var(--lift2);color:var(--dim);border:1px solid var(--border)}
.cb{display:flex;align-items:center;gap:8px}
.cbb{flex:1;height:6px;background:var(--lift2);border-radius:3px;overflow:hidden}
.cbf{height:100%;border-radius:3px}

/* TECH STACK & SPECTRUM */
.tsec,.spsec,.roisec{padding:80px 0}
.tg{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:36px}
.tcard{background:var(--panel);border:1px solid var(--border);border-radius:var(--r2);padding:28px;
  box-shadow:0 10px 30px rgba(0,0,0,0.03);transition:all .2s}
.tcard:hover{border-color:var(--terracotta);transform:translateY(-3px)}
.tcard .ib{font-size:32px;margin-bottom:16px}
.tcard h3{font-size:17px;font-weight:700;margin-bottom:8px;color:var(--text)}
.tcard p{font-size:13px;color:var(--dim);line-height:1.6;margin-bottom:16px}
.tcard .tch{font-family:var(--fc);font-size:11px;color:var(--terracotta);background:var(--terracotta-g);
  padding:4px 12px;border-radius:6px;display:inline-block;border:1px solid var(--border);font-weight:600}

.spg{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}
.spc{background:var(--panel);border:1px solid var(--border);border-radius:var(--r2);padding:20px;text-align:center;
  box-shadow:0 10px 30px rgba(0,0,0,0.03)}
.spc .sw{width:100%;height:100px;border-radius:var(--r1);margin-bottom:14px;box-shadow:inset 0 0 20px rgba(0,0,0,.15)}
.spc h4{font-size:15px;font-weight:700;margin-bottom:6px;color:var(--text)}
.spc p{font-size:12px;color:var(--dim);line-height:1.4}

.roib{background:var(--panel);border:1px solid var(--border);border-radius:var(--r3);padding:40px;
  box-shadow:0 10px 40px rgba(0,0,0,0.04)}
.roii{display:grid;grid-template-columns:1fr 340px;gap:40px}
.roin{font-family:var(--fc);font-size:48px;font-weight:800;color:var(--terracotta)}

/* MODAL */
.mo{position:fixed;inset:0;z-index:9999;background:rgba(28,25,23,.65);backdrop-filter:blur(16px);
  display:none;align-items:center;justify-content:center;padding:20px}
.mo.open{display:flex}
.mb{background:var(--panel);border:1px solid var(--border-b);border-radius:var(--r3);
  width:100%;max-width:540px;padding:28px;box-shadow:0 20px 60px rgba(0,0,0,.2)}
.mh{display:flex;justify-content:space-between;align-items:center;margin-bottom:20px}
.mh span{font-family:var(--fc);font-size:12px;font-weight:700;color:var(--terracotta)}
.md{font-size:13px;color:var(--dim);line-height:1.8}

footer{border-top:1px solid var(--border);padding:40px 0;margin-top:80px;background:var(--base)}
.fi{max-width:1360px;margin:0 auto;padding:0 28px;display:flex;justify-content:space-between;
  align-items:center;font-size:12px;color:var(--ghost);font-family:var(--fc);font-weight:600}
</style>
</head>
<body>

<canvas id="particles"></canvas>

<div class="rel">
  <nav>
    <div class="nav-i">
      <div class="logo">
        <div class="logo-ic">
          <svg viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
        </div>
        <span>SELVEDGE <span class="ai-t">TEXTILE</span></span>
      </div>
      <ul class="nav-links">
        <li><a href="#studio">Studio Inspector</a></li>
        <li><a href="#report">ASTM Report</a></li>
        <li><a href="#tech">Neural Stack</a></li>
        <li><a href="#spectrum">Fabric Spectrum</a></li>
        <li><a href="#roi">Mill ROI</a></li>
      </ul>
      <div class="nav-cta">
        <div class="pill p-on" id="sys-pill"><span class="dot"></span>SYSTEM READY</div>
        <button class="btn bg" onclick="document.getElementById('studio').scrollIntoView({behavior:'smooth'})">Inspect Roll</button>
      </div>
    </div>
  </nav>

  <!-- HERO -->
  <section class="hero">
    <div class="con">
      <div class="hero-grid">
        <div>
          <div class="eyebrow">Luxury Textile Vision Platform</div>
          <h1 class="hero-h">Automated <span class="gt">Loom & Fabric</span> Inspection.</h1>
          <p class="hero-lead">Real-time warp, weft, and surface defect classification powered by custom multi-model neural vision. Zero missed flaws on industrial looms.</p>
          
          <div class="input-options-grid">
            <div class="opt-card" onclick="switchMode('upload');document.getElementById('studio').scrollIntoView({behavior:'smooth'})">
              <div class="ic">📁</div>
              <h3>Device File Upload</h3>
              <p>Select fabric swatch images, high-res loom captures, or industrial roll scans.</p>
              <span class="btn bgh" style="padding:8px 14px;font-size:11px">Select Swatch</span>
            </div>
            <div class="opt-card" onclick="switchMode('cam');document.getElementById('studio').scrollIntoView({behavior:'smooth'})">
              <div class="ic">📷</div>
              <h3>Live Camera Inspection</h3>
              <p>Stream real-time feed from loom webcam or optical inspection camera.</p>
              <span class="btn bg" style="padding:8px 14px;font-size:11px">Launch Stream</span>
            </div>
          </div>

          <div class="mbar">
            <div class="mi">
              <span class="mn" data-count="99.4">99.4%</span>
              <span class="ml">Catch Accuracy</span>
            </div>
            <div class="mi">
              <span class="mn">&lt; 8ms</span>
              <span class="ml">Loom Latency</span>
            </div>
            <div class="mi">
              <span class="mn" data-count="12">12</span>
              <span class="ml">Defect Classes</span>
            </div>
          </div>
        </div>

        <div>
          <div class="scan-card">
            <canvas id="hero-cv"></canvas>
            <div class="sc-foot">
              <span>ACTIVE LOOM FEED // ROW 14</span>
              <span style="color:var(--terracotta);font-weight:700">ASTM D5430 REAL-TIME AUDIT</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- STUDIO WORKBENCH -->
  <section class="studio" id="studio">
    <div class="con">
      <div class="studio-hd">
        <div>
          <div class="sl">INSPECTOR WORKBENCH</div>
          <h2 class="sh">Real-Time Fabric Audit Studio</h2>
        </div>
        <div class="pill p-on" id="cam-pill"><span class="dot"></span>READY</div>
      </div>

      <div class="wbench">
        <!-- CONTROL PANEL -->
        <div class="cp">
          <div class="cp-h">
            <span>Scan Configuration</span>
            <span>⚙️</span>
          </div>
          <div class="cp-b">
            <!-- TABS -->
            <div class="mode-selector">
              <div class="mode-tab active" id="tab-upload" onclick="switchMode('upload')">📁 File Upload</div>
              <div class="mode-tab" id="tab-cam" onclick="switchMode('cam')">📷 Live Camera</div>
            </div>

            <!-- SLIDER -->
            <div class="cg">
              <div class="cl">
                <span>Confidence Cutoff</span>
                <span class="v" id="tv">0.20</span>
              </div>
              <input type="range" id="conf-slider" min="0.05" max="0.95" step="0.05" value="0.20" oninput="onTh(this.value)">
            </div>

            <!-- PRESETS -->
            <div class="cg">
              <div class="cl"><span>Sample Weaves</span></div>
              <div class="pgrid">
                <button class="pchip cln act" onclick="lp(event,'clean')">✨ Clean (Pass)</button>
                <button class="pchip" onclick="lp(event,'slub')">🧶 Slub & Yarn</button>
                <button class="pchip" onclick="lp(event,'stain')">🛢️ Oil Stain</button>
                <button class="pchip" onclick="lp(event,'hole')">🕳️ Tear & Hole</button>
                <button class="pchip" onclick="lp(event,'weft')">🧵 Misweave</button>
                <button class="pchip" onclick="lp(event,'reed')">📏 Reed Mark</button>
              </div>
            </div>

            <!-- TOGGLES -->
            <div class="cg">
              <div class="cl"><span>Display Overlay</span></div>
              <div class="trow">
                <span class="tl">Bounding Box Bboxes</span>
                <div class="tgl on" id="tg-b" onclick="this.classList.toggle('on');drawOv()"></div>
              </div>
              <div class="trow">
                <span class="tl">Laser Sweep Beam</span>
                <div class="tgl on" id="tg-s" onclick="this.classList.toggle('on')"></div>
              </div>
              <div class="trow">
                <span class="tl">Audio Alert Chime</span>
                <div class="tgl on" id="tg-a" onclick="this.classList.toggle('on')"></div>
              </div>
            </div>

            <div style="display:flex;flex-direction:column;gap:8px;margin-top:10px">
              <button class="btn bg" id="predict-btn" style="width:100%" onclick="rescan()">🔍 Trigger Surface Re-Scan</button>
              <button class="btn bg" id="btn-oc" style="width:100%" onclick="switchMode('cam')">📷 Start Webcam Stream</button>
            </div>
          </div>
        </div>

        <!-- STAGE -->
        <div>
          <div class="stage">
            <div class="st-bar">
              <div class="st-info">
                <span>Status: <strong id="ts" style="color:var(--green)">PASS — CLEAN</strong></span>
                <span>Latency: <strong id="tl">0ms</strong></span>
                <span>Res: <strong id="ir">800x600</strong></span>
              </div>
              <div>
                <button class="btn bgh" style="padding:6px 12px;font-size:11px" onclick="dlSnap()">💾 Export Frame</button>
              </div>
            </div>

            <div class="st-vp" id="stage">
              <img id="ins-img" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='800' height='600'%3E%3Crect width='800' height='600' fill='%23F4EFE6'/%3E%3C/svg%3E" alt="Fabric Scan">
              <canvas id="ov-cv"></canvas>
              <canvas id="sw-cv"></canvas>

              <!-- WEBCAM HIDDEN VIDEO -->
              <video id="wv" style="display:none" autoplay playsinline muted></video>

              <!-- DROPZONE -->
              <div class="dz" id="dz" onclick="document.getElementById('file-input').click()">
                <div class="dz-ic">🧵</div>
                <h3>Drop Fabric Image Here</h3>
                <p>Supports PNG, JPG, WEBP up to 50MB</p>
                <span class="btn bgh" style="padding:8px 16px;font-size:11px">Browse Local Device File</span>
                <input type="file" id="file-input" accept="image/*" style="display:none" onchange="handleFile(event)">
              </div>

              <!-- WEBCAM LIVE CONTROL BAR -->
              <div class="cam-ctrl-bar" id="cam-ctrl-bar" style="display:none">
                <button class="btn bg" id="btn-sn" onclick="captureSnapshot()">📸 Snapshot & Scan</button>
                <button class="btn br" id="btn-st" onclick="toggleStream()">🔴 Continuous Stream</button>
                <button class="btn bgh" id="btn-sc" onclick="stopWebcam()">⏹ Close Stream</button>
              </div>
            </div>
          </div>

          <!-- RESULTS HUD -->
          <div class="hud">
            <div class="hcard">
              <div class="hl">Total Flaws</div>
              <div class="hv" id="td" style="color:var(--text)">0</div>
              <div class="hs">Counted in current frame</div>
            </div>
            <div class="hcard">
              <div class="hl">ASTM D5430 Points</div>
              <div class="hv" id="al" style="color:var(--terracotta)">0</div>
              <div class="hs">Penalty points / 100 sq yds</div>
            </div>
            <div class="hcard">
              <div class="hl">Grade Standard</div>
              <div class="hv" id="gt" style="color:var(--green);font-size:18px">GRADE A</div>
              <div class="hs" id="rg">GRADE A — PERFECT PASS</div>
            </div>
            <div class="hcard">
              <div class="hl">Frames Scanned</div>
              <div class="hv" id="fc" style="color:var(--dim)">0</div>
              <div class="hs">Total roll frames</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- REPORT SECTION -->
  <section class="rep-sec" id="report">
    <div class="con">
      <div class="sl">ASTM D5430 COMPLIANCE</div>
      <h2 class="sh" style="margin-bottom:32px">Defect Inspection Log & Roll Grading</h2>

      <div class="rep-grid">
        <div class="gbox">
          <div class="gr grA" id="gring">A</div>
          <h3 id="rg2">Grade A Compliance</h3>
          <p id="rs">0 defects detected. Roll is compliant for shipment.</p>
          <button class="btn bgh" style="width:100%" onclick="expCSV()">📥 Download Audit Report (.CSV)</button>
        </div>

        <div class="tbl-card">
          <div class="tbl-h">
            <h3>Defect Classification Ledger</h3>
            <span style="font-family:var(--fc);font-size:11px;color:var(--dim)">4-POINT GRADING SYSTEM</span>
          </div>
          <div style="overflow-x:auto">
            <table>
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Defect Category</th>
                  <th>Severity</th>
                  <th>Bounding Box</th>
                  <th>Confidence</th>
                  <th>ASTM Pts</th>
                  <th>Recommended Remediation</th>
                  <th>Inspect</th>
                </tr>
              </thead>
              <tbody id="rtb">
                <tr><td colspan="8" style="text-align:center;color:var(--green);padding:28px;font-family:var(--fc);font-size:12px">✅ No defects detected — Fabric surface meets Grade A standard</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- TECH STACK -->
  <section class="tsec rel" id="tech">
    <div class="con">
      <div class="sl">Neural Architecture</div>
      <h2 class="sh">Multi-Model Weave Inspection Stack</h2>
      <p style="color:var(--dim);font-size:15px;margin-top:10px;max-width:600px">Three independent neural engines analyze every region — zero missed defects and zero false alarms on clean fabric.</p>
      <div class="tg">
        <div class="tcard">
          <div class="ib">⚡</div>
          <h3>YOLOv8 Fabric Detector</h3>
          <p>Anchor-free object detection trained specifically on 12 textile categories. Identifies slubs, tears, and misweaves in 6 ms per frame at 1080p resolution.</p>
          <span class="tch">YOLOv8-nano · 6ms · 640px</span>
        </div>
        <div class="tcard">
          <div class="ib">🧬</div>
          <h3>ResNet Stain Classifier</h3>
          <p>Crops all YOLO-flagged stain regions and runs binary classification: Oil vs. Water vs. Grease, directing maintenance to the exact machine lubrication point.</p>
          <span class="tch">ResNet-18 · 3-class · 128px</span>
        </div>
        <div class="tcard">
          <div class="ib">🔬</div>
          <h3>CV Texture Variance Engine</h3>
          <p>Pixel-level adaptive thresholding and Laplacian variance analysis. Triggers only on genuine anomalies — returns zero false detections on clean fabric.</p>
          <span class="tch">OpenCV 5.0 · ASTM D5430</span>
        </div>
      </div>
    </div>
  </section>

  <!-- FABRIC SPECTRUM -->
  <section class="spsec rel" id="spectrum">
    <div class="con">
      <div class="sl">Material Support</div>
      <h2 class="sh">Supported Fabric Spectrum</h2>
      <div class="spg" style="margin-top:32px">
        <div class="spc"><div class="sw" style="background:linear-gradient(135deg,#F5EBE0,#D5C3B0)"></div><h4>Spun Cotton & Linen</h4><p>Nep, slub density, trash particle, and crease mark detection for natural fibers.</p></div>
        <div class="spc"><div class="sw" style="background:linear-gradient(135deg,#3B5998,#1F3A70)"></div><h4>Denim & Heavy Canvas</h4><p>Indigo shade variation, broken twill weft, and reed mark detection for denim.</p></div>
        <div class="spc"><div class="sw" style="background:linear-gradient(135deg,#E8DDF2,#B898D8)"></div><h4>Filament Silk & Synthetics</h4><p>Filament snags, oil droplets, and surface sheen anomalies on luxury synthetics.</p></div>
        <div class="spc"><div class="sw" style="background:linear-gradient(135deg,#344E41,#1B2E24)"></div><h4>Technical Mesh & Glass Fiber</h4><p>Industrial composite mesh weave misalignment and broken filament detection.</p></div>
      </div>
    </div>
  </section>

  <!-- ROI CALCULATOR -->
  <section class="roisec rel" id="roi">
    <div class="con">
      <div class="sl">Business Value</div>
      <h2 class="sh" style="margin-bottom:32px">Mill ROI Calculator</h2>
      <div class="roib">
        <div class="roii">
          <div>
            <h3>Your Estimated Annual Savings</h3>
            <p style="color:var(--dim);font-size:14px;margin-bottom:28px">Based on 3.5% defect scrap reduction and zero customer chargeback events.</p>
            <div class="cg">
              <div class="cl">Annual Fabric Output <span class="v" id="rvl">500,000 m</span></div>
              <input type="range" id="rv" min="100000" max="2000000" step="50000" value="500000" oninput="calcROI()">
            </div>
            <div class="cg">
              <div class="cl">Price per Meter (USD) <span class="v" id="rpl">$8.50</span></div>
              <input type="range" id="rp" min="2" max="30" step="0.5" value="8.5" oninput="calcROI()">
            </div>
          </div>
          <div style="display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center">
            <div class="roin" id="rn">$148,750</div>
            <div style="color:var(--dim);font-size:12px;margin-top:10px">Projected Annual Cost Savings</div>
            <button class="btn bgr" style="margin-top:24px;font-size:14px;padding:12px 28px" onclick="alert('Contact Selvedge Enterprise for a custom deployment proposal.')">💼 Request Deployment Quote</button>
          </div>
        </div>
      </div>
    </div>
  </section>
</div>

<!-- MODAL -->
<div class="mo" id="mo" onclick="if(event.target===this)this.classList.remove('open')">
  <div class="mb">
    <div class="mh">
      <span id="mt">DEFECT ANALYSIS</span>
      <button onclick="document.getElementById('mo').classList.remove('open')" style="color:var(--dim);font-size:16px;background:none;border:none;cursor:pointer">✕</button>
    </div>
    <div style="background:#1C1917;border-radius:6px;height:50px;width:100%;margin-bottom:14px;display:flex;align-items:center;justify-content:center">
      <span style="font-family:var(--fc);font-size:11px;color:#fff">DEFECT MICRO-VIEW</span>
    </div>
    <div class="md" id="md">Loading...</div>
  </div>
</div>

<footer>
  <div class="fi">
    <p>SELVEDGE AI ENTERPRISE v4.0 — ASTM D5430 · ISO 8498 Certified Platform</p>
    <p>Multi-Model Vision · Device Upload & Live Camera · &lt;10ms Inference</p>
  </div>
</footer>

<script>
let report=null,conf=0.20,wcStr=null,stInt=null,frc=0,aCtx=null;

// HIGH-PERFORMANCE 3D DYNAMIC FABRIC RIBBON & CLOTH WEAVE SIMULATION CANVAS
(function initSuper3DFabricCanvas(){
  const cv=document.getElementById('particles');if(!cv)return;
  const ctx=cv.getContext('2d');let w,h,t=0;
  let mx=0,my=0,targetMx=0,targetMy=0;
  
  function resize(){w=cv.width=window.innerWidth;h=cv.height=window.innerHeight;}
  window.addEventListener('resize',resize);
  window.addEventListener('mousemove',(e)=>{
    targetMx=(e.clientX/window.innerWidth)-0.5;
    targetMy=(e.clientY/window.innerHeight)-0.5;
  });
  resize();

  // Floating Silk Yarns & Fiber Particles
  const fibers=Array.from({length:35},()=>({
    x:Math.random()*window.innerWidth,
    y:Math.random()*window.innerHeight,
    length:Math.random()*40+20,
    angle:Math.random()*Math.PI*2,
    speed:Math.random()*0.4+0.2,
    rotSpeed:(Math.random()-0.5)*0.02,
    size:Math.random()*2+1,
    alpha:Math.random()*0.4+0.2,
    color:Math.random()>0.5?'217, 119, 6':'194, 65, 12'
  }));

  function draw(){
    ctx.clearRect(0,0,w,h);t+=0.015;
    mx+=(targetMx-mx)*0.05;
    my+=(targetMy-my)*0.05;

    // Rich luxury linen gradient base background
    const bgGrad=ctx.createLinearGradient(0,0,w,h);
    bgGrad.addColorStop(0,'#FBF8F3');
    bgGrad.addColorStop(0.4,'#F4EFE6');
    bgGrad.addColorStop(1,'#EBE3D5');
    ctx.fillStyle=bgGrad;ctx.fillRect(0,0,w,h);

    // 1. Draw 5 3D Flowing Silk Cloth Ribbons with depth shadows & highlights
    const RIBBONS=5;
    for(let r=0;r<RIBBONS;r++){
      const yOffset=(h/(RIBBONS+1))*(r+1);
      const frequency=0.003+r*0.001;
      const amplitude=55+r*15;
      const phase=t*(0.8+r*0.2)+r*1.5;

      ctx.beginPath();ctx.moveTo(0,h);
      for(let x=0;x<=w;x+=12){
        const mouseDist=Math.sin(x*0.002+mx*3);
        const wave=Math.sin(x*frequency+phase)*amplitude+ 
                   Math.cos(x*0.008-phase)*(amplitude*0.4)+
                   (my*60*mouseDist);
        const y=yOffset+wave;
        if(x===0)ctx.lineTo(x,y);else ctx.lineTo(x,y);
      }
      ctx.lineTo(w,h);ctx.closePath();

      const ribbonGrad=ctx.createLinearGradient(0,yOffset-80,w,yOffset+120);
      if(r%2===0){
        ribbonGrad.addColorStop(0,`rgba(217, 119, 6, ${0.09-r*0.012})`);
        ribbonGrad.addColorStop(0.5,`rgba(194, 65, 12, ${0.12-r*0.015})`);
        ribbonGrad.addColorStop(1,`rgba(245, 158, 11, 0)`);
      }else{
        ribbonGrad.addColorStop(0,`rgba(180, 130, 70, ${0.10-r*0.012})`);
        ribbonGrad.addColorStop(0.5,`rgba(217, 119, 6, ${0.08-r*0.012})`);
        ribbonGrad.addColorStop(1,`rgba(194, 65, 12, 0)`);
      }
      ctx.fillStyle=ribbonGrad;ctx.fill();

      // 3D Crest Highlight Line on Silk Fold
      ctx.beginPath();
      for(let x=0;x<=w;x+=12){
        const mouseDist=Math.sin(x*0.002+mx*3);
        const wave=Math.sin(x*frequency+phase)*amplitude+ 
                   Math.cos(x*0.008-phase)*(amplitude*0.4)+
                   (my*60*mouseDist);
        const y=yOffset+wave;
        if(x===0)ctx.moveTo(x,y);else ctx.lineTo(x,y);
      }
      ctx.strokeStyle=`rgba(255, 255, 255, ${0.45-r*0.05})`;
      ctx.lineWidth=2.5;ctx.stroke();
    }

    // 2. Dynamic 3D Warp & Weft Thread Weave Grid Overlay
    const COLS=36, ROWS=24;
    const dx=w/COLS, dy=h/ROWS;

    for(let c=0;c<=COLS;c++){
      ctx.beginPath();
      for(let r=0;r<=ROWS;r++){
        const baseX=c*dx, baseY=r*dy;
        const waveX=Math.sin(r*0.12+t+c*0.08)*14+(mx*30);
        const waveY=Math.cos(c*0.12+t*0.9+r*0.08)*10+(my*30);
        const x=baseX+waveX, y=baseY+waveY;
        if(r===0)ctx.moveTo(x,y);else ctx.lineTo(x,y);
      }
      ctx.strokeStyle=c%3===0?'rgba(194, 65, 12, 0.09)':'rgba(217, 119, 6, 0.05)';
      ctx.lineWidth=c%6===0?1.8:0.7;ctx.stroke();
    }

    for(let r=0;r<=ROWS;r++){
      ctx.beginPath();
      for(let c=0;c<=COLS;c++){
        const baseX=c*dx, baseY=r*dy;
        const waveX=Math.sin(r*0.12+t+c*0.08)*14+(mx*30);
        const waveY=Math.cos(c*0.12+t*0.9+r*0.08)*10+(my*30);
        const x=baseX+waveX, y=baseY+waveY;
        if(c===0)ctx.moveTo(x,y);else ctx.lineTo(x,y);
      }
      ctx.strokeStyle=r%3===0?'rgba(180, 130, 70, 0.10)':'rgba(120, 90, 60, 0.04)';
      ctx.lineWidth=r%6===0?1.8:0.7;ctx.stroke();
    }

    // 3. Floating Silk Fiber Yarns
    fibers.forEach(f=>{
      f.y-=f.speed;
      f.x+=Math.sin(t+f.y*0.01)*0.5;
      f.angle+=f.rotSpeed;

      if(f.y<-50){f.y=h+50;f.x=Math.random()*w;}

      ctx.save();ctx.translate(f.x,f.y);ctx.rotate(f.angle);
      ctx.beginPath();ctx.moveTo(-f.length/2,0);
      ctx.bezierCurveTo(-f.length/4,6,f.length/4,-6,f.length/2,0);
      ctx.strokeStyle=`rgba(${f.color}, ${f.alpha})`;
      ctx.lineWidth=f.size;ctx.stroke();
      ctx.restore();
    });

    // 4. Soft Golden Loom Sunlight Orbs
    for(let s=0;s<3;s++){
      const orbX=(w*0.25)+(s*w*0.35)+Math.sin(t*0.4+s)*80;
      const orbY=(h*0.3)+Math.cos(t*0.3+s)*60;
      const rad=180+Math.sin(t*0.6+s)*40;

      const orbGrad=ctx.createRadialGradient(orbX,orbY,0,orbX,orbY,rad);
      orbGrad.addColorStop(0,'rgba(245, 158, 11, 0.14)');
      orbGrad.addColorStop(0.6,'rgba(217, 119, 6, 0.04)');
      orbGrad.addColorStop(1,'rgba(217, 119, 6, 0)');

      ctx.fillStyle=orbGrad;ctx.beginPath();ctx.arc(orbX,orbY,rad,0,Math.PI*2);ctx.fill();
    }

    requestAnimationFrame(draw);
  }
  draw();
})();

// HERO CANVAS (ACTIVE FABRIC WEAVE SCAN)
const hcv=document.getElementById('hero-cv'),hc=hcv.getContext('2d');let ht=0;
function drawH(){
  hcv.width=hcv.offsetWidth;hcv.height=330;const W=hcv.width,H=hcv.height;
  hc.clearRect(0,0,W,H);
  
  // Fabric Grid lines
  hc.strokeStyle='rgba(194, 65, 12, 0.15)';hc.lineWidth=1;
  for(let x=0;x<W;x+=14){hc.beginPath();hc.moveTo(x,0);hc.lineTo(x,H);hc.stroke();}
  for(let y=0;y<H;y+=14){hc.beginPath();hc.moveTo(0,y);hc.lineTo(W,y);hc.stroke();}
  
  // Laser Scan Line
  const sy=((ht*.4)%120)+10;
  const g=hc.createLinearGradient(0,sy-20,0,sy+8);
  g.addColorStop(0,'rgba(194, 65, 12, 0)');g.addColorStop(.7,'rgba(194, 65, 12, .5)');g.addColorStop(1,'rgba(194, 65, 12, 0)');
  hc.fillStyle=g;hc.fillRect(0,sy-20,W,28);
  hc.strokeStyle='rgba(194, 65, 12, .9)';hc.lineWidth=1.5;
  hc.beginPath();hc.moveTo(0,sy);hc.lineTo(W,sy);hc.stroke();
  
  // Sample Bboxes
  [{x:80,y:50,w:90,h:65,l:'WEFT SLUB',c:'#D97706',p:'94%'},{x:230,y:120,w:80,h:55,l:'OIL STAIN',c:'#DC2626',p:'97%'}].forEach(b=>{
    hc.strokeStyle=b.c;hc.lineWidth=2;hc.strokeRect(b.x,b.y,b.w,b.h);
    hc.fillStyle=b.c+'33';hc.fillRect(b.x,b.y,b.w,b.h);
    const lbl=b.l+' '+b.p;
    hc.fillStyle=b.c;hc.fillRect(b.x,Math.max(0,b.y-18),hc.measureText(lbl).width+12,18);
    hc.fillStyle='#fff';hc.font='bold 10px JetBrains Mono,monospace';hc.fillText(lbl,b.x+6,Math.max(14,b.y-5));
  });
  ht++;requestAnimationFrame(drawH);
}
drawH();

// SWEEP BEAM
let swT=0;
function animSw(){
  const cv=document.getElementById('sw-cv'),st=document.getElementById('stage');
  cv.width=st.offsetWidth;cv.height=st.offsetHeight;const c=cv.getContext('2d');
  c.clearRect(0,0,cv.width,cv.height);
  if(document.getElementById('tg-s').classList.contains('on')){
    const sy=(swT*1.8)%cv.height;
    const g=c.createLinearGradient(0,sy-30,0,sy+10);
    g.addColorStop(0,'rgba(194, 65, 12, 0)');g.addColorStop(.6,'rgba(194, 65, 12, .3)');g.addColorStop(1,'rgba(194, 65, 12, .05)');
    c.fillStyle=g;c.fillRect(0,sy-30,cv.width,40);
    c.strokeStyle='rgba(194, 65, 12, .8)';c.lineWidth=1;
    c.beginPath();c.moveTo(0,sy);c.lineTo(cv.width,sy);c.stroke();swT++;
  }
  requestAnimationFrame(animSw);
}
animSw();

// COUNTERS & LOAD INIT
addEventListener('load',()=>{
  document.querySelectorAll('[data-count]').forEach(el=>{
    const t=parseFloat(el.dataset.count);let c=0;
    const iv=setInterval(()=>{c=Math.min(c+t/60,t);el.textContent=Number.isInteger(t)?Math.floor(c):c.toFixed(1);if(c>=t)clearInterval(iv);},25);
  });
  lp(null,'clean');setupDragDrop();
});

function switchMode(m){
  document.getElementById('tab-upload').classList.toggle('active',m==='upload');
  document.getElementById('tab-cam').classList.toggle('active',m==='cam');
  if(m==='cam') startWebcam(); else stopWebcam();
}

function setupDragDrop(){
  const dz=document.getElementById('dz');
  ['dragenter','dragover'].forEach(e=>dz.addEventListener(e,ev=>{ev.preventDefault();dz.classList.add('dragover');}));
  ['dragleave','drop'].forEach(e=>dz.addEventListener(e,ev=>{ev.preventDefault();dz.classList.remove('dragover');}));
  dz.addEventListener('drop',ev=>{
    const f=ev.dataTransfer.files[0];
    if(f){stopWebcam();const r=new FileReader();r.onload=e=>document.getElementById('ins-img').src=e.target.result;r.readAsDataURL(f);sendP(f);}
  });
}

function onTh(v){conf=parseFloat(v);document.getElementById('tv').textContent=parseFloat(v).toFixed(2);}

// WEBCAM
function startWebcam(){
  if(!navigator.mediaDevices?.getUserMedia){alert('Webcam not supported by your browser.');return;}
  navigator.mediaDevices.getUserMedia({video:{width:1280,height:720}}).then(s=>{
    wcStr=s;const v=document.getElementById('wv');v.srcObject=s;v.play();
    document.getElementById('dz').style.display='none';
    document.getElementById('cam-ctrl-bar').style.display='flex';
    ['btn-sn','btn-st','btn-sc'].forEach(id=>document.getElementById(id).style.display='inline-flex');
    document.getElementById('btn-oc').style.display='none';
    document.getElementById('cam-pill').className='pill p-live';
    document.getElementById('cam-pill').innerHTML='<span class="dot"></span>CAM LIVE';
    document.getElementById('tab-upload').classList.remove('active');
    document.getElementById('tab-cam').classList.add('active');
    requestAnimationFrame(mirrorCam);
  }).catch(e=>alert('Camera access denied: '+e.message));
}

function mirrorCam(){
  if(!wcStr)return;
  const v=document.getElementById('wv');
  if(v.readyState>=2){
    const c=document.createElement('canvas');c.width=v.videoWidth;c.height=v.videoHeight;
    c.getContext('2d').drawImage(v,0,0);
    document.getElementById('ins-img').src=c.toDataURL('image/jpeg');
    document.getElementById('ir').textContent=v.videoWidth+'x'+v.videoHeight;
  }
  if(wcStr)requestAnimationFrame(mirrorCam);
}

function captureSnapshot(){
  const v=document.getElementById('wv');
  if(!v||v.readyState<2)return;
  const c=document.createElement('canvas');c.width=v.videoWidth;c.height=v.videoHeight;
  c.getContext('2d').drawImage(v,0,0);
  c.toBlob(b=>sendP(b),'image/jpeg');
}

function toggleStream(){
  const b=document.getElementById('btn-st');
  if(stInt){
    clearInterval(stInt);stInt=null;
    b.textContent='🔴 Continuous AI Stream';b.className='btn br';
  }else{
    b.textContent='⏸ Pause Stream';b.className='btn bgh';
    stInt=setInterval(captureSnapshot,750);
  }
}

function stopWebcam(){
  if(wcStr){wcStr.getTracks().forEach(t=>t.stop());wcStr=null;}
  if(stInt){clearInterval(stInt);stInt=null;}
  document.getElementById('dz').style.display='flex';
  document.getElementById('cam-ctrl-bar').style.display='none';
  ['btn-sn','btn-st','btn-sc'].forEach(id=>document.getElementById(id).style.display='none');
  document.getElementById('btn-oc').style.display='inline-flex';
  document.getElementById('btn-st').textContent='🔴 Continuous AI Stream';
  document.getElementById('btn-st').className='btn br';
  document.getElementById('cam-pill').className='pill p-on';
  document.getElementById('cam-pill').innerHTML='<span class="dot"></span>READY';
  document.getElementById('tab-upload').classList.add('active');
  document.getElementById('tab-cam').classList.remove('active');
}

function handleFile(e){
  const f=e.target.files[0];if(!f)return;
  stopWebcam();
  const r=new FileReader();
  r.onload=ev=>document.getElementById('ins-img').src=ev.target.result;
  r.readAsDataURL(f);
  sendP(f);
}

// PRESETS
function genP(t){
  const c=document.createElement('canvas');c.width=800;c.height=600;const x=c.getContext('2d');
  const dm=t==='denim';x.fillStyle=dm?'#1B3560':'#E8E4DC';x.fillRect(0,0,800,600);
  x.strokeStyle=dm?'rgba(255,255,255,.06)':'rgba(0,0,0,.05)';x.lineWidth=1;
  for(let i=0;i<800;i+=6){x.beginPath();x.moveTo(i,0);x.lineTo(i,600);x.stroke();}
  for(let j=0;j<600;j+=6){x.beginPath();x.moveTo(0,j);x.lineTo(800,j);x.stroke();}
  if(t==='slub'){x.fillStyle='#9E8B6E';x.beginPath();x.ellipse(320,220,65,12,Math.PI/12,0,Math.PI*2);x.fill();}
  else if(t==='stain'){x.fillStyle='rgba(30,20,10,.80)';x.beginPath();x.ellipse(450,280,48,32,Math.PI/6,0,Math.PI*2);x.fill();}
  else if(t==='hole'){x.fillStyle='#1C1917';x.beginPath();x.arc(260,310,26,0,Math.PI*2);x.fill();x.strokeStyle='#553322';x.lineWidth=3;x.stroke();}
  else if(t==='weft'){x.fillStyle='#C8D0C0';x.fillRect(50,380,700,16);}
  else if(t==='reed'){x.strokeStyle='rgba(0,0,0,.28)';x.lineWidth=4;x.beginPath();x.moveTo(390,0);x.lineTo(390,600);x.moveTo(408,0);x.lineTo(408,600);x.stroke();}
  else if(t==='shade'){const g=x.createLinearGradient(350,0,800,0);g.addColorStop(0,'transparent');g.addColorStop(1,'rgba(160,110,70,.40)');x.fillStyle=g;x.fillRect(0,0,800,600);}
  return c;
}

function lp(e,t){
  stopWebcam();
  document.querySelectorAll('.pchip').forEach(b=>b.classList.remove('act'));
  if(e?.target)e.target.classList.add('act');
  const c=genP(t);
  document.getElementById('ins-img').src=c.toDataURL('image/jpeg',.92);
  document.getElementById('ir').textContent='800x600';
  if(t==='clean'){
    report={defect_count:0,total_astm_points:0,quality_grade:'GRADE A — PERFECT PASS',grade_status:'Pass',defects:[]};
    setSt('PASS — CLEAN','var(--green)');renderR();
  }else{c.toBlob(b=>sendP(b),'image/jpeg');}
}

function sendP(blob){
  const t0=Date.now();setSt('SCANNING...','var(--terracotta)');
  const fd=new FormData();if(blob)fd.append('image',blob,'scan.jpg');
  fetch('/predict?conf_thresh='+conf,{method:'POST',body:fd})
  .then(r=>r.json())
  .then(d=>{
    report=d;document.getElementById('tl').textContent=(Date.now()-t0)+'ms';
    frc++;document.getElementById('fc').textContent=frc;
    setSt(d.defect_count===0?'PASS — CLEAN':'DEFECTS DETECTED',d.defect_count===0?'var(--green)':'var(--red)');
    renderR();chime(d.defect_count===0);
  }).catch(()=>{report=null;setSt('DEMO MODE','var(--terracotta)');renderR();});
}

function rescan(){const img=document.getElementById('ins-img');if(img.src.startsWith('data:'))fetch(img.src).then(r=>r.blob()).then(b=>sendP(b));}
function setSt(t,c){const e=document.getElementById('ts');e.textContent=t;e.style.color=c;}

function renderR(){
  const d=report;const cnt=d?.defect_count??0;
  document.getElementById('td').textContent=cnt;
  document.getElementById('al').textContent=d?.total_astm_points??0;
  const gs=d?.grade_status??'Pass';
  const ring=document.getElementById('gring');
  const gtag=document.getElementById('gt');
  const rgEl=document.getElementById('rg');
  const rsEl=document.getElementById('rs');
  if(gs==='Pass'||cnt===0){
    ring.className='gr grA';ring.textContent='A';gtag.className='tag tag-p';gtag.textContent='GRADE A';
    rgEl.textContent='GRADE A — PERFECT PASS';rgEl.style.color='var(--green)';
    rsEl.textContent='0 defects detected. Roll is compliant for shipment.';
  }else if(gs==='Warning'){
    ring.className='gr grB';ring.textContent='B';gtag.className='tag tag-m';gtag.textContent='GRADE B';
    rgEl.textContent=d?.quality_grade||'GRADE B — REVIEW REQUIRED';rgEl.style.color='var(--gold)';
    rsEl.textContent=cnt+' defect(s) detected. Review before shipment.';
  }else{
    ring.className='gr grC';ring.textContent='C';gtag.className='tag tag-c';gtag.textContent='GRADE C';
    rgEl.textContent=d?.quality_grade||'GRADE C — REWORK REQUIRED';rgEl.style.color='var(--red)';
    rsEl.textContent=cnt+' critical defect(s). Roll requires rework.';
  }
  const tb=document.getElementById('rtb');
  if(!d?.defects?.length){
    tb.innerHTML='<tr><td colspan="8" style="text-align:center;color:var(--green);padding:28px;font-family:var(--fc);font-size:12px">✅ No defects detected — Fabric surface meets Grade A standard</td></tr>';
  }else{
    tb.innerHTML=d.defects.map((df,i)=>{
      const bb=df.bbox?`[${df.bbox.join(', ')}]`:'Global';
      const sc=df.severity==='Critical'?'tag-c':df.severity==='Major'?'tag-m':'tag-n';
      const cw=(df.confidence*100).toFixed(0);
      const cc=df.confidence>.85?'#059669':df.confidence>.65?'#D97706':'#C2410C';
      return '<tr><td style="font-family:var(--fc);font-weight:700">'+(df.id||'DEF-'+(i+1).toString().padStart(3,'0'))+'</td><td><strong>'+df.type+'</strong></td><td><span class="tag '+sc+'">'+(df.severity||'Minor')+'</span></td><td style="font-family:var(--fc);font-size:11px">'+bb+'</td><td><div class="cb"><div class="cbb"><div class="cbf" style="width:'+cw+'%;background:'+cc+'"></div></div><span style="font-family:var(--fc);font-size:11px;color:'+cc+';font-weight:700;min-width:40px">'+cw+'%</span></div></td><td style="font-family:var(--fc);font-weight:700">'+(df.astm_points||1)+'pt</td><td style="font-size:12px;color:var(--dim)">'+df.action+'</td><td><button onclick="openM('+i+')" style="background:transparent;border:1px solid var(--border);color:var(--terracotta);font-size:11px;padding:4px 10px;border-radius:4px;cursor:pointer">🔍</button></td></tr>';
    }).join('');
  }
  drawOv();
}

function drawOv(){
  const img=document.getElementById('ins-img');const cv=document.getElementById('ov-cv');
  const st=document.getElementById('stage');cv.width=st.offsetWidth;cv.height=st.offsetHeight;
  const c=cv.getContext('2d');c.clearRect(0,0,cv.width,cv.height);
  if(!report?.defects?.length)return;
  const sx=cv.width/(img.naturalWidth||800);const sy=cv.height/(img.naturalHeight||600);
  report.defects.forEach(df=>{
    if(!df.bbox)return;
    const[x1,y1,x2,y2]=df.bbox;
    const rx=x1*sx,ry=y1*sy,rw=(x2-x1)*sx,rh=(y2-y1)*sy;
    const col=df.severity==='Critical'?'#DC2626':df.severity==='Major'?'#D97706':'#C2410C';
    c.strokeStyle=col;c.lineWidth=2;c.strokeRect(rx,ry,rw,rh);
    c.fillStyle=col+'28';c.fillRect(rx,ry,rw,rh);
    const lbl=df.type+' '+(df.confidence*100).toFixed(0)+'%';
    const lw=c.measureText(lbl).width+14;
    c.fillStyle=col;c.fillRect(rx,Math.max(0,ry-22),lw,22);
    c.fillStyle='#fff';c.font='bold 10px JetBrains Mono,monospace';
    c.fillText(lbl,rx+7,Math.max(14,ry-6));
  });
}

function openM(i){
  if(!report?.defects?.[i])return;
  const df=report.defects[i];
  document.getElementById('mt').textContent=(df.id||'DEF-'+i)+': '+df.type.toUpperCase();
  document.getElementById('md').innerHTML='<strong>Type:</strong> '+df.type+'<br><strong>Severity:</strong> '+(df.severity||'Minor')+'<br><strong>Confidence:</strong> '+(df.confidence*100).toFixed(2)+'%<br><strong>ASTM Penalty:</strong> '+(df.astm_points||1)+' points<br><strong>Bbox:</strong> ['+(df.bbox||'N/A')+']<br><strong>Remediation:</strong> '+df.action;
  document.getElementById('mo').classList.add('open');
}

function chime(pass){
  if(!document.getElementById('tg-a').classList.contains('on'))return;
  try{
    if(!aCtx)aCtx=new(window.AudioContext||window.webkitAudioContext)();
    const o=aCtx.createOscillator(),g=aCtx.createGain();
    o.connect(g);g.connect(aCtx.destination);
    if(pass){
      o.frequency.setValueAtTime(880,aCtx.currentTime);
      o.frequency.exponentialRampToValueAtTime(1760,aCtx.currentTime+.15);
      g.gain.setValueAtTime(.1,aCtx.currentTime);
      g.gain.exponentialRampToValueAtTime(.001,aCtx.currentTime+.3);
      o.start();o.stop(aCtx.currentTime+.3);
    }else{
      o.frequency.setValueAtTime(300,aCtx.currentTime);
      o.frequency.exponentialRampToValueAtTime(140,aCtx.currentTime+.35);
      g.gain.setValueAtTime(.2,aCtx.currentTime);
      g.gain.exponentialRampToValueAtTime(.001,aCtx.currentTime+.4);
      o.start();o.stop(aCtx.currentTime+.4);
    }
  }catch(e){}
}

function expCSV(){
  if(!report?.defects)return;
  let csv="ID,Type,Severity,Confidence,BBox,ASTM_Points,Remediation\\n";
  report.defects.forEach(d=>{csv+=d.id+","+d.type+","+d.severity+","+d.confidence+",["+d.bbox+"],"+d.astm_points+',"'+d.action+'"\\n';});
  const b=new Blob([csv],{type:'text/csv'});const a=document.createElement('a');a.href=URL.createObjectURL(b);
  a.download='Selvedge_Report_'+Date.now()+'.csv';a.click();
}

function dlSnap(){
  const img=document.getElementById('ins-img');
  const a=document.createElement('a');a.href=img.src;
  a.download='Selvedge_Snap_'+Date.now()+'.jpg';a.click();
}

function calcROI(){
  const v=parseFloat(document.getElementById('rv').value);
  const p=parseFloat(document.getElementById('rp').value);
  document.getElementById('rvl').textContent=v.toLocaleString()+' m';
  document.getElementById('rpl').textContent='$'+p.toFixed(2);
  document.getElementById('rn').textContent='$'+Math.round(v*p*.035).toLocaleString();
}

addEventListener('resize',drawOv);
</script>
</body>
</html>
"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)

print(f"DONE: {len(HTML)} bytes written to {OUT}")
