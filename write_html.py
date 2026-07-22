import os

OUT = r"c:\Users\crist\OneDrive\Desktop\Fbric Defect detection\selvedge.html"

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SELVEDGE AI — Fabric Defect Inspection Platform</title>
<meta name="description" content="Clean, LeetCode-inspired industrial fabric defect detection workspace with real-time neural vision, ASTM D5430 grading, and live camera support.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&family=Syne:wght@700;800&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
:root{
  --void:#FAF7F2;--base:#F4EFE6;--panel:rgba(255,255,255,0.94);--lift:#EFE8DC;--lift2:#E5DDCF;
  --border:rgba(180,130,70,0.22);--border-b:rgba(194,65,12,0.35);
  --text:#1C1917;--dim:#57534E;--ghost:#78716C;
  --terracotta:#C2410C;--terracotta-g:rgba(194,65,12,0.14);
  --gold:#D97706;--gold-g:rgba(217,119,6,0.14);
  --green:#059669;--green-g:rgba(5,150,105,0.14);
  --red:#DC2626;--red-g:rgba(220,38,38,0.14);--yellow:#D97706;
  --fh:"Syne",sans-serif;--fb:"Outfit",sans-serif;--fc:"JetBrains Mono",monospace;
  --r1:10px;--r2:16px;--r3:20px
}
body{background:var(--void);color:var(--text);font-family:var(--fb);overflow-x:hidden;line-height:1.5}
#particles{position:fixed;inset:0;z-index:0;pointer-events:none}
.rel{position:relative;z-index:1}
.con{max-width:1380px;margin:0 auto;padding:0 24px}

/* CLEAN LEETCODE-STYLE NAV */
nav{position:fixed;top:0;left:0;right:0;z-index:999;
  background:rgba(250,247,242,.92);backdrop-filter:blur(20px) saturate(180%);
  border-bottom:1px solid var(--border);height:60px;display:flex;align-items:center}
.nav-i{max-width:1380px;margin:0 auto;padding:0 24px;
  display:flex;align-items:center;justify-content:space-between;width:100%}
.logo{display:flex;align-items:center;gap:10px;font-family:var(--fh);font-size:18px;font-weight:800;letter-spacing:1.5px;color:var(--text)}
.logo-ic{width:34px;height:34px;background:linear-gradient(135deg,var(--terracotta),var(--gold));
  border-radius:9px;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 14px var(--terracotta-g)}
