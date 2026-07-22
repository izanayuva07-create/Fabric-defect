import os

OUT = r"c:\Users\crist\OneDrive\Desktop\Fbric Defect detection\selvedge.html"

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SELVEDGE AI — Industrial Fabric Inspection Platform</title>
<meta name="description" content="Selvedge AI Automated Fabric Defect Inspection Platform. Multi-model neural vision, 3D fabric showcase, ASTM D5430 quality grading, live webcam stream, user login, and subscription tiers.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&family=Syne:wght@700;800&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
:root{
  --void:#FAF7F2;--base:#F4EFE6;--panel:rgba(255,255,255,0.95);--lift:#EFE8DC;--lift2:#E5DDCF;
  --border:rgba(180,130,70,0.24);--border-b:rgba(194,65,12,0.35);
  --text:#1C1917;--dim:#57534E;--ghost:#78716C;
  --terracotta:#C2410C;--terracotta-g:rgba(194,65,12,0.14);
  --gold:#D97706;--gold-g:rgba(217,119,6,0.14);
  --green:#059669;--green-g:rgba(5,150,105,0.14);
  --red:#DC2626;--red-g:rgba(220,38,38,0.14);--yellow:#D97706;
  --fh:"Syne",sans-serif;--fb:"Outfit",sans-serif;--fc:"JetBrains Mono",monospace;
  --r1:10px;--r2:16px;--r3:20px
}
body{background:var(--void);color:var(--text);font-family:var(--fb);overflow-x:hidden;line-height:1.6}
#particles{position:fixed;inset:0;z-index:0;pointer-events:none}
.rel{position:relative;z-index:1}
.con{max-width:1400px;margin:0 auto;padding:0 24px}

/* CLEAN NAVBAR WITH 3-LINE HAMBURGER MENU */
nav{position:fixed;top:0;left:0;right:0;z-index:999;
  background:rgba(250,247,242,.94);backdrop-filter:blur(20px) saturate(180%);
  border-bottom:1px solid var(--border);height:64px;display:flex;align-items:center}
.nav-i{max-width:1400px;margin:0 auto;padding:0 24px;
  display:flex;align-items:center;justify-content:space-between;width:100%}
.nav-left{display:flex;align-items:center;gap:14px}

/* 3-LINE HAMBURGER BUTTON */
.menu-btn{background:var(--lift);border:1px solid var(--border);width:38px;height:38px;
  border-radius:10px;display:flex;flex-direction:column;align-items:center;justify-content:center;
  gap:4px;cursor:pointer;transition:all .2s}
.menu-btn:hover{background:#fff;border-color:var(--terracotta)}
.menu-btn span{width:18px;height:2px;background:var(--text);border-radius:2px;transition:all .2s}

.logo{display:flex;align-items:center;gap:10px;font-family:var(--fh);font-size:18px;font-weight:800;letter-spacing:1.5px;color:var(--text)}
.logo-ic{width:34px;height:34px;background:linear-gradient(135deg,var(--terracotta),var(--gold));
  border-radius:10px;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 14px var(--terracotta-g)}
.logo-ic svg{width:18px;height:18px;stroke:#fff;fill:none;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
.ai-t{background:linear-gradient(135deg,var(--terracotta),var(--gold));-webkit-background-clip:text;-webkit-text-fill-color:transparent}

.nav-links{display:flex;gap:28px;list-style:none}
.nav-links a{color:var(--dim);text-decoration:none;font-size:13px;font-weight:600;transition:color .2s}
.nav-links a:hover{color:var(--terracotta)}

.nav-cta{display:flex;gap:10px;align-items:center}

/* PILLS */
.pill{display:inline-flex;align-items:center;gap:6px;
  font-family:var(--fc);font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.8px;
  padding:4px 12px;border-radius:99px;border:1px solid}
.p-on{color:var(--green);border-color:var(--green);background:var(--green-g)}
.p-live{color:var(--red);border-color:var(--red);background:var(--red-g);animation:bpill .9s infinite}
@keyframes bpill{0%,100%{opacity:1}50%{opacity:.5}}
.dot{width:6px;height:6px;border-radius:50%;background:currentColor}

/* BUTTONS */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:6px;font-family:var(--fb);font-weight:700;font-size:13px;
  padding:10px 20px;border-radius:var(--r1);cursor:pointer;border:none;transition:all .2s;white-space:nowrap;text-decoration:none}
.bg{background:linear-gradient(135deg,var(--terracotta),#EA580C);color:#fff;box-shadow:0 4px 14px var(--terracotta-g)}
.bg:hover{transform:translateY(-2px);box-shadow:0 6px 20px var(--terracotta-g)}
.bgh{background:rgba(255,255,255,.9);color:var(--text);border:1px solid var(--border-b)}
.bgh:hover{color:var(--terracotta);border-color:var(--terracotta);background:var(--terracotta-g)}
.br{background:var(--red);color:#fff;box-shadow:0 4px 14px var(--red-g)}
.br:hover{transform:translateY(-1px)}

/* SLIDE-OUT LEFT DRAWER MENU */
.drawer-overlay{position:fixed;inset:0;background:rgba(28,25,23,.5);backdrop-filter:blur(8px);
  z-index:9999;opacity:0;pointer-events:none;transition:opacity .25s ease}
.drawer-overlay.open{opacity:1;pointer-events:auto}
.drawer{position:fixed;top:0;left:0;bottom:0;width:320px;background:var(--panel);
  border-right:1px solid var(--border-b);z-index:10000;transform:translateX(-100%);
  transition:transform .25s cubic-bezier(0.16,1,0.3,1);padding:24px;display:flex;flex-direction:column;
  box-shadow:10px 0 30px rgba(0,0,0,0.15)}
.drawer-overlay.open .drawer{transform:translateX(0)}

.drawer-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:24px;
  padding-bottom:16px;border-bottom:1px solid var(--border)}
.drawer-header h3{font-family:var(--fh);font-size:16px;font-weight:800;color:var(--text)}
.drawer-close{background:none;border:none;font-size:18px;color:var(--dim);cursor:pointer}

.drawer-user{background:var(--lift);border:1px solid var(--border);border-radius:var(--r1);padding:14px;
  margin-bottom:20px;display:flex;align-items:center;gap:12px;cursor:pointer}
.drawer-user:hover{border-color:var(--terracotta)}
.drawer-user .u-ic{width:36px;height:36px;border-radius:50%;background:linear-gradient(135deg,var(--terracotta),var(--gold));
  color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700}
.drawer-user .u-info h4{font-size:13px;font-weight:700}
.drawer-user .u-info p{font-size:11px;color:var(--dim)}

.drawer-menu{list-style:none;display:flex;flex-direction:column;gap:8px}
.drawer-menu a{display:flex;align-items:center;gap:12px;padding:12px 14px;border-radius:var(--r1);
  color:var(--text);text-decoration:none;font-weight:600;font-size:13px;transition:all .15s}
.drawer-menu a:hover{background:var(--lift);color:var(--terracotta)}

/* MAIN WORKSPACE HEADER (FIRST MAIN SECTION) */
.hdr{padding:84px 0 16px}
.hdr-flex{display:flex;justify-content:space-between;align-items:flex-end}
.hdr-title h1{font-family:var(--fh);font-size:28px;font-weight:800;color:var(--text)}
.hdr-title p{font-size:13px;color:var(--dim);margin-top:2px}

/* STUDIO WORKBENCH GRID (FIRST MAIN SECTION) */
.studio{padding:10px 0 40px}
.wbench{display:grid;grid-template-columns:310px 1fr;gap:20px;align-items:start}

/* CONTROL PANEL */
.cp{background:var(--panel);border:1px solid var(--border);border-radius:var(--r2);overflow:hidden;
  box-shadow:0 6px 24px rgba(0,0,0,0.03)}
.cp-h{background:var(--lift);padding:12px 16px;border-bottom:1px solid var(--border);
  display:flex;justify-content:space-between;align-items:center;
  font-family:var(--fc);font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:var(--terracotta)}
.cp-b{padding:16px}
.cg{margin-bottom:18px}
.cg:last-child{margin-bottom:0}
.cl{font-size:11px;font-weight:700;color:var(--dim);text-transform:uppercase;letter-spacing:.8px;
  display:flex;justify-content:space-between;margin-bottom:8px}
.cl .v{font-family:var(--fc);color:var(--terracotta);font-size:12px;font-weight:700}
input[type=range]{-webkit-appearance:none;appearance:none;width:100%;height:5px;
  background:var(--lift2);border-radius:3px;outline:none}
input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;appearance:none;
  width:16px;height:16px;border-radius:50%;background:linear-gradient(135deg,var(--terracotta),#EA580C);
  cursor:pointer;box-shadow:0 3px 8px var(--terracotta-g)}

/* MODE SELECTOR */
.mode-selector{display:flex;background:var(--lift);padding:4px;border-radius:var(--r1);
  border:1px solid var(--border);margin-bottom:16px}
.mode-tab{flex:1;text-align:center;padding:8px 10px;font-size:12px;font-weight:700;
  border-radius:6px;cursor:pointer;transition:all .2s;color:var(--dim)}
.mode-tab.active{background:var(--terracotta);color:#fff;box-shadow:0 3px 10px var(--terracotta-g)}

.pgrid{display:grid;grid-template-columns:1fr 1fr;gap:6px}
.pchip{background:var(--lift);border:1px solid var(--border);color:var(--text);
  font-size:11px;font-weight:600;padding:8px 10px;border-radius:8px;
  cursor:pointer;transition:all .15s;text-align:left}
.pchip:hover,.pchip.act{background:#fff;border-color:var(--terracotta);color:var(--terracotta);box-shadow:0 3px 8px rgba(194,65,12,0.1)}
.pchip.cln:hover,.pchip.cln.act{border-color:var(--green);color:var(--green);box-shadow:0 3px 8px var(--green-g)}

/* TOGGLES */
.trow{display:flex;justify-content:space-between;align-items:center;padding:8px 0;border-bottom:1px solid var(--border)}
.trow:last-child{border-bottom:none}
.tl{font-size:12px;color:var(--dim);font-weight:500}
.tgl{width:38px;height:20px;background:var(--lift2);border-radius:10px;position:relative;cursor:pointer;
  transition:background .2s;border:1px solid var(--border)}
.tgl::after{content:"";position:absolute;top:2px;left:2px;width:14px;height:14px;background:var(--ghost);
  border-radius:50%;transition:all .2s}
.tgl.on{background:var(--terracotta)}
.tgl.on::after{left:18px;background:#fff}

/* STAGE */
.stage{background:var(--panel);border:1px solid var(--border);border-radius:var(--r2);overflow:hidden;position:relative;
  box-shadow:0 6px 24px rgba(0,0,0,0.03)}
.st-bar{background:var(--lift);padding:10px 16px;border-bottom:1px solid var(--border);
  display:flex;justify-content:space-between;align-items:center}
.st-info{display:flex;align-items:center;gap:14px;font-family:var(--fc);font-size:11px}
.st-info span{color:var(--dim);font-weight:600}
.st-info strong{color:var(--text)}
.st-vp{position:relative;min-height:480px;display:flex;align-items:center;justify-content:center;
  background:#1C1917;overflow:hidden}
#ins-img{max-width:100%;max-height:540px;display:block;margin:0 auto;object-fit:contain;filter:none!important}
#ov-cv,#sw-cv{position:absolute;inset:0;pointer-events:none;width:100%;height:100%}
.cam-ctrl-bar{position:absolute;bottom:16px;left:50%;transform:translateX(-50%);z-index:20;
  display:flex;gap:10px;background:rgba(255,255,255,.94);backdrop-filter:blur(16px);
  padding:8px 16px;border-radius:99px;border:1px solid var(--border);box-shadow:0 8px 24px rgba(0,0,0,0.1)}

/* RESULTS HUD */
.hud{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:16px}
.hcard{background:var(--panel);border:1px solid var(--border);border-radius:var(--r2);padding:16px;
  box-shadow:0 4px 16px rgba(0,0,0,0.02)}
.hcard .hl{font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.8px;color:var(--ghost);margin-bottom:4px}
.hcard .hv{font-family:var(--fc);font-size:22px;font-weight:800;color:var(--text)}
.hcard .hs{font-size:11px;color:var(--dim);margin-top:2px}

/* SMART ANALYTICS & DEFECT HEATMAP SECTION */
.smart-analytics{margin-top:20px;background:var(--panel);border:1px solid var(--border);border-radius:var(--r2);padding:16px;
  box-shadow:0 4px 16px rgba(0,0,0,0.02)}
.smart-analytics-h{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px}
.smart-analytics-h h4{font-family:var(--fc);font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:var(--terracotta)}
#sig-cv{width:100%;height:60px;background:var(--lift);border-radius:8px;display:block}

/* 3 UNCHANGED TRAINED FABRIC IMAGES SHOWCASE GALLERY */
.fabric-showcase{padding:40px 0 50px}
.sec-head{text-align:center;margin-bottom:30px}
.sec-head h2{font-family:var(--fh);font-size:26px;font-weight:800;color:var(--text)}
.sec-head p{font-size:13px;color:var(--dim);margin-top:4px}

.fab-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.fab-card{background:var(--panel);border:1px solid var(--border);border-radius:var(--r2);overflow:hidden;
  box-shadow:0 8px 30px rgba(0,0,0,0.04);transition:all .3s ease;display:flex;flex-direction:column}
.fab-card:hover{transform:translateY(-6px);border-color:var(--terracotta);box-shadow:0 14px 40px rgba(194,65,12,0.12)}
.fab-img-wrap{position:relative;height:220px;overflow:hidden;background:#1C1917}
.fab-img-wrap img{width:100%;height:100%;object-fit:cover;transition:transform .5s ease}
.fab-card:hover .fab-img-wrap img{transform:scale(1.06)}
.fab-tag{position:absolute;top:14px;left:14px;background:rgba(28,25,23,0.85);backdrop-filter:blur(8px);
  color:#fff;font-family:var(--fc);font-size:10px;font-weight:700;padding:4px 10px;border-radius:6px;
  text-transform:uppercase;letter-spacing:.8px;border:1px solid rgba(255,255,255,0.2)}
.fab-body{padding:20px;flex:1;display:flex;flex-direction:column;justify-content:space-between}
.fab-body h3{font-size:16px;font-weight:800;color:var(--text);margin-bottom:6px}
.fab-body p{font-size:12px;color:var(--dim);line-height:1.5;margin-bottom:14px}

/* PARAGRAPHS ABOUT FABRIC DEFECTS SECTION */
.defects-info{padding:50px 0;background:var(--lift);border-top:1px solid var(--border);border-bottom:1px solid var(--border)}
.def-grid{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}
.def-text h2{font-family:var(--fh);font-size:28px;font-weight:800;color:var(--text);margin-bottom:14px}
.def-text p{font-size:14px;color:var(--dim);line-height:1.7;margin-bottom:14px}
.def-box{background:var(--panel);border:1px solid var(--border);border-radius:var(--r2);padding:24px;
  box-shadow:0 6px 24px rgba(0,0,0,0.03)}
.def-box h4{font-family:var(--fc);font-size:11px;font-weight:700;color:var(--terracotta);text-transform:uppercase;
  letter-spacing:1px;margin-bottom:12px}
.def-box ul{list-style:none;display:flex;flex-direction:column;gap:10px}
.def-box li{display:flex;align-items:flex-start;gap:10px;font-size:12px;color:var(--text)}
.def-box li span{color:var(--terracotta);font-weight:800}

/* ADVANTAGES OF OUR WEBPAGE SECTION */
.advantages{padding:60px 0}
.adv-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:30px}
.adv-card{background:var(--panel);border:1px solid var(--border);border-radius:var(--r2);padding:24px;
  box-shadow:0 6px 24px rgba(0,0,0,0.03);transition:all .25s ease}
.adv-card:hover{border-color:var(--terracotta);transform:translateY(-4px)}
.adv-ic{width:44px;height:44px;border-radius:12px;background:var(--terracotta-g);color:var(--terracotta);
  display:flex;align-items:center;justify-content:center;font-size:20px;margin-bottom:16px;font-weight:800}
.adv-card h3{font-size:16px;font-weight:800;color:var(--text);margin-bottom:6px}
.adv-card p{font-size:12px;color:var(--dim);line-height:1.6}

/* FEATURES WE PROVIDE SECTION */
.features-sec{padding:60px 0;background:var(--base);border-top:1px solid var(--border)}
.feat-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:30px}
.feat-card{background:var(--panel);border:1px solid var(--border);border-radius:var(--r2);padding:24px;
  box-shadow:0 6px 24px rgba(0,0,0,0.03)}
.feat-card .num{font-family:var(--fc);font-size:10px;font-weight:800;color:var(--gold);text-transform:uppercase;margin-bottom:6px}
.feat-card h3{font-size:15px;font-weight:800;color:var(--text);margin-bottom:6px}
.feat-card p{font-size:12px;color:var(--dim);line-height:1.5}

/* REPORT SECTION */
.rep-sec{padding:24px 0 60px}
.rep-grid{display:grid;grid-template-columns:280px 1fr;gap:20px;align-items:start}
.gbox{background:var(--panel);border:1px solid var(--border);border-radius:var(--r2);padding:20px;text-align:center;
  box-shadow:0 6px 24px rgba(0,0,0,0.03)}
.gr{width:76px;height:76px;border-radius:50%;margin:0 auto 12px;display:flex;align-items:center;
  justify-content:center;font-family:var(--fh);font-size:30px;font-weight:800;border:3px solid}
.grA{border-color:var(--green);color:var(--green);background:var(--green-g);box-shadow:0 0 20px var(--green-g)}
.grB{border-color:var(--yellow);color:var(--yellow);background:rgba(217,119,6,.15);box-shadow:0 0 20px rgba(217,119,6,.15)}
.grC{border-color:var(--red);color:var(--red);background:var(--red-g);box-shadow:0 0 20px var(--red-g)}
.gbox h3{font-size:16px;font-weight:700;margin-bottom:4px;color:var(--text)}
.gbox p{font-size:12px;color:var(--dim);line-height:1.4;margin-bottom:14px}

.tbl-card{background:var(--panel);border:1px solid var(--border);border-radius:var(--r2);overflow:hidden;
  box-shadow:0 6px 24px rgba(0,0,0,0.03)}
.tbl-h{background:var(--lift);padding:12px 16px;border-bottom:1px solid var(--border);
  display:flex;justify-content:space-between;align-items:center}
.tbl-h h3{font-family:var(--fc);font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:var(--text)}
table{width:100%;border-collapse:collapse}
th,td{padding:10px 14px;text-align:left;font-size:12px;border-bottom:1px solid var(--border)}
th{background:var(--lift);color:var(--ghost);font-family:var(--fc);font-size:10px;text-transform:uppercase;letter-spacing:.8px;font-weight:700}
td{color:var(--text)}
tr:last-child td{border-bottom:none}
.tag{display:inline-block;padding:2px 8px;border-radius:4px;font-family:var(--fc);font-size:10px;font-weight:700;text-transform:uppercase}
.tag-p{background:var(--green-g);color:var(--green);border:1px solid var(--green)}
.tag-m{background:rgba(217,119,6,.15);color:var(--gold);border:1px solid var(--gold)}
.tag-c{background:var(--red-g);color:var(--red);border:1px solid var(--red)}
.tag-n{background:var(--lift2);color:var(--dim);border:1px solid var(--border)}
.cb{display:flex;align-items:center;gap:6px}
.cbb{flex:1;height:5px;background:var(--lift2);border-radius:3px;overflow:hidden}
.cbf{height:100%;border-radius:3px}

/* MODALS */
.mo{position:fixed;inset:0;z-index:99999;background:rgba(28,25,23,.65);backdrop-filter:blur(16px);
  display:none;align-items:center;justify-content:center;padding:20px}
.mo.open{display:flex}
.mb{background:var(--panel);border:1px solid var(--border-b);border-radius:var(--r3);
  width:100%;max-width:480px;padding:24px;box-shadow:0 20px 60px rgba(0,0,0,.2)}
.mh{display:flex;justify-content:space-between;align-items:center;margin-bottom:16px}
.mh span{font-family:var(--fh);font-size:16px;font-weight:800;color:var(--text)}

/* FORM INPUTS IN LOGIN MODAL */
.form-grp{margin-bottom:14px}
.form-grp label{display:block;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.8px;color:var(--dim);margin-bottom:6px}
.form-grp input{width:100%;padding:10px 12px;border-radius:var(--r1);border:1px solid var(--border);
  background:var(--lift);font-family:var(--fb);font-size:13px;color:var(--text);outline:none}
.form-grp input:focus{border-color:var(--terracotta);background:#fff}

/* PRICING TIERS IN SUBSCRIPTION MODAL */
.sub-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:14px}
.sub-card{background:var(--lift);border:1px solid var(--border);border-radius:var(--r1);padding:16px;text-align:center}
.sub-card.pop{border-color:var(--terracotta);background:#fff;box-shadow:0 4px 14px var(--terracotta-g)}
.sub-card h4{font-size:15px;font-weight:800;color:var(--text)}
.sub-card .price{font-family:var(--fc);font-size:22px;font-weight:800;color:var(--terracotta);margin:8px 0}
.sub-card p{font-size:11px;color:var(--dim);line-height:1.4;margin-bottom:12px}

footer{border-top:1px solid var(--border);padding:24px 0;margin-top:40px;background:var(--base)}
.fi{max-width:1400px;margin:0 auto;padding:0 24px;display:flex;justify-content:space-between;
  align-items:center;font-size:11px;color:var(--ghost);font-family:var(--fc);font-weight:600}
</style>
</head>
<body>

<canvas id="particles"></canvas>

<div class="rel">
  <!-- NAVIGATION BAR WITH HAMBURGER 3-LINES -->
  <nav>
    <div class="nav-i">
      <div class="nav-left">
        <button class="menu-btn" onclick="toggleDrawer()" title="Menu">
          <span></span><span></span><span></span>
        </button>

        <div class="logo">
          <div class="logo-ic">
            <svg viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
          </div>
          <span>SELVEDGE <span class="ai-t">AI</span></span>
        </div>
      </div>

      <ul class="nav-links">
        <li><a href="#studio">Inspector</a></li>
        <li><a href="#showcase">3 Swatches</a></li>
        <li><a href="#defects-info">Defect Guide</a></li>
        <li><a href="#advantages">Advantages</a></li>
        <li><a href="#features">Features</a></li>
      </ul>

      <div class="nav-cta">
        <div class="pill p-on" id="sys-pill"><span class="dot"></span>ONLINE</div>
        <button class="btn bgh" onclick="openLoginModal()">👤 Sign In</button>
        <button class="btn bg" onclick="document.getElementById('file-input').click()">📁 Select Swatch</button>
      </div>
    </div>
  </nav>

  <!-- SLIDE-OUT LEFT MENU DRAWER -->
  <div class="drawer-overlay" id="drawer-overlay" onclick="if(event.target===this)closeDrawer()">
    <div class="drawer">
      <div class="drawer-header">
        <h3>SELVEDGE AI MENU</h3>
        <button class="drawer-close" onclick="closeDrawer()">✕</button>
      </div>

      <div class="drawer-user" onclick="closeDrawer();openLoginModal()">
        <div class="u-ic">👤</div>
        <div class="u-info">
          <h4>Operator Portal</h4>
          <p>Sign in to sync loom audit logs</p>
        </div>
      </div>

      <ul class="drawer-menu">
        <li><a href="#studio" onclick="closeDrawer()">🔍 Studio Inspector</a></li>
        <li><a href="#showcase" onclick="closeDrawer()">🧵 3 Fabric Swatches</a></li>
        <li><a href="#defects-info" onclick="closeDrawer()">📖 Fabric Defect Guide</a></li>
        <li><a href="#advantages" onclick="closeDrawer()">⚡ Platform Advantages</a></li>
        <li><a href="#features" onclick="closeDrawer()">🛠️ Key System Features</a></li>
        <li><a href="#report" onclick="closeDrawer()">📊 ASTM Audit Ledger</a></li>
        <li><a href="#" onclick="closeDrawer();openAboutModal()">ℹ️ About Platform</a></li>
        <li><a href="#" onclick="closeDrawer();openSubModal()">💳 Subscription Plans</a></li>
      </ul>
    </div>
  </div>

  <!-- MAIN WORKSPACE HEADER (FIRST MAIN SECTION AT TOP) -->
  <header class="hdr" id="studio">
    <div class="con">
      <div class="hdr-flex">
        <div class="hdr-title">
          <h1>Industrial Fabric Defect Inspection System</h1>
          <p>SELVEDGE AI Real-Time Multi-Model Neural Vision & ASTM D5430 Quality Audit Workspace</p>
        </div>
        <div style="display:flex;gap:10px">
          <span class="pill p-on" id="cam-pill"><span class="dot"></span>READY</span>
        </div>
      </div>
    </div>
  </header>

  <!-- STUDIO WORKBENCH (FIRST MAIN WORKSPACE SECTION) -->
  <section class="studio">
    <div class="con">
      <div class="wbench">
        <!-- CONTROL PANEL -->
        <div class="cp">
          <div class="cp-h">
            <span>Inspector Controls</span>
            <span>⚙️</span>
          </div>
          <div class="cp-b">
            <!-- MODE TABS -->
            <div class="mode-selector">
              <div class="mode-tab active" id="tab-upload" onclick="switchMode('upload');document.getElementById('file-input').click()">📁 File Upload</div>
              <div class="mode-tab" id="tab-cam" onclick="switchMode('cam')">📷 Live Camera</div>
            </div>

            <!-- SLIDER -->
            <div class="cg">
              <div class="cl">
                <span>Confidence Threshold</span>
                <span class="v" id="tv">0.20</span>
              </div>
              <input type="range" id="conf-slider" min="0.05" max="0.95" step="0.05" value="0.20" oninput="onTh(this.value)">
            </div>

            <!-- UNCHANGED SAMPLE TRAINED DATASET PRESETS -->
            <div class="cg">
              <div class="cl"><span>Sample Defect Swatches</span></div>
              <div class="pgrid">
                <button class="pchip cln act" onclick="lp(event,'clean')">✨ Clean (Pass)</button>
                <button class="pchip" onclick="lp(event,'stain')">💧 Fabric Stain</button>
                <button class="pchip" onclick="lp(event,'thread')">🧶 Thread Error</button>
                <button class="pchip" onclick="lp(event,'hole')">🕳️ Tear / Hole</button>
                <button class="pchip" onclick="lp(event,'oil')">🛢️ Oil Spot</button>
                <button class="pchip" onclick="lp(event,'stitch')">🪡 Broken Stitch</button>
                <button class="pchip" onclick="lp(event,'lines')">🧵 Reed Lines</button>
              </div>
            </div>

            <!-- TOGGLES -->
            <div class="cg">
              <div class="cl"><span>Display Overlay</span></div>
              <div class="trow">
                <span class="tl">Bounding Boxes</span>
                <div class="tgl on" id="tg-b" onclick="this.classList.toggle('on');drawOv()"></div>
              </div>
              <div class="trow">
                <span class="tl">Laser Scan Beam</span>
                <div class="tgl on" id="tg-s" onclick="this.classList.toggle('on')"></div>
              </div>
              <div class="trow">
                <span class="tl">Audio Alert Chime</span>
                <div class="tgl on" id="tg-a" onclick="this.classList.toggle('on')"></div>
              </div>
            </div>

            <div style="display:flex;flex-direction:column;gap:8px;margin-top:12px">
              <button class="btn bg" id="predict-btn" style="width:100%" onclick="rescan()">🔍 Re-Scan Surface</button>
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
              <div style="display:flex;gap:8px">
                <button class="btn bgh" style="padding:4px 10px;font-size:11px" onclick="document.getElementById('file-input').click()">📁 Select Image</button>
                <button class="btn bgh" style="padding:4px 10px;font-size:11px" onclick="dlSnap()">💾 Export Frame</button>
              </div>
            </div>

            <div class="st-vp" id="stage">
              <img id="ins-img" src="/test_clean.jpg" alt="Fabric Scan" crossorigin="anonymous">
              <canvas id="ov-cv"></canvas>
              <canvas id="sw-cv"></canvas>

              <video id="wv" style="display:none" autoplay playsinline muted></video>
              <input type="file" id="file-input" accept="image/*" style="display:none" onchange="handleFile(event)">

              <!-- WEBCAM CONTROL BAR -->
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
              <div class="hs">Points / 100 sq yds</div>
            </div>
            <div class="hcard">
              <div class="hl">Grade Standard</div>
              <div class="hv" id="gt" style="color:var(--green);font-size:17px">GRADE A</div>
              <div class="hs" id="rg">GRADE A — PERFECT PASS</div>
            </div>
            <div class="hcard">
              <div class="hl">Frames Scanned</div>
              <div class="hv" id="fc" style="color:var(--dim)">0</div>
              <div class="hs">Total roll frames</div>
            </div>
          </div>

          <!-- SMART ANALYTICS TELEMETRY / WEAVE VARIANCE HEATMAP -->
          <div class="smart-analytics">
            <div class="smart-analytics-h">
              <h4>Real-Time Weave Anomaly & Defect Telemetry Signal</h4>
              <span style="font-family:var(--fc);font-size:10px;color:var(--dim)">PIXEL VARIANCE // ASTM D5430 WAVE</span>
            </div>
            <canvas id="sig-cv"></canvas>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 3 UNCHANGED TRAINED FABRIC IMAGES SHOWCASE GALLERY -->
  <section class="fabric-showcase" id="showcase">
    <div class="con">
      <div class="sec-head">
        <h2>3 High-Resolution Fabric Inspection Swatches</h2>
        <p>Explore real-world trained textile samples evaluated by SELVEDGE AI neural vision</p>
      </div>

      <div class="fab-grid">
        <!-- FABRIC 1: BLUE LIQUID STAIN -->
        <div class="fab-card">
          <div class="fab-img-wrap">
            <span class="fab-tag">01 · Liquid Stain</span>
            <img src="/ref_stain.jpg" alt="Blue Fabric Liquid Stain Swatch">
          </div>
          <div class="fab-body">
            <div>
              <h3>Blue Fabric Stain Swatch</h3>
              <p>Detects chemical, oil, and liquid discolorations using ResNet-18 binary and multi-class stain engines to prevent dye house rejection.</p>
            </div>
            <button class="btn bgh" style="width:100%;margin-top:14px" onclick="document.querySelector('#studio').scrollIntoView({behavior:'smooth'});lp(null,'stain')">🔍 Inspect Liquid Stain</button>
          </div>
        </div>

        <!-- FABRIC 2: WOVEN THREAD ERROR -->
        <div class="fab-card">
          <div class="fab-img-wrap">
            <span class="fab-tag">02 · Thread Error</span>
            <img src="/ref_thread_error.jpg" alt="Woven Fabric Thread Error Swatch">
          </div>
          <div class="fab-body">
            <div>
              <h3>Woven Thread Error Swatch</h3>
              <p>Identifies warp/weft thread misweaves, slubs, knot anomalies, and missing yarn ends at sub-millimeter precision directly on active looms.</p>
            </div>
            <button class="btn bgh" style="width:100%;margin-top:14px" onclick="document.querySelector('#studio').scrollIntoView({behavior:'smooth'});lp(null,'thread')">🔍 Inspect Thread Error</button>
          </div>
        </div>

        <!-- FABRIC 3: DENIM TEAR & HOLE -->
        <div class="fab-card">
          <div class="fab-img-wrap">
            <span class="fab-tag">03 · Structural Tear</span>
            <img src="/ref_hole.jpg" alt="Denim Fabric Hole & Tear Swatch">
          </div>
          <div class="fab-body">
            <div>
              <h3>Denim Hole & Tear Swatch</h3>
              <p>Pinpoints structural punctures, frayed tears, and needle punctures to trigger immediate loom shutdown before full roll damage occurs.</p>
            </div>
            <button class="btn bgh" style="width:100%;margin-top:14px" onclick="document.querySelector('#studio').scrollIntoView({behavior:'smooth'});lp(null,'hole')">🔍 Inspect Denim Hole</button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- PARAGRAPHS ABOUT FABRIC DEFECTS SECTION -->
  <section class="defects-info" id="defects-info">
    <div class="con">
      <div class="def-grid">
        <div class="def-text">
          <h2>Understanding Industrial Fabric Defects</h2>
          <p>Fabric defects occur during weaving, knitting, or finishing stages due to yarn tension fluctuations, mechanical loom wear, chemical spills, or broken warp ends. Unchecked flaws severely reduce fabric commercial value and result in heavy financial penalties for textile manufacturers.</p>
          <p>Manual human inspection in modern high-speed looms is slow, subjective, and prone to fatigue, missing up to <strong>30% of critical flaws</strong>. SELVEDGE AI automates surface scanning with sub-8ms neural vision, instantly localizing and grading defects according to international standards.</p>
        </div>
        <div class="def-box">
          <h4>Common Loom Defect Categories</h4>
          <ul>
            <li><span>• Holes & Structural Tears:</span> Punctures causing roll rejection.</li>
            <li><span>• Oil & Chemical Stains:</span> Contamination from loom lubrication points.</li>
            <li><span>• Thread & Weave Errors:</span> Broken warp ends, floats, and slubs.</li>
            <li><span>• Reed Lines & Dents:</span> Friction lines caused by damaged loom reeds.</li>
            <li><span>• Broken Stitches:</span> Splicing failures during continuous weaving.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- ADVANTAGES OF OUR WEBPAGE SECTION -->
  <section class="advantages" id="advantages">
    <div class="con">
      <div class="sec-head">
        <h2>Advantages of Selvedge AI Platform</h2>
        <p>Why modern textile mills rely on our intelligent automated inspection workspace</p>
      </div>

      <div class="adv-grid">
        <div class="adv-card">
          <div class="adv-ic">⚡</div>
          <h3>Sub-8ms Real-Time Inference</h3>
          <p>Ultra-low latency single-pass YOLOv8 and PyTorch models enable real-time defect detection without slowing down high-speed automated loom rollers.</p>
        </div>
        <div class="adv-card">
          <div class="adv-ic">📊</div>
          <h3>ASTM D5430 Compliance</h3>
          <p>Automated 4-Point System penalty point calculations assign Grade A (Pass), Grade B (Warning), or Grade C (Reject) standard status for every roll frame.</p>
        </div>
        <div class="adv-card">
          <div class="adv-ic">🎯</div>
          <h3>Multi-Model Neural Hybrid</h3>
          <p>Combines object detection bounding boxes with deep classification neural networks to eliminate false alarms and guarantee high accuracy.</p>
        </div>
        <div class="adv-card">
          <div class="adv-ic">📷</div>
          <h3>Live Camera Stream Integration</h3>
          <p>Supports continuous IP/USB webcam video streaming with snapshot capture and live anomaly alerts directly inside your web browser.</p>
        </div>
        <div class="adv-card">
          <div class="adv-ic">📥</div>
          <h3>One-Click Audit Ledger Export</h3>
          <p>Generates downloadable CSV reports and high-resolution annotated frame snapshots for factory quality management and client compliance verification.</p>
        </div>
        <div class="adv-card">
          <div class="adv-ic">🌐</div>
          <h3>Zero Installation Web App</h3>
          <p>Runs natively on standard modern web browsers with interactive 3D visual effects, responsive controls, and secure operator authentication.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- WHAT FEATURES WE PROVIDE SECTION -->
  <section class="features-sec" id="features">
    <div class="con">
      <div class="sec-head">
        <h2>What Features We Provide</h2>
        <p>Comprehensive end-to-end tools designed for operators, quality managers, and loom engineers</p>
      </div>

      <div class="feat-grid">
        <div class="feat-card">
          <div class="num">FEATURE 01</div>
          <h3>Interactive AI Surface Inspector</h3>
          <p>Upload any fabric image or select sample swatches to view color-coded bounding boxes, confidence scores, and adjustable threshold sliders.</p>
        </div>
        <div class="feat-card">
          <div class="num">FEATURE 02</div>
          <h3>Continuous Live Stream & Audio Alert</h3>
          <p>Stream live loom video feeds with real-time laser scan beams and audible chime alerts upon defect detection.</p>
        </div>
        <div class="feat-card">
          <div class="num">FEATURE 03</div>
          <h3>ASTM D5430 Audit Classification Ledger</h3>
          <p>View detailed defect logs with unique IDs, coordinates, severity tags (Minor, Major, Critical), penalty points, and loom remediation actions.</p>
        </div>
        <div class="feat-card">
          <div class="num">FEATURE 04</div>
          <h3>Live Weave Anomaly Waveform</h3>
          <p>Monitor real-time pixel variance waveforms and signal telemetry graphs to detect subtle weave texture irregularities.</p>
        </div>
        <div class="feat-card">
          <div class="num">FEATURE 05</div>
          <h3>Operator Account Portal & Slide-Out Drawer</h3>
          <p>Seamless left slide-out navigation drawer with user login modal, subscription plan selection, and technical neural specs.</p>
        </div>
        <div class="feat-card">
          <div class="num">FEATURE 06</div>
          <h3>One-Click Frame & CSV Report Export</h3>
          <p>Export complete inspection histories to CSV spreadsheet format and download full-resolution image frame snapshots instantaneously.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- REPORT SECTION -->
  <section class="rep-sec" id="report">
    <div class="con">
      <div class="rep-grid">
        <div class="gbox">
          <div class="gr grA" id="gring">A</div>
          <h3 id="rg2">Grade A Compliance</h3>
          <p id="rs">0 defects detected. Roll is compliant for shipment.</p>
          <button class="btn bgh" style="width:100%" onclick="expCSV()">📥 Export Audit Ledger (.CSV)</button>
        </div>

        <div class="tbl-card">
          <div class="tbl-h">
            <h3>ASTM D5430 Defect Classification Ledger</h3>
            <span style="font-family:var(--fc);font-size:10px;color:var(--dim)">4-POINT SYSTEM</span>
          </div>
          <div style="overflow-x:auto">
            <table>
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Category</th>
                  <th>Severity</th>
                  <th>BBox</th>
                  <th>Confidence</th>
                  <th>ASTM Pts</th>
                  <th>Remediation Action</th>
                  <th>Inspect</th>
                </tr>
              </thead>
              <tbody id="rtb">
                <tr><td colspan="8" style="text-align:center;color:var(--green);padding:20px;font-family:var(--fc);font-size:12px">✅ No defects detected — Fabric surface meets Grade A standard</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </section>
</div>

<!-- LOGIN MODAL -->
<div class="mo" id="login-modal" onclick="if(event.target===this)closeModal('login-modal')">
  <div class="mb">
    <div class="mh">
      <span>Operator Account Sign In</span>
      <button onclick="closeModal('login-modal')" style="color:var(--dim);font-size:16px;background:none;border:none;cursor:pointer">✕</button>
    </div>
    <form onsubmit="event.preventDefault();alert('Signed in successfully!');closeModal('login-modal')">
      <div class="form-grp">
        <label>Operator Email / ID</label>
        <input type="email" placeholder="operator@textilemill.com" required>
      </div>
      <div class="form-grp">
        <label>Password</label>
        <input type="password" placeholder="••••••••" required>
      </div>
      <button class="btn bg" style="width:100%;padding:12px;margin-top:10px" type="submit">Sign In to Dashboard</button>
    </form>
  </div>
</div>

<!-- SUBSCRIPTION MODAL -->
<div class="mo" id="sub-modal" onclick="if(event.target===this)closeModal('sub-modal')">
  <div class="mb">
    <div class="mh">
      <span>Mill Subscription Plans</span>
      <button onclick="closeModal('sub-modal')" style="color:var(--dim);font-size:16px;background:none;border:none;cursor:pointer">✕</button>
    </div>
    <div class="sub-grid">
      <div class="sub-card">
        <h4>Starter Mill</h4>
        <div class="price">$49/mo</div>
        <p>10,000 scans / mo<br>ASTM D5430 grading<br>Email reports</p>
        <button class="btn bgh" style="width:100%" onclick="alert('Subscribed to Starter Tier!')">Select Tier</button>
      </div>
      <div class="sub-card pop">
        <h4>Pro Loom</h4>
        <div class="price">$149/mo</div>
        <p>Unlimited scans<br>Live webcam stream<br>&lt;8ms latency</p>
        <button class="btn bg" style="width:100%" onclick="alert('Subscribed to Pro Tier!')">Select Tier</button>
      </div>
    </div>
  </div>
</div>

<!-- ABOUT MODAL -->
<div class="mo" id="about-modal" onclick="if(event.target===this)closeModal('about-modal')">
  <div class="mb">
    <div class="mh">
      <span>About Selvedge AI</span>
      <button onclick="closeModal('about-modal')" style="color:var(--dim);font-size:16px;background:none;border:none;cursor:pointer">✕</button>
    </div>
    <div style="font-size:13px;color:var(--dim);line-height:1.7">
      <p style="margin-bottom:10px">Selvedge AI is a world-class industrial fabric defect inspection platform designed for textile mills and automated looms.</p>
      <p style="margin-bottom:10px">Combining YOLOv8 object detection and ResNet stain classification, the platform evaluates every fabric millimeter against the ASTM D5430 4-point grading system with sub-10ms latency.</p>
    </div>
  </div>
</div>

<footer>
  <div class="fi">
    <p>SELVEDGE AI — Industrial Fabric Inspection Platform</p>
    <p>ASTM D5430 · Multi-Model Neural Inspection · &lt; 8ms Latency</p>
  </div>
</footer>

<script>
let report=null,conf=0.20,wcStr=null,stInt=null,frc=0,aCtx=null;

function toggleDrawer(){
  document.getElementById('drawer-overlay').classList.toggle('open');
}
function closeDrawer(){
  document.getElementById('drawer-overlay').classList.remove('open');
}

function openLoginModal(){closeDrawer();document.getElementById('login-modal').classList.add('open');}
function openSubModal(){closeDrawer();document.getElementById('sub-modal').classList.add('open');}
function openAboutModal(){closeDrawer();document.getElementById('about-modal').classList.add('open');}
function closeModal(id){document.getElementById(id).classList.remove('open');}

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

    const bgGrad=ctx.createLinearGradient(0,0,w,h);
    bgGrad.addColorStop(0,'#FBF8F3');
    bgGrad.addColorStop(0.4,'#F4EFE6');
    bgGrad.addColorStop(1,'#EBE3D5');
    ctx.fillStyle=bgGrad;ctx.fillRect(0,0,w,h);

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

let sigT=0;
function drawSig(){
  const cv=document.getElementById('sig-cv');if(!cv)return;
  cv.width=cv.offsetWidth;cv.height=60;
  const ctx=cv.getContext('2d');const W=cv.width,H=cv.height;
  ctx.clearRect(0,0,W,H);
  
  ctx.beginPath();ctx.moveTo(0,H/2);
  const cnt=report?.defect_count||0;
  for(let x=0;x<=W;x+=6){
    const amp=cnt>0?Math.sin(x*0.05+sigT)*18+Math.random()*10:Math.sin(x*0.03+sigT)*4;
    ctx.lineTo(x,H/2+amp);
  }
  ctx.strokeStyle=cnt>0?'#DC2626':'#059669';
  ctx.lineWidth=1.5;ctx.stroke();
  sigT+=0.08;requestAnimationFrame(drawSig);
}
drawSig();

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

const PRESETS = {
  'clean': '/test_clean.jpg',
  'stain': '/ref_stain.jpg',
  'thread': '/ref_thread_error.jpg',
  'hole': '/ref_hole.jpg',
  'oil': '/ref_oil_spot.png',
  'stitch': '/ref_broken_stitch.jpg',
  'lines': '/ref_lines.jpg'
};

addEventListener('load',()=>{
  lp(null,'clean');
});

function switchMode(m){
  document.getElementById('tab-upload').classList.toggle('active',m==='upload');
  document.getElementById('tab-cam').classList.toggle('active',m==='cam');
  if(m==='cam') startWebcam(); else stopWebcam();
}

function onTh(v){conf=parseFloat(v);document.getElementById('tv').textContent=parseFloat(v).toFixed(2);}

function startWebcam(){
  if(!navigator.mediaDevices?.getUserMedia){alert('Webcam not supported by your browser.');return;}
  navigator.mediaDevices.getUserMedia({video:{width:1280,height:720}}).then(s=>{
    wcStr=s;const v=document.getElementById('wv');v.srcObject=s;v.play();
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

function lp(e,type){
  stopWebcam();
  document.querySelectorAll('.pchip').forEach(b=>b.classList.remove('act'));
  if(e?.target)e.target.classList.add('act');
  
  const src = PRESETS[type] || PRESETS['clean'];
  const img = document.getElementById('ins-img');
  
  img.crossOrigin = "anonymous";
  img.onload = function() {
    document.getElementById('ir').textContent = (img.naturalWidth || 800) + 'x' + (img.naturalHeight || 600);
    fetch(img.src)
      .then(res => res.blob())
      .then(blob => sendP(blob))
      .catch(() => {
        const cv = document.createElement('canvas');
        cv.width = img.naturalWidth || 800;
        cv.height = img.naturalHeight || 600;
        const ctx = cv.getContext('2d');
        ctx.drawImage(img, 0, 0);
        cv.toBlob(b => sendP(b), 'image/jpeg');
      });
  };
  img.src = src + '?t=' + Date.now();
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
    tb.innerHTML='<tr><td colspan="8" style="text-align:center;color:var(--green);padding:20px;font-family:var(--fc);font-size:12px">✅ No defects detected — Fabric surface meets Grade A standard</td></tr>';
  }else{
    tb.innerHTML=d.defects.map((df,i)=>{
      const bb=df.bbox?`[${df.bbox.join(', ')}]`:'Global';
      const sc=df.severity==='Critical'?'tag-c':df.severity==='Major'?'tag-m':'tag-n';
      const cw=(df.confidence*100).toFixed(0);
      const cc=df.confidence>.85?'#059669':df.confidence>.65?'#D97706':'#C2410C';
      return '<tr><td style="font-family:var(--fc);font-weight:700">'+(df.id||'DEF-'+(i+1).toString().padStart(3,'0'))+'</td><td><strong>'+df.type+'</strong></td><td><span class="tag '+sc+'">'+(df.severity||'Minor')+'</span></td><td style="font-family:var(--fc);font-size:11px">'+bb+'</td><td><div class="cb"><div class="cbb"><div class="cbf" style="width:'+cw+'%;background:'+cc+'"></div></div><span style="font-family:var(--fc);font-size:11px;color:'+cc+';font-weight:700;min-width:40px">'+cw+'%</span></div></td><td style="font-family:var(--fc);font-weight:700">'+(df.astm_points||1)+'pt</td><td style="font-size:12px;color:var(--dim)">'+df.action+'</td><td><button onclick="openM('+i+')" style="background:transparent;border:1px solid var(--border);color:var(--terracotta);font-size:11px;padding:3px 8px;border-radius:4px;cursor:pointer">🔍</button></td></tr>';
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

addEventListener('resize',drawOv);
</script>
</body>
</html>
"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)

print(f"DONE: {len(HTML)} bytes written to {OUT}")