.logo-ic svg{width:18px;height:18px;stroke:#fff;fill:none;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round}
.ai-t{background:linear-gradient(135deg,var(--terracotta),var(--gold));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.nav-links{display:flex;gap:24px;list-style:none}
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
  padding:8px 18px;border-radius:var(--r1);cursor:pointer;border:none;transition:all .2s;white-space:nowrap}
.bg{background:linear-gradient(135deg,var(--terracotta),#EA580C);color:#fff;box-shadow:0 4px 14px var(--terracotta-g)}
.bg:hover{transform:translateY(-1px);box-shadow:0 6px 18px var(--terracotta-g)}
.bgh{background:rgba(255,255,255,.9);color:var(--text);border:1px solid var(--border-b)}
.bgh:hover{color:var(--terracotta);border-color:var(--terracotta);background:var(--terracotta-g)}
.br{background:var(--red);color:#fff;box-shadow:0 4px 14px var(--red-g)}
.br:hover{transform:translateY(-1px)}
.bgr{background:linear-gradient(135deg,#059669,#10B981);color:#fff;box-shadow:0 4px 14px var(--green-g)}
.bgr:hover{transform:translateY(-1px)}

/* MAIN WORKSPACE HEADER */
.hdr{padding:84px 0 20px}
.hdr-flex{display:flex;justify-content:space-between;align-items:center}
.hdr-title h1{font-family:var(--fh);font-size:26px;font-weight:800;color:var(--text)}
.hdr-title p{font-size:13px;color:var(--dim);margin-top:2px}

/* STUDIO WORKBENCH GRID (LEETCODE 2-COLUMN STYLE) */
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

/* PRESETS GRID */
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

/* REPORT SECTION */
.rep-sec{padding:30px 0 60px}
.rep-grid{display:grid;grid-template-columns:300px 1fr;gap:20px;align-items:start}
.gbox{background:var(--panel);border:1px solid var(--border);border-radius:var(--r2);padding:24px;text-align:center;
  box-shadow:0 6px 24px rgba(0,0,0,0.03)}
.gr{width:80px;height:80px;border-radius:50%;margin:0 auto 14px;display:flex;align-items:center;
  justify-content:center;font-family:var(--fh);font-size:32px;font-weight:800;border:3px solid}
.grA{border-color:var(--green);color:var(--green);background:var(--green-g);box-shadow:0 0 24px var(--green-g)}
.grB{border-color:var(--yellow);color:var(--yellow);background:rgba(217,119,6,.15);box-shadow:0 0 24px rgba(217,119,6,.15)}
.grC{border-color:var(--red);color:var(--red);background:var(--red-g);box-shadow:0 0 24px var(--red-g)}
.gbox h3{font-size:17px;font-weight:700;margin-bottom:4px;color:var(--text)}
.gbox p{font-size:12px;color:var(--dim);line-height:1.4;margin-bottom:16px}

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

/* TECH SPECS MODAL */
.mo{position:fixed;inset:0;z-index:9999;background:rgba(28,25,23,.65);backdrop-filter:blur(16px);
  display:none;align-items:center;justify-content:center;padding:20px}
.mo.open{display:flex}
.mb{background:var(--panel);border:1px solid var(--border-b);border-radius:var(--r3);
  width:100%;max-width:500px;padding:24px;box-shadow:0 20px 60px rgba(0,0,0,.2)}
.mh{display:flex;justify-content:space-between;align-items:center;margin-bottom:16px}
.mh span{font-family:var(--fc);font-size:12px;font-weight:700;color:var(--terracotta)}

footer{border-top:1px solid var(--border);padding:24px 0;margin-top:40px;background:var(--base)}
.fi{max-width:1380px;margin:0 auto;padding:0 24px;display:flex;justify-content:space-between;
  align-items:center;font-size:11px;color:var(--ghost);font-family:var(--fc);font-weight:600}
</style>
</head>
<body>

<canvas id="particles"></canvas>

<div class="rel">
  <!-- LEETCODE-STYLE CLEAN NAVBAR -->
  <nav>
    <div class="nav-i">
      <div class="logo">
        <div class="logo-ic">
          <svg viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
        </div>
        <span>SELVEDGE <span class="ai-t">AI</span></span>
      </div>
      <ul class="nav-links">
        <li><a href="#studio">Inspector Workspace</a></li>
        <li><a href="#report">Audit Ledger</a></li>
        <li><a href="#tech" onclick="openTechModal()">Model Architecture</a></li>
      </ul>
      <div class="nav-cta">
        <div class="pill p-on" id="sys-pill"><span class="dot"></span>ONLINE</div>
        <button class="btn bg" onclick="document.getElementById('file-input').click()">📁 Upload Swatch</button>
      </div>
    </div>
  </nav>

  <!-- MAIN HEADER -->
  <header class="hdr">
    <div class="con">
      <div class="hdr-flex">
        <div class="hdr-title">
          <h1>Fabric Surface Inspector</h1>
          <p>ASTM D5430 Automated Quality Grading & Defect Detection</p>
        </div>
        <div style="display:flex;gap:10px">
          <span class="pill p-on" id="cam-pill"><span class="dot"></span>READY</span>
        </div>
      </div>
    </div>
  </header>

  <!-- STUDIO WORKBENCH (LEETCODE 2-COLUMN VIEWPORT) -->
  <section class="studio" id="studio">
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
              <div class="mode-tab active" id="tab-upload" onclick="switchMode('upload');document.getElementById('file-input').click()">📁 Upload File</div>
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

            <!-- REAL FABRIC PRESETS -->
            <div class="cg">
              <div class="cl"><span>Sample Defect Swatches</span></div>
              <div class="pgrid">
                <button class="pchip cln act" onclick="lp(event,'clean')">✨ Clean (Pass)</button>
                <button class="pchip" onclick="lp(event,'stain')">🛢️ Oil Stain</button>
                <button class="pchip" onclick="lp(event,'water')">💧 Water Stain</button>
                <button class="pchip" onclick="lp(event,'hole')">🕳️ Tear / Hole</button>
                <button class="pchip" onclick="lp(event,'slub')">🧶 Slub & Weave</button>
                <button class="pchip" onclick="lp(event,'sample')">🧵 Fabric Roll</button>
              </div>
            </div>

            <!-- TOGGLES -->
            <div class="cg">
              <div class="cl"><span>Overlay Options</span></div>
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
                <tr><td colspan="8" style="text-align:center;color:var(--green);padding:24px;font-family:var(--fc);font-size:12px">✅ No defects detected — Fabric surface meets Grade A standard</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </section>
</div>

<!-- TECH MODAL -->
<div class="mo" id="mo" onclick="if(event.target===this)this.classList.remove('open')">
  <div class="mb">
    <div class="mh">
      <span id="mt" style="font-family:var(--fh);font-size:16px;color:var(--text)">Neural Architecture Specs</span>
      <button onclick="document.getElementById('mo').classList.remove('open')" style="color:var(--dim);font-size:16px;background:none;border:none;cursor:pointer">✕</button>
    </div>
    <div style="font-size:13px;color:var(--dim);line-height:1.7" id="md">
      <p style="margin-bottom:10px"><strong>• YOLOv8 Defect Detector:</strong> Real-time single-pass object detection trained for fabric flaws (&lt; 8ms latency).</p>
      <p style="margin-bottom:10px"><strong>• ResNet-18 Stain Engine:</strong> Binary & multi-class classification for Oil vs. Water vs. Grease stains.</p>
      <p style="margin-bottom:10px"><strong>• Laplacian Texture Variance:</strong> High-precision surface anomaly thresholding compliant with ASTM D5430 standards.</p>
    </div>
  </div>
</div>

<footer>
  <div class="fi">
    <p>SELVEDGE AI — Industrial Fabric Inspection Workspace</p>
    <p>ASTM D5430 · Multi-Model Neural Inspection · &lt; 8ms Latency</p>
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

// REAL FABRIC SAMPLE PRESET MAP & PRESET LOADER
const PRESETS = {
  'clean': '/test_clean.jpg',
  'stain': '/test_oil.jpg',
  'water': '/test_water.jpg',
  'hole': '/test_hole.jpg',
  'slub': '/test_detected.jpg',
  'sample': '/sample.jpg'
};

addEventListener('load',()=>{
  lp(null,'clean');
});

function openTechModal(){
  document.getElementById('mo').classList.add('open');
}

function switchMode(m){
  document.getElementById('tab-upload').classList.toggle('active',m==='upload');
  document.getElementById('tab-cam').classList.toggle('active',m==='cam');
  if(m==='cam') startWebcam(); else stopWebcam();
}

function onTh(v){conf=parseFloat(v);document.getElementById('tv').textContent=parseFloat(v).toFixed(2);}

// WEBCAM
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

addEventListener('resize',drawOv);
</script>
</body>
</html>
"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)

print(f"DONE: {len(HTML)} bytes written to {OUT}")
