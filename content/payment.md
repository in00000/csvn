{{- $title := .Title -}}
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{ $title }} · CSVN — Corporate Services Vendor Network</title>
<meta name="description" content="{{ .Description }}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{{ .Permalink }}">

<!-- Open Graph -->
<meta property="og:title" content="{{ $title }} · CSVN">
<meta property="og:description" content="{{ .Description }}">
<meta property="og:url" content="{{ .Permalink }}">
<meta property="og:type" content="website">

<!-- Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

<!-- jsPDF for invoice generation -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>

<!-- Structured data -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "CSVN Standard Listing",
  "description": "12-month listing on CSVN — Corporate Services Vendor Network",
  "offers": {
    "@type": "Offer",
    "price": "999",
    "priceCurrency": "INR",
    "availability": "https://schema.org/InStock"
  }
}
</script>

<style>
/* ============================================================
   CSVN Payment Page — Hugo Layout
   ============================================================ */
:root{
  --brand:#4f46e5;--brand-dark:#3730a3;--brand-light:#eef2ff;--brand-soft:#e0e7ff;
  --success:#10b981;--success-dark:#059669;--success-bg:#f0fdf4;--success-border:#86efac;
  --danger:#ef4444;--danger-bg:#fef2f2;
  --ink:#0f172a;--ink-2:#1e293b;--ink-3:#334155;
  --muted:#64748b;--muted-2:#94a3b8;
  --line:#e2e8f0;--line-2:#f1f5f9;--bg:#f8fafc;--white:#fff;
  --ease:cubic-bezier(.4,0,.2,1);
  --ease-out:cubic-bezier(0,0,.2,1);
  --ease-spring:cubic-bezier(.34,1.56,.64,1);
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{
  font-family:'Inter',-apple-system,BlinkMacSystemFont,system-ui,sans-serif;
  background:var(--bg);color:var(--ink-2);line-height:1.6;
  font-feature-settings:'cv02','cv03','cv04','cv11';
  -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;
  padding-bottom:60px;overflow-x:hidden;
}
.container{max-width:920px;margin:0 auto;padding:0 20px}
button,input,select,textarea{font:inherit;color:inherit}
button{cursor:pointer;border:none;background:none}
img{max-width:100%;display:block}

/* Progress bar */
.progress-bar{position:fixed;top:0;left:0;right:0;height:3px;z-index:200;
  background:linear-gradient(90deg,var(--brand),#8b5cf6,#a855f7);
  transform:scaleX(0);transform-origin:left;
  transition:transform .4s var(--ease-out);
  box-shadow:0 0 12px rgba(79,70,229,.5);pointer-events:none}
.progress-bar.active{transform:scaleX(1)}

/* Header */
.top-bar{position:sticky;top:0;z-index:100;
  background:rgba(255,255,255,.85);
  backdrop-filter:saturate(180%) blur(16px);
  -webkit-backdrop-filter:saturate(180%) blur(16px);
  border-bottom:1px solid rgba(226,232,240,.7);
  padding:14px 0;transition:box-shadow .2s var(--ease)}
.top-bar.scrolled{box-shadow:0 1px 12px rgba(15,23,42,.05)}
.top-bar-inner{display:flex;align-items:center;justify-content:space-between;gap:16px}
.brand{display:flex;align-items:center;gap:11px;font-weight:800;font-size:17px;color:var(--ink);text-decoration:none;letter-spacing:-.02em}
.brand img{height:38px;width:auto;display:block}
.brand-text{display:flex;flex-direction:column;line-height:1.15}
.brand-sub{font-size:10.5px;color:var(--muted);font-weight:500;letter-spacing:.01em}
.back-link{font-size:12px;font-weight:700;color:var(--brand);text-decoration:none;padding:6px 12px;border-radius:8px;transition:background .15s ease;margin-right:8px}
.back-link:hover{background:var(--brand-light)}
.secure-badge{display:inline-flex;align-items:center;gap:7px;
  background:var(--success-bg);color:#047857;border:1px solid var(--success-border);
  padding:6px 12px;border-radius:100px;font-size:11px;font-weight:700}
.secure-badge::before{content:'';width:6px;height:6px;border-radius:50%;
  background:var(--success);box-shadow:0 0 0 3px rgba(16,185,129,.2);
  animation:pulse 2s ease-in-out infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.4}}

/* Hero */
.hero{margin-top:28px;
  background:linear-gradient(135deg,#1e1b4b 0%,#4f46e5 50%,#7c3aed 100%);
  border-radius:24px;padding:36px 32px;color:#fff;
  position:relative;overflow:hidden;
  box-shadow:0 24px 48px -16px rgba(79,70,229,.45);isolation:isolate}
.hero::before{content:'';position:absolute;top:-60%;right:-25%;width:520px;height:520px;border-radius:50%;
  background:radial-gradient(circle,rgba(255,255,255,.18) 0%,transparent 65%);pointer-events:none;z-index:-1}
.hero-label{display:inline-flex;align-items:center;gap:6px;
  font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;
  background:rgba(255,255,255,.14);padding:6px 12px;border-radius:100px;
  backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,.18)}
.hero h1{font-size:clamp(24px,4vw,34px);font-weight:900;letter-spacing:-.03em;margin:16px 0 8px;line-height:1.1;color:#fff}
.hero-sub{font-size:14px;opacity:.85;max-width:520px}
.hero-amount{font-size:clamp(44px,8vw,68px);font-weight:900;letter-spacing:-.045em;margin-top:22px;line-height:1;color:#fff}
.hero-amount small{font-size:15px;font-weight:600;opacity:.7;display:block;margin-top:8px;letter-spacing:0}
.hero-meta{display:flex;gap:20px;flex-wrap:wrap;margin-top:26px;font-size:12px;opacity:.9;font-weight:500}
.hero-meta span{display:inline-flex;align-items:center;gap:6px}

/* Steps */
.steps{display:flex;gap:6px;margin:28px 0 20px;background:var(--white);padding:8px;
  border-radius:14px;border:1px solid var(--line);box-shadow:0 1px 3px rgba(15,23,42,.06);
  overflow-x:auto;scrollbar-width:none}
.steps::-webkit-scrollbar{display:none}
.step{flex:1;min-width:130px;display:flex;align-items:center;gap:10px;
  padding:10px 14px;border-radius:10px;font-size:12px;font-weight:600;
  color:var(--muted);cursor:pointer;transition:all .25s var(--ease);
  white-space:nowrap;user-select:none}
.step:hover{background:var(--line-2)}
.step.active{background:var(--brand-light);color:var(--brand);font-weight:700}
.step.done{color:var(--ink-3)}
.step-num{width:24px;height:24px;border-radius:50%;background:var(--line);
  color:var(--muted);display:flex;align-items:center;justify-content:center;
  font-size:11px;font-weight:800;flex-shrink:0;transition:all .3s var(--ease)}
.step.active .step-num{background:var(--brand);color:#fff;transform:scale(1.05)}
.step.done .step-num{background:var(--success);color:#fff}
.step.done .step-num::before{content:'✓';font-size:13px;font-weight:900}
.step.done .step-num span{display:none}

/* Cards */
.card{background:var(--white);border:1px solid var(--line);
  border-radius:16px;padding:28px;box-shadow:0 1px 3px rgba(15,23,42,.06);
  margin-bottom:16px}
.card.animating-out{opacity:0;transform:translateY(-8px);pointer-events:none;transition:all .18s var(--ease)}
.card.animating-in{animation:cardIn .4s var(--ease-out)}
@keyframes cardIn{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}
.card-title{font-size:16px;font-weight:800;color:var(--ink);
  letter-spacing:-.02em;margin-bottom:6px;display:flex;align-items:center;gap:10px}
.card-title .badge{display:inline-flex;align-items:center;justify-content:center;
  width:26px;height:26px;border-radius:8px;background:var(--brand-light);
  color:var(--brand);font-size:12px;font-weight:800;flex-shrink:0}
.card-desc{font-size:13px;color:var(--muted);margin-bottom:18px;line-height:1.6}

/* Form */
.form-grid{display:grid;gap:14px}
.form-row{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.field label{display:block;font-size:12px;font-weight:700;color:var(--ink);margin-bottom:6px}
.field label .req{color:var(--danger);margin-left:2px}
.field label .opt{color:var(--muted);font-weight:500;font-size:11px}
.field input,.field select{width:100%;padding:12px 14px;
  border:1.5px solid var(--line);border-radius:10px;font-size:14px;
  font-family:inherit;color:var(--ink);background:var(--white);
  transition:all .15s var(--ease);outline:none;-webkit-appearance:none;appearance:none}
.field select{background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath fill='%2364748b' d='M6 8L0 0h12z'/%3E%3C/svg%3E");
  background-repeat:no-repeat;background-position:right 14px center;
  background-size:10px;padding-right:36px}
.field input:focus,.field select:focus{border-color:var(--brand);box-shadow:0 0 0 4px rgba(79,70,229,.12)}
.field input.error,.field select.error{border-color:var(--danger);box-shadow:0 0 0 4px rgba(239,68,68,.1)}
.field input[readonly]{background:var(--line-2);color:var(--muted);cursor:not-allowed}
.field-hint{font-size:11px;color:var(--muted);margin-top:6px;line-height:1.5}
.field-error{font-size:11.5px;color:var(--danger);margin-top:6px;font-weight:600;display:none}
.field-error.show{display:block}

/* Buttons */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;
  padding:12px 22px;border-radius:10px;font-size:13.5px;font-weight:700;
  font-family:inherit;cursor:pointer;border:none;transition:all .2s var(--ease);
  text-decoration:none;white-space:nowrap;position:relative;overflow:hidden}
.btn:disabled{opacity:.55;cursor:not-allowed;transform:none!important}
.btn-primary{background:linear-gradient(135deg,var(--brand) 0%,#6366f1 100%);color:#fff;
  box-shadow:0 6px 16px -4px rgba(79,70,229,.4)}
.btn-primary:hover:not(:disabled){transform:translateY(-2px);box-shadow:0 12px 24px -8px rgba(79,70,229,.5)}
.btn-ghost{background:var(--white);color:var(--ink);border:1.5px solid var(--line)}
.btn-ghost:hover:not(:disabled){border-color:var(--brand);color:var(--brand);transform:translateY(-1px)}
.btn-block{width:100%}
.btn-row{display:flex;gap:10px;flex-wrap:wrap;justify-content:center}
.btn svg{width:14px;height:14px;flex-shrink:0}
.btn.loading{pointer-events:none;color:transparent}
.btn.loading::after{content:'';position:absolute;width:16px;height:16px;
  border:2px solid rgba(255,255,255,.3);border-top-color:#fff;border-radius:50%;
  animation:spin .7s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}

/* Payee */
.payee-box{background:linear-gradient(135deg,#f0fdf4 0%,#ecfdf5 100%);
  border:1.5px solid var(--success-border);border-radius:12px;padding:18px;margin-bottom:16px}
.payee-head{display:flex;align-items:center;gap:9px;margin-bottom:12px}
.payee-check{width:22px;height:22px;border-radius:50%;background:var(--success);
  color:#fff;display:flex;align-items:center;justify-content:center;
  font-size:12px;font-weight:900;flex-shrink:0}
.payee-title{font-size:12px;font-weight:800;color:#065f46;letter-spacing:.05em;text-transform:uppercase}
.payee-row{display:flex;justify-content:space-between;align-items:center;
  padding:9px 0;border-bottom:1px solid #d1fae5;font-size:13px;gap:12px}
.payee-row:last-child{border-bottom:0}
.payee-row .lbl{color:#047857;font-weight:500;flex-shrink:0}
.payee-row .val{color:#065f46;font-weight:800;text-align:right;word-break:break-all}
.payee-row .val.mono{font-family:ui-monospace,Monaco,Menlo,monospace;font-size:12px}

/* QR */
.qr-wrap{text-align:center;padding:26px 16px;
  background:linear-gradient(135deg,#fafbff 0%,#f5f3ff 100%);
  border-radius:12px;border:1.5px dashed var(--brand-soft);margin-bottom:16px}
.qr-wrap img{width:220px;height:220px;background:#fff;padding:12px;
  border-radius:14px;box-shadow:0 8px 24px -6px rgba(79,70,229,.18);
  display:inline-block;transition:transform .3s var(--ease-spring)}
.qr-wrap img:hover{transform:scale(1.04)}
.qr-hint{font-size:12px;color:var(--muted);margin-top:14px;font-weight:500}
.upi-apps{display:inline-flex;align-items:center;gap:8px;background:#fff;
  border:1px solid var(--line);padding:8px 14px;border-radius:100px;
  font-size:11px;font-weight:700;color:var(--muted);margin-top:14px}
.upi-apps .dot{width:6px;height:6px;border-radius:50%;background:var(--success)}

/* UPI box */
.upi-box{display:flex;align-items:center;gap:10px;background:var(--line-2);
  border:1.5px solid var(--line);border-radius:10px;padding:10px 12px;margin-bottom:14px}
.upi-box code{flex:1;font-family:ui-monospace,Monaco,Menlo,monospace;
  font-size:12px;font-weight:700;color:var(--brand);background:transparent;
  word-break:break-all;padding:6px 2px}
.copy-btn{background:var(--brand);color:#fff;border:none;padding:8px 14px;
  border-radius:8px;font-size:11px;font-weight:800;cursor:pointer;
  font-family:inherit;transition:all .18s var(--ease);flex-shrink:0;white-space:nowrap}
.copy-btn:hover{background:var(--brand-dark)}
.copy-btn.copied{background:var(--success)}

/* Upload */
.file-upload{border:2px dashed var(--line);border-radius:12px;padding:26px 16px;
  text-align:center;cursor:pointer;transition:all .2s var(--ease);
  background:var(--line-2);display:block}
.file-upload:hover{border-color:var(--brand);background:var(--brand-light)}
.file-upload input{display:none}
.file-upload svg{width:32px;height:32px;color:var(--muted);margin:0 auto 8px}
.file-upload .fu-title{font-size:13px;font-weight:700;color:var(--ink);margin-bottom:4px}
.file-upload .fu-desc{font-size:11px;color:var(--muted)}
.file-preview{display:none;margin-top:12px;padding:12px;background:#fff;
  border:1px solid var(--line);border-radius:10px;align-items:center;gap:12px}
.file-preview.show{display:flex}
.file-preview img{width:52px;height:52px;object-fit:cover;border-radius:8px;border:1px solid var(--line)}
.file-preview .info{flex:1;min-width:0}
.file-preview .name{font-size:12px;font-weight:700;color:var(--ink);
  overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.file-preview .size{font-size:11px;color:var(--muted);margin-top:2px}
.file-preview .remove{background:none;border:none;color:var(--danger);
  font-size:11.5px;font-weight:700;cursor:pointer;font-family:inherit;
  padding:7px 11px;border-radius:6px}
.file-preview .remove:hover{background:var(--danger-bg)}

/* Summary */
.summary-box{background:var(--line-2);border:1px solid var(--line);
  border-radius:12px;padding:18px;margin-bottom:18px}
.summary-box h4{font-size:11.5px;font-weight:800;color:var(--muted);
  text-transform:uppercase;letter-spacing:.06em;margin-bottom:12px;
  display:flex;align-items:center;justify-content:space-between}
.summary-box h4 .edit-link{font-size:11px;font-weight:700;color:var(--brand);
  text-transform:none;letter-spacing:0;cursor:pointer;text-decoration:none}
.summary-box h4 .edit-link:hover{text-decoration:underline}
.summary-row{display:flex;justify-content:space-between;padding:8px 0;
  font-size:13px;gap:12px;border-bottom:1px solid var(--line)}
.summary-row:last-child{border-bottom:0}
.summary-row .k{color:var(--muted);font-weight:500;flex-shrink:0}
.summary-row .v{color:var(--ink);font-weight:700;text-align:right;word-break:break-word}
.summary-row.total{border-top:2px solid var(--line);border-bottom:0;
  padding-top:14px;margin-top:8px}
.summary-row.total .k{color:var(--ink);font-weight:800;font-size:14px}
.summary-row.total .v{color:var(--brand);font-size:18px;font-weight:900}

/* Success */
.success-state{display:none;text-align:center;padding:32px 16px}
.success-state.show{display:block;animation:cardIn .5s var(--ease-out)}
.success-icon{width:72px;height:72px;border-radius:50%;
  background:linear-gradient(135deg,var(--success) 0%,var(--success-dark) 100%);
  color:#fff;display:inline-flex;align-items:center;justify-content:center;
  margin-bottom:20px;box-shadow:0 16px 32px -8px rgba(16,185,129,.5);
  animation:pop .6s var(--ease-spring)}
@keyframes pop{0%{transform:scale(0);opacity:0}60%{transform:scale(1.15)}100%{transform:scale(1);opacity:1}}
.success-icon svg{width:34px;height:34px;stroke-width:3}
.success-state h3{font-size:22px;font-weight:900;color:var(--ink);
  margin-bottom:10px;letter-spacing:-.025em}
.success-state p{font-size:14px;color:var(--muted);max-width:460px;margin:0 auto 20px;line-height:1.65}
.success-ref{display:inline-block;background:var(--brand-light);
  border:1px dashed var(--brand-soft);padding:10px 16px;border-radius:10px;
  font-family:ui-monospace,Monaco,monospace;font-size:12.5px;font-weight:800;
  color:var(--brand);margin-bottom:22px}

/* Info */
.info-banner{background:linear-gradient(135deg,var(--brand-light) 0%,#f5f3ff 100%);
  border:1px solid var(--brand-soft);border-radius:12px;padding:14px 16px;
  margin-bottom:16px;display:flex;gap:11px;align-items:flex-start}
.info-banner svg{width:18px;height:18px;color:var(--brand);flex-shrink:0;margin-top:1px}
.info-banner p{font-size:12.5px;color:#3730a3;line-height:1.65}

/* Trust */
.trust-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));
  gap:12px;margin-top:8px}
.trust-item{background:var(--white);border:1px solid var(--line);
  border-radius:12px;padding:16px;display:flex;gap:12px;align-items:flex-start;
  transition:all .2s var(--ease)}
.trust-item:hover{border-color:var(--brand-soft);transform:translateY(-2px);
  box-shadow:0 4px 12px rgba(15,23,42,.06)}
.trust-item .ti-icon{width:38px;height:38px;border-radius:10px;
  background:var(--brand-light);color:var(--brand);display:flex;
  align-items:center;justify-content:center;flex-shrink:0;
  font-weight:900;font-size:13px}
.trust-item .ti-title{font-size:13px;font-weight:800;color:var(--ink);margin-bottom:3px}
.trust-item .ti-desc{font-size:11.5px;color:var(--muted);line-height:1.55}

/* Warn */
.warn-box{background:var(--danger-bg);border:1.5px solid #fecaca;
  border-radius:12px;padding:16px;margin-top:14px}
.warn-box h4{font-size:13px;font-weight:800;color:#991b1b;
  margin-bottom:10px;display:flex;align-items:center;gap:8px}
.warn-box h4 svg{width:16px;height:16px;flex-shrink:0}
.warn-list{list-style:none;padding:0;display:grid;gap:6px}
.warn-list li{font-size:12px;color:#7f1d1d;padding-left:18px;position:relative;line-height:1.6}
.warn-list li::before{content:'✗';position:absolute;left:0;top:0;color:var(--danger);font-weight:900;font-size:12px}

/* FAQ */
.faq-item{border-bottom:1px solid var(--line);padding:16px 0;cursor:pointer}
.faq-item:last-child{border-bottom:0}
.faq-q{display:flex;justify-content:space-between;align-items:center;gap:16px;
  font-size:14px;font-weight:700;color:var(--ink)}
.faq-q svg{width:16px;height:16px;color:var(--muted);transition:transform .3s var(--ease);flex-shrink:0}
.faq-item.open .faq-q svg{transform:rotate(180deg);color:var(--brand)}
.faq-a{max-height:0;overflow:hidden;
  transition:max-height .35s var(--ease),padding .35s var(--ease);
  font-size:13px;color:var(--muted);line-height:1.7}
.faq-item.open .faq-a{max-height:500px;padding-top:10px}

/* Toast */
.toast-container{position:fixed;bottom:24px;left:50%;transform:translateX(-50%);
  z-index:1000;display:flex;flex-direction:column;gap:8px;
  pointer-events:none;align-items:center}
.toast{background:var(--ink);color:#fff;padding:12px 18px;border-radius:11px;
  font-size:13px;font-weight:600;box-shadow:0 20px 40px -12px rgba(15,23,42,.15);
  display:flex;align-items:center;gap:10px;animation:toastIn .35s var(--ease-spring);
  pointer-events:auto;max-width:calc(100vw - 32px)}
.toast.success{background:linear-gradient(135deg,var(--success) 0%,var(--success-dark) 100%)}
.toast.error{background:linear-gradient(135deg,var(--danger) 0%,#dc2626 100%)}
.toast svg{width:16px;height:16px;flex-shrink:0}
@keyframes toastIn{from{opacity:0;transform:translateY(20px) scale(.95)}to{opacity:1;transform:translateY(0) scale(1)}}

/* Footer */
.foot{text-align:center;font-size:12px;color:var(--muted);
  padding:36px 16px 8px;line-height:1.7}
.foot strong{color:var(--ink);font-weight:800}
.foot a{color:var(--brand);text-decoration:none;font-weight:700}
.foot a:hover{text-decoration:underline}

/* Mobile */
@media (max-width:600px){
  .container{padding:0 14px}
  .hero{padding:28px 22px;border-radius:20px}
  .hero-amount{font-size:44px}
  .card{padding:20px;border-radius:14px}
  .qr-wrap img{width:190px;height:190px}
  .form-row{grid-template-columns:1fr}
  .btn-row .btn{flex:1 1 calc(50% - 5px);min-width:0}
  .step{min-width:auto;padding:9px 11px;font-size:11px}
  .step .step-label{display:none}
  .step.active .step-label{display:inline}
  .secure-badge span{display:none}
  .payee-row{font-size:12px}
}

@media print{
  .top-bar,.steps,.btn,.secure-badge,.trust-grid,.foot,.faq-item,.info-banner,.progress-bar{display:none!important}
  body{background:#fff;padding:0}
  .card{box-shadow:none;border:1px solid #ccc;page-break-inside:avoid}
}

@media (prefers-reduced-motion:reduce){
  *,*::before,*::after{animation-duration:.01ms!important;transition-duration:.01ms!important}
}
</style>
</head>
<body>

<div class="progress-bar" id="progressBar"></div>

<!-- Header -->
<div class="top-bar" id="topBar">
  <div class="container">
    <div class="top-bar-inner">
      <a href="/" class="brand">
        <img src="/logo.png" alt="CSVN — Corporate Services Vendor Network">
      </a>
      <div style="display:flex;align-items:center;gap:8px">
        <a href="/" class="back-link">← Back to CSVN</a>
        <div class="secure-badge"><span>Secure UPI Payment</span></div>
      </div>
    </div>
  </div>
</div>

<div class="container">

  <!-- Hero -->
  <div class="hero">
    <span class="hero-label">Complete Your Listing</span>
    <h1>CSVN Standard Listing</h1>
    <p class="hero-sub">Get your business listed on India's verified B2B vendor network with priority placement and unlimited customer inquiries for 12 months.</p>
    <div class="hero-amount">
      ₹999
      <small>One-time payment · 12 months validity</small>
    </div>
    <div class="hero-meta">
      <span>✓ Instant activation</span>
      <span>✓ GST invoice</span>
      <span>✓ 7-day refund</span>
    </div>
  </div>

  <!-- Steps -->
  <div class="steps" id="stepsBar">
    <div class="step active" data-step="1"><div class="step-num"><span>1</span></div><span class="step-label">Your Details</span></div>
    <div class="step" data-step="2"><div class="step-num"><span>2</span></div><span class="step-label">Pay ₹999</span></div>
    <div class="step" data-step="3"><div class="step-num"><span>3</span></div><span class="step-label">Generate Invoice</span></div>
    <div class="step" data-step="4"><div class="step-num"><span>4</span></div><span class="step-label">Confirmation</span></div>
  </div>

  <!-- STEP 1 -->
  <div class="card" id="section-1">
    <div class="card-title"><span class="badge">1</span>Tell Us About Your Business</div>
    <p class="card-desc">We'll use these details to prepare your invoice and activate your listing. All information is kept confidential.</p>

    <div class="info-banner">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
      <p>Please enter details exactly as you want them to appear on your invoice and public listing. You'll be able to review everything in Step 3.</p>
    </div>

    <form id="businessForm" onsubmit="submitBusinessDetails(event)" novalidate>
      <div class="form-grid">

        <div class="field">
          <label for="bizName">Business Name <span class="req">*</span></label>
          <input type="text" id="bizName" placeholder="e.g. Shree Ganesh Electricals Pvt Ltd" required>
          <div class="field-error" id="err-bizName">Please enter your business name (min. 2 characters)</div>
        </div>

        <div class="field">
          <label for="contactName">Account Holder / Contact Person <span class="req">*</span></label>
          <input type="text" id="contactName" placeholder="e.g. Rahul Sharma" required>
          <div class="field-error" id="err-contactName">Please enter the account holder name</div>
        </div>

        <div class="form-row">
          <div class="field">
            <label for="email">Email Address <span class="req">*</span></label>
            <input type="email" id="email" placeholder="you@business.com" required>
            <div class="field-hint">Your invoice and confirmation will be emailed here.</div>
            <div class="field-error" id="err-email">Please enter a valid email address</div>
          </div>

          <div class="field">
            <label for="phone">WhatsApp Number <span class="req">*</span></label>
            <input type="tel" id="phone" placeholder="10-digit mobile number" maxlength="10" inputmode="numeric" required>
            <div class="field-error" id="err-phone">Please enter a valid 10-digit mobile number</div>
          </div>
        </div>

        <div class="form-row">
          <div class="field">
            <label for="category">Business Category <span class="req">*</span></label>
            <select id="category" required>
              <option value="">Select your category</option>
              <option>Accounting &amp; Taxation</option>
              <option>Legal &amp; Compliance</option>
              <option>IT &amp; Software Services</option>
              <option>Marketing &amp; Advertising</option>
              <option>HR &amp; Recruitment</option>
              <option>Logistics &amp; Supply Chain</option>
              <option>Manufacturing &amp; Industrial</option>
              <option>Real Estate &amp; Construction</option>
              <option>Financial Services</option>
              <option>Consulting &amp; Advisory</option>
              <option>Other Corporate Services</option>
            </select>
            <div class="field-error" id="err-category">Please select a category</div>
          </div>

          <div class="field">
            <label for="city">City / Area <span class="req">*</span></label>
            <input type="text" id="city" placeholder="e.g. Pimpri-Chinchwad, Pune" required>
            <div class="field-error" id="err-city">Please enter your city</div>
          </div>
        </div>

        <div class="form-row">
          <div class="field">
            <label for="website">Business Website <span class="opt">(optional)</span></label>
            <input type="url" id="website" placeholder="https://yourbusiness.com">
          </div>

          <div class="field">
            <label for="gst">GST Number <span class="opt">(optional)</span></label>
            <input type="text" id="gst" placeholder="27ABCDE1234F1Z5" maxlength="15" style="text-transform:uppercase">
          </div>
        </div>

      </div>

      <button type="submit" class="btn btn-primary btn-block" style="margin-top:22px">
        Continue to Payment →
      </button>
    </form>
  </div>

  <!-- STEP 2 -->
  <div class="card" id="section-2" style="display:none">
    <div class="card-title"><span class="badge">2</span>Pay ₹999 via UPI</div>
    <p class="card-desc">Scan the QR code with any UPI app, or pay directly to our verified UPI ID. Complete the payment, then continue to Step 3.</p>

    <div class="payee-box">
      <div class="payee-head">
        <div class="payee-check">✓</div>
        <div class="payee-title">Verified Payee — Confirm Before Paying</div>
      </div>
      <div class="payee-row"><span class="lbl">Account Holder</span><span class="val">Sachin Ambekar</span></div>
      <div class="payee-row"><span class="lbl">Business Name</span><span class="val">CSVN — Corporate Services Vendor Network</span></div>
      <div class="payee-row"><span class="lbl">Payment Gateway</span><span class="val">BharatPe (Yes Bank)</span></div>
      <div class="payee-row"><span class="lbl">UPI ID</span><span class="val mono">BHARATPE09B9S1M8C3G33183@yesbankltd</span></div>
    </div>

    <p style="font-size:13px;color:var(--muted);margin-bottom:16px">
      When you scan the QR or paste the UPI ID, your app will display the payee as <strong style="color:var(--ink)">Sachin Ambekar</strong>. This is the only correct account for CSVN payments.
    </p>

    <div class="qr-wrap">
      <img id="qrImage" src="/qr.png" alt="CSVN Payment QR Code" loading="lazy">
      <div class="qr-hint">Scan with any UPI app</div>
      <div class="upi-apps"><span class="dot"></span>PhonePe · GPay · Paytm · BHIM</div>
      <div class="btn-row" style="margin-top:16px">
        <button type="button" class="btn btn-ghost" onclick="downloadQR(this)">↓ Download QR</button>
        <a class="btn btn-primary" id="upiLinkBtn" href="#" style="display:none">Open UPI App</a>
      </div>
    </div>

    <p style="font-size:11.5px;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:.06em;margin-bottom:8px">Or pay to this UPI ID</p>
    <div class="upi-box">
      <code>BHARATPE09B9S1M8C3G33183@yesbankltd</code>
      <button type="button" class="copy-btn" onclick="copyText('BHARATPE09B9S1M8C3G33183@yesbankltd',this)">Copy</button>
    </div>

    <p style="font-size:11.5px;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:.06em;margin:18px 0 8px">Amount to pay</p>
    <div class="upi-box">
      <code style="color:var(--success)">₹999.00</code>
      <button type="button" class="copy-btn" onclick="copyText('999',this)">Copy</button>
    </div>

    <div class="info-banner" style="margin-top:16px">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
      <p>After completing the payment, keep your UPI app open — you'll need the <strong>UTR / Transaction ID</strong> for the next step.</p>
    </div>

    <button type="button" class="btn btn-primary btn-block" style="margin-top:18px" onclick="nextStep(3)">
      I've Paid · Continue to Invoice →
    </button>
  </div>

  <!-- STEP 3 -->
  <div class="card" id="section-3" style="display:none">
    <div class="card-title"><span class="badge">3</span>Confirm Payment &amp; Generate Invoice</div>
    <p class="card-desc">Enter your UPI Transaction ID (UTR) and upload a screenshot of your payment. We'll generate your invoice instantly.</p>

    <div class="summary-box">
      <h4>Your Business Details <a class="edit-link" onclick="editStep1()">Edit →</a></h4>
      <div class="summary-row"><span class="k">Business Name</span><span class="v" id="sum-biz">—</span></div>
      <div class="summary-row"><span class="k">Account Holder</span><span class="v" id="sum-name">—</span></div>
      <div class="summary-row"><span class="k">Email</span><span class="v" id="sum-email">—</span></div>
      <div class="summary-row"><span class="k">WhatsApp</span><span class="v" id="sum-phone">—</span></div>
      <div class="summary-row"><span class="k">Category</span><span class="v" id="sum-category">—</span></div>
      <div class="summary-row"><span class="k">City</span><span class="v" id="sum-city">—</span></div>
      <div class="summary-row total"><span class="k">Amount</span><span class="v">₹999.00</span></div>
    </div>

    <form id="paymentForm" onsubmit="submitPaymentDetails(event)" novalidate>
      <div class="form-grid">

        <div class="field">
          <label for="utr">UPI Transaction ID / UTR <span class="req">*</span></label>
          <input type="text" id="utr" placeholder="12-digit reference from your UPI app" maxlength="20" inputmode="numeric" required>
          <div class="field-hint">Find this in your UPI app → tap the payment → copy the Transaction ID.</div>
          <div class="field-error" id="err-utr">Please enter a valid UTR (8–20 characters)</div>
        </div>

        <div class="field">
          <label>Payment Screenshot <span class="req">*</span></label>
          <label class="file-upload" id="fileUpload" for="screenshot">
            <input type="file" id="screenshot" accept="image/*" onchange="handleFile(this)">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
            <div class="fu-title">Click to upload or drag &amp; drop</div>
            <div class="fu-desc">PNG, JPG up to 5 MB</div>
          </label>
          <div class="file-preview" id="filePreview">
            <img id="fileThumb" src="" alt="">
            <div class="info">
              <div class="name" id="fileName"></div>
              <div class="size" id="fileSize"></div>
            </div>
            <button type="button" class="remove" onclick="removeFile()">Remove</button>
          </div>
          <div class="field-error" id="err-screenshot">Please attach a payment screenshot</div>
        </div>

      </div>

      <button type="submit" class="btn btn-primary btn-block" style="margin-top:22px" id="submitBtn">
        Confirm Payment · Generate Invoice
      </button>
    </form>

    <div class="success-state" id="successState">
      <div class="success-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
      </div>
      <h3>Invoice Generated Successfully</h3>
      <p>We've received your payment details. A confirmation email with your invoice has been sent to both you and our team. We'll verify the UTR and activate your listing within 24 business hours.</p>
      <div class="success-ref" id="successRef">Invoice: CSVN-XXXX-XXXX</div>
      <div class="btn-row" style="margin-bottom:16px">
        <button type="button" class="btn btn-primary" onclick="downloadInvoice(this)" id="downloadBtn">↓ Download Invoice (PDF)</button>
        <button type="button" class="btn btn-ghost" onclick="window.print()">Print</button>
        <button type="button" class="btn btn-ghost" onclick="resetForm()">New Payment</button>
      </div>
      <p style="font-size:12px;color:var(--muted)">
        Questions? Email <a href="mailto:info@csvn.in" style="color:var(--brand);font-weight:700">info@csvn.in</a> or WhatsApp <a href="tel:+918793932827" style="color:var(--brand);font-weight:700">+91 87939 32827</a>
      </p>
    </div>
  </div>

  <!-- STEP 4 -->
  <div class="card" id="section-4" style="display:none">
    <div class="card-title"><span class="badge">4</span>What Happens Next</div>
    <p class="card-desc">Your payment confirmation has reached our team. Here's our verification and activation timeline.</p>

    <div style="display:grid;gap:10px">
      <div class="trust-item"><div class="ti-icon">1</div><div><div class="ti-title">Payment Verification</div><div class="ti-desc">We match your UTR against our bank statement. Typically within <strong>4 business hours</strong>.</div></div></div>
      <div class="trust-item"><div class="ti-icon">2</div><div><div class="ti-title">Business Details Confirmation</div><div class="ti-desc">We verify your business name, address, and category. Within <strong>1 business day</strong>.</div></div></div>
      <div class="trust-item"><div class="ti-icon">3</div><div><div class="ti-title">Listing Goes Live</div><div class="ti-desc">Your business appears on CSVN with priority placement. Within <strong>24 hours</strong>.</div></div></div>
      <div class="trust-item"><div class="ti-icon">4</div><div><div class="ti-title">GST Invoice Email</div><div class="ti-desc">A GST-compliant invoice is emailed to you. Sent the <strong>same day</strong> as activation.</div></div></div>
    </div>
  </div>

  <!-- TRUST -->
  <div class="card">
    <div class="card-title">Your Payment Is Protected</div>
    <p class="card-desc">We follow strict verification practices to keep your money and data safe.</p>

    <div class="trust-grid">
      <div class="trust-item"><div class="ti-icon">🔒</div><div><div class="ti-title">Verified Payee</div><div class="ti-desc">Registered under Sachin Ambekar via BharatPe.</div></div></div>
      <div class="trust-item"><div class="ti-icon">✓</div><div><div class="ti-title">7-Day Refund</div><div class="ti-desc">Full refund if no inquiries received.</div></div></div>
      <div class="trust-item"><div class="ti-icon">⏱</div><div><div class="ti-title">24-Hour Activation</div><div class="ti-desc">Your listing goes live the same day.</div></div></div>
      <div class="trust-item"><div class="ti-icon">✉</div><div><div class="ti-title">GST Invoice</div><div class="ti-desc">Emailed automatically after activation.</div></div></div>
    </div>

    <div class="warn-box">
      <h4>
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
        We will NEVER ask you for:
      </h4>
      <ul class="warn-list">
        <li>Your UPI PIN, OTP, CVV, or bank password</li>
        <li>Payment to any UPI ID other than the one on this page</li>
        <li>Payment via gift cards, crypto, or unusual methods</li>
        <li>Payment requests over WhatsApp or social media DMs</li>
      </ul>
      <p style="font-size:12px;color:#7f1d1d;margin-top:12px;line-height:1.6">
        If anyone contacts you claiming to be from CSVN and asks for something different, report it to <a href="mailto:report@csvn.in" style="color:#991b1b;font-weight:800">report@csvn.in</a> immediately.
      </p>
    </div>
  </div>

  <!-- FAQ -->
  <div class="card">
    <div class="card-title">Frequently Asked Questions</div>

    <div class="faq-item" onclick="toggleFaq(this)">
      <div class="faq-q">What if I paid but didn't receive a confirmation?<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></div>
      <div class="faq-a">Email us at info@csvn.in with your UTR and business name. We'll verify manually and confirm within 2 business hours.</div>
    </div>
    <div class="faq-item" onclick="toggleFaq(this)">
      <div class="faq-q">Can I pay from a different UPI app?<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></div>
      <div class="faq-a">Yes. Any UPI app works — PhonePe, Google Pay, Paytm, BHIM, Amazon Pay, WhatsApp Pay, or your bank's app. Just make sure the payee name shows "Sachin Ambekar".</div>
    </div>
    <div class="faq-item" onclick="toggleFaq(this)">
      <div class="faq-q">Is the payment refundable?<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></div>
      <div class="faq-a">Yes — full refund within 7 days if you haven't received any customer inquiries, partial refund between 8–15 days, no refund after 15 days. See our full <a href="/refund/" style="color:var(--brand);font-weight:700">Refund Policy</a>.</div>
    </div>
    <div class="faq-item" onclick="toggleFaq(this)">
      <div class="faq-q">How long does activation take?<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></div>
      <div class="faq-a">Typically within 24 hours of receiving your payment confirmation. You'll get an email with your listing URL and invoice as soon as it's live.</div>
    </div>
    <div class="faq-item" onclick="toggleFaq(this)">
      <div class="faq-q">Do I get a GST invoice?<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></div>
      <div class="faq-a">Yes. A GST-compliant invoice is emailed to the address you provide, on the same day your listing is activated.</div>
    </div>
  </div>

  <div class="foot">
    <p><strong>CSVN</strong> — Corporate Services Vendor Network</p>
    <p style="margin-top:6px">Owned and operated by Sachin Ambekar · Nigdi, Pimpri-Chinchwad, Pune</p>
    <p style="margin-top:12px">
      <a href="mailto:info@csvn.in">info@csvn.in</a> ·
      <a href="tel:+918793932827">+91 87939 32827</a> ·
      Mon–Sat, 10 AM – 6 PM IST
    </p>
    <p style="margin-top:16px;font-size:11px;color:var(--muted-2)">
      <a href="/terms/">Terms</a> · <a href="/privacy/">Privacy</a> · <a href="/refund/">Refund</a> · <a href="/disclaimer/">Disclaimer</a> · <a href="/grievance-officer/">Grievance</a>
    </p>
  </div>

</div>

<div class="toast-container" id="toastContainer"></div>

<script>
/* ============================================================
   CSVN Payment System — Hugo Layout
   Admin email: pcmcdiary@gmail.com
   ============================================================ */
(function(){
  'use strict';

  const CONFIG = {
    brandName: 'CSVN — Corporate Services Vendor Network',
    ownerName: 'Sachin Ambekar',
    upiId: 'BHARATPE09B9S1M8C3G33183@yesbankltd',
    payeeName: 'Sachin Ambekar',
    amount: 999,
    qrUrl: '/qr.png',
    supportEmail: 'info@csvn.in',
    supportPhone: '+91 87939 32827',
    product: 'CSVN Standard Listing — 12 Months',
    adminEndpoint: 'https://formsubmit.co/ajax/pcmcdiary@gmail.com'
  };

  const STORAGE_KEY = 'csvn_payment_v1';
  let state = { step:1, form:{}, hasScreenshot:false, submittedRef:null, receiptData:null };

  function saveState(){
    try{ localStorage.setItem(STORAGE_KEY, JSON.stringify({
      step:state.step, form:state.form,
      submittedRef:state.submittedRef, receiptData:state.receiptData
    })); }catch(e){}
  }
  function loadState(){
    try{
      const raw = localStorage.getItem(STORAGE_KEY);
      if(!raw) return;
      Object.assign(state, JSON.parse(raw));
    }catch(e){}
  }

  /* Progress bar */
  const progressBar = document.getElementById('progressBar');
  let progressTimer = null;
  function showProgress(){
    progressBar.classList.add('active');
    progressBar.style.transform = 'scaleX(0.15)';
    clearTimeout(progressTimer);
    progressTimer = setTimeout(()=>{ progressBar.style.transform='scaleX(0.7)'; }, 150);
  }
  function hideProgress(){
    clearTimeout(progressTimer);
    progressBar.style.transform = 'scaleX(1)';
    setTimeout(()=>{
      progressBar.classList.remove('active');
      setTimeout(()=>{ progressBar.style.transform='scaleX(0)'; }, 300);
    }, 250);
  }

  /* Step navigation */
  function showStep(n){
    state.step = Math.max(1, Math.min(4, n));
    saveState();
    for(let i=1;i<=4;i++){
      const el = document.getElementById('section-'+i);
      if(!el) continue;
      if(i===3 && document.getElementById('successState').classList.contains('show')){
        el.style.display='block';
      } else {
        el.style.display = (i===state.step)?'block':'none';
      }
    }
    document.querySelectorAll('.step').forEach(el=>{
      const s = parseInt(el.dataset.step);
      el.classList.toggle('active', s===state.step);
      el.classList.toggle('done', s<state.step);
    });
    requestAnimationFrame(()=>requestAnimationFrame(scrollToActiveSection));
  }

  function scrollToActiveSection(){
    let target = document.getElementById('section-'+state.step);
    if(state.step===3 && document.getElementById('successState').classList.contains('show')){
      target = document.getElementById('successState');
    }
    if(!target) return;
    const rect = target.getBoundingClientRect();
    const topBar = document.getElementById('topBar');
    const offset = (topBar ? topBar.offsetHeight : 64) + 20;
    if(rect.top >= offset && rect.top <= window.innerHeight/2) return;
    const y = rect.top + window.pageYOffset - offset;
    window.scrollTo({top: Math.max(0,y), behavior:'smooth'});
  }

  function nextStep(n){
    const current = document.getElementById('section-'+state.step);
    if(current){
      current.classList.add('animating-out');
      setTimeout(()=>{
        current.classList.remove('animating-out');
        showStep(n);
        if(n===3) refreshSummary();
        const next = document.getElementById('section-'+n);
        if(next){
          next.classList.add('animating-in');
          setTimeout(()=>next.classList.remove('animating-in'), 500);
        }
      }, 180);
    } else {
      showStep(n);
      if(n===3) refreshSummary();
    }
  }
  window.nextStep = nextStep;

  document.querySelectorAll('.step').forEach(el=>{
    el.addEventListener('click', ()=>{
      const n = parseInt(el.dataset.step);
      if(n>1 && !state.form.bizName){ showToast('Please complete Step 1 first','error'); return; }
      showStep(n);
      if(n===3) refreshSummary();
    });
  });

  /* Field helpers */
  function showFieldError(id, show){
    const err = document.getElementById('err-'+id);
    const inp = document.getElementById(id);
    if(err) err.classList.toggle('show', show);
    if(inp) inp.classList.toggle('error', show);
  }
  function isFieldValid(id, v){
    switch(id){
      case 'bizName': case 'contactName': case 'city': return v.length>=2;
      case 'email': return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v);
      case 'phone': return /^\d{10}$/.test(v);
      case 'category': return v.length>0;
      default: return true;
    }
  }

  /* Step 1 */
  ['bizName','contactName','email','phone','category','city','website','gst'].forEach(id=>{
    const el = document.getElementById(id);
    if(!el) return;
    const handler = ()=>{ state.form[id]=el.value; saveState(); if(el.classList.contains('error')) showFieldError(id,false); };
    el.addEventListener('input', handler);
    el.addEventListener('change', handler);
  });

  window.submitBusinessDetails = function(e){
    e.preventDefault();
    let ok = true;
    ['bizName','contactName','email','phone','category','city'].forEach(id=>{
      const el = document.getElementById(id);
      const v = el ? el.value.trim() : '';
      if(!isFieldValid(id,v)){ showFieldError(id,true); ok=false; } else showFieldError(id,false);
    });
    if(!ok){ showToast('Please fix the highlighted fields','error'); return; }
    ['bizName','contactName','email','phone','category','city','website','gst'].forEach(id=>{
      const el = document.getElementById(id);
      if(el) state.form[id]=el.value;
    });
    saveState();
    const btn = e.target.querySelector('button[type="submit"]');
    btn.classList.add('loading');
    showProgress();
    setTimeout(()=>{
      btn.classList.remove('loading');
      hideProgress();
      showToast('Business details saved','success');
      nextStep(2);
    }, 350);
  };

  /* Summary */
  function refreshSummary(){
    const f = state.form;
    document.getElementById('sum-biz').textContent = f.bizName || '—';
    document.getElementById('sum-name').textContent = f.contactName || '—';
    document.getElementById('sum-email').textContent = f.email || '—';
    document.getElementById('sum-phone').textContent = f.phone ? '+91 '+f.phone : '—';
    document.getElementById('sum-category').textContent = f.category || '—';
    document.getElementById('sum-city').textContent = f.city || '—';
  }
  window.editStep1 = function(){ showStep(1); };

  /* File upload */
  const MAX_SIZE = 5*1024*1024;
  window.handleFile = function(input){
    const file = input.files && input.files[0];
    if(!file) return;
    if(file.size > MAX_SIZE){ showToast('File too large. Max 5 MB.','error'); input.value=''; return; }
    if(!file.type.startsWith('image/')){ showToast('Please upload an image file','error'); input.value=''; return; }
    const reader = new FileReader();
    reader.onload = e=>{
      document.getElementById('fileThumb').src = e.target.result;
      document.getElementById('fileName').textContent = file.name;
      document.getElementById('fileSize').textContent = (file.size/1024).toFixed(1)+' KB';
      document.getElementById('filePreview').classList.add('show');
      document.getElementById('fileUpload').style.display='none';
      showFieldError('screenshot', false);
      state.hasScreenshot = true;
      saveState();
    };
    reader.readAsDataURL(file);
  };
  window.removeFile = function(){
    document.getElementById('screenshot').value = '';
    document.getElementById('filePreview').classList.remove('show');
    document.getElementById('fileUpload').style.display = 'block';
    state.hasScreenshot = false;
    saveState();
  };

  const uploadLabel = document.getElementById('fileUpload');
  ['dragenter','dragover'].forEach(ev=>{
    uploadLabel.addEventListener(ev, e=>{ e.preventDefault(); uploadLabel.style.borderColor='var(--brand)'; uploadLabel.style.background='var(--brand-light)'; });
  });
  ['dragleave','drop'].forEach(ev=>{
    uploadLabel.addEventListener(ev, e=>{ e.preventDefault(); uploadLabel.style.borderColor=''; uploadLabel.style.background=''; });
  });
  uploadLabel.addEventListener('drop', e=>{
    const files = e.dataTransfer.files;
    if(files.length){
      document.getElementById('screenshot').files = files;
      window.handleFile(document.getElementById('screenshot'));
    }
  });

  /* Submit payment */
  window.submitPaymentDetails = async function(e){
    e.preventDefault();
    const utr = document.getElementById('utr').value.trim();
    if(utr.length<8 || utr.length>20){ showFieldError('utr',true); showToast('Please enter a valid UTR','error'); return; }
    showFieldError('utr',false);
    if(!state.hasScreenshot){ showFieldError('screenshot',true); showToast('Please attach the payment screenshot','error'); return; }
    showFieldError('screenshot',false);

    const btn = document.getElementById('submitBtn');
    btn.classList.add('loading');
    showProgress();

    const ref = 'CSVN-'+Date.now().toString(36).toUpperCase().slice(-6)+'-'+Math.random().toString(36).slice(2,6).toUpperCase();
    state.submittedRef = ref;
    const f = state.form;
    state.receiptData = {
      ref,
      business: f.bizName || '', name: f.contactName || '',
      email: f.email || '', phone: f.phone || '',
      category: f.category || '', city: f.city || '',
      website: f.website || '', gst: f.gst || '',
      utr, amount: CONFIG.amount,
      paidAt: new Date().toISOString()
    };
    saveState();

    try {
      await sendEmails(state.receiptData);
      showToast('Invoice generated & emailed','success');
    } catch(err){
      console.error('Email failed:', err);
      showToast('Invoice generated (email may be delayed)','info');
    }

    document.getElementById('paymentForm').style.display='none';
    document.getElementById('successRef').textContent = 'Invoice: '+ref;
    document.getElementById('successState').classList.add('show');
    document.getElementById('section-4').style.display='block';

    document.querySelectorAll('.step').forEach(el=>{
      const s = parseInt(el.dataset.step);
      el.classList.toggle('done', s<=3);
      el.classList.toggle('active', s===4);
    });

    state.step = 3;
    saveState();
    btn.classList.remove('loading');
    hideProgress();

    requestAnimationFrame(()=>requestAnimationFrame(scrollToActiveSection));
  };

  /* Emails */
  async function sendEmails(d){
    const dateStr = new Date(d.paidAt).toLocaleString('en-IN',{dateStyle:'medium',timeStyle:'short'});

    // JSON snippet for quick copy into data/clients/real-XX.json
    const jsonSnippet = JSON.stringify({
      id: d.ref.toLowerCase().replace(/[^a-z0-9]/g,'-'),
      name: d.business,
      phone: d.phone,
      city: d.city,
      category: (d.category||'').toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,''),
      tier: 'Standard',
      order: 999,
      website: d.website || '',
      gst: d.gst || '',
      email: d.email
    }, null, 2);

    const payload = {
      _subject: `🟡 PENDING VERIFICATION — ${d.business} (₹${d.amount}) — UTR: ${d.utr} | CSVN`,
      _template: 'table',
      _captcha: 'false',
      _replyto: d.email,
      _cc: d.email,
      'Invoice No.': d.ref,
      'Business Name': d.business,
      'Account Holder': d.name,
      'Email': d.email,
      'WhatsApp': '+91 '+d.phone,
      'Category': d.category,
      'City': d.city,
      'Website': d.website || '—',
      'GST Number': d.gst || '—',
      'Amount Paid': 'Rs. '+d.amount,
      'UPI / UTR': d.utr,
      'Payment Date': dateStr,
      'Status': '⚠ PENDING VERIFICATION',
      'Next Action': '1) Verify UTR against BharatPe. 2) Paste JSON below into data/clients/real-XX.json. 3) Push to GitHub.',
      '--- JSON for data/clients/ ---': jsonSnippet
    };

    const res = await fetch(CONFIG.adminEndpoint, {
      method: 'POST',
      headers: {'Content-Type':'application/json','Accept':'application/json'},
      body: JSON.stringify(payload)
    });
    if(!res.ok) throw new Error('Email failed: '+res.status);
  }

  /* Invoice PDF */
  window.downloadInvoice = function(btn){
    const d = state.receiptData;
    if(!d){ showToast('No invoice data available','error'); return; }
    if(btn) btn.classList.add('loading');
    try{
      const { jsPDF } = window.jspdf;
      const doc = new jsPDF({unit:'mm',format:'a4'});
      const pageW = doc.internal.pageSize.getWidth();
      const pageH = doc.internal.pageSize.getHeight();
      const margin = 16;
      let y = 0;

      // Header
      doc.setFillColor(79,70,229);
      doc.rect(0,0,pageW,40,'F');
      doc.setTextColor(255,255,255);
      doc.setFont('helvetica','bold');
      doc.setFontSize(22);
      doc.text('CSVN', margin, 18);
      doc.setFont('helvetica','normal');
      doc.setFontSize(9);
      doc.text('Corporate Services Vendor Network', margin, 25);
      doc.text('Nigdi, Pimpri-Chinchwad, Pune, Maharashtra', margin, 30.5);
      doc.text('info@csvn.in  |  +91 87939 32827', margin, 36);
      doc.setFont('helvetica','bold');
      doc.setFontSize(16);
      doc.text('TAX INVOICE', pageW-margin, 20, {align:'right'});
      doc.setFontSize(9);
      doc.setFont('helvetica','normal');
      doc.text('Original for Recipient', pageW-margin, 27, {align:'right'});

      y = 56;

      // Invoice details
      doc.setTextColor(15,23,42);
      doc.setFont('helvetica','bold');
      doc.setFontSize(11);
      doc.text('Invoice Details', margin, y);
      y += 3;
      doc.setDrawColor(226,232,240);
      doc.line(margin, y, pageW-margin, y);
      y += 7;
      [
        ['Invoice No.', d.ref],
        ['Invoice Date', new Date(d.paidAt).toLocaleDateString('en-IN',{dateStyle:'medium'})],
        ['Payment Method', 'UPI / BharatPe (Yes Bank)'],
        ['Payment Status', 'Paid — Awaiting Verification']
      ].forEach(([k,v])=>{
        doc.setFont('helvetica','normal');
        doc.setTextColor(100,116,139);
        doc.text(k, margin, y);
        doc.setFont('helvetica','bold');
        doc.setTextColor(15,23,42);
        doc.text(String(v), margin+42, y);
        y += 7;
      });
      y += 6;

      // Billed to
      doc.setFont('helvetica','bold');
      doc.setFontSize(11);
      doc.setTextColor(15,23,42);
      doc.text('Billed To', margin, y);
      y += 3;
      doc.line(margin, y, pageW-margin, y);
      y += 7;
      const custRows = [
        ['Business Name', d.business],
        ['Account Holder', d.name],
        ['Email', d.email],
        ['Phone', '+91 '+d.phone],
        ['Category', d.category],
        ['City', d.city]
      ];
      if(d.gst) custRows.push(['GST Number', d.gst]);
      if(d.website) custRows.push(['Website', d.website]);
      doc.setFontSize(10);
      custRows.forEach(([k,v])=>{
        doc.setFont('helvetica','normal');
        doc.setTextColor(100,116,139);
        doc.text(k, margin, y);
        doc.setFont('helvetica','bold');
        doc.setTextColor(15,23,42);
        doc.text(String(v), margin+42, y);
        y += 7;
      });
      y += 6;

      // Services
      doc.setFont('helvetica','bold');
      doc.setFontSize(11);
      doc.text('Services', margin, y);
      y += 7;
      doc.setFillColor(238,242,255);
      doc.rect(margin, y-5, pageW-margin*2, 9, 'F');
      doc.setFontSize(9);
      doc.setTextColor(79,70,229);
      doc.text('DESCRIPTION', margin+3, y+1);
      doc.text('AMOUNT', pageW-margin-3, y+1, {align:'right'});
      y += 10;
      doc.setFont('helvetica','normal');
      doc.setFontSize(10);
      doc.setTextColor(15,23,42);
      doc.text(CONFIG.product, margin+3, y);
      doc.setFont('helvetica','bold');
      doc.text('Rs. '+d.amount+'.00', pageW-margin-3, y, {align:'right'});
      y += 9;
      doc.setDrawColor(226,232,240);
      doc.line(margin, y-2, pageW-margin, y-2);
      y += 6;

      // Total
      doc.setFillColor(79,70,229);
      doc.rect(margin, y-5, pageW-margin*2, 12, 'F');
      doc.setFontSize(12);
      doc.setTextColor(255,255,255);
      doc.text('TOTAL PAID', margin+3, y+3);
      doc.text('Rs. '+d.amount+'.00', pageW-margin-3, y+3, {align:'right'});
      y += 18;

      // UTR
      doc.setFillColor(240,253,244);
      doc.setDrawColor(134,239,172);
      doc.roundedRect(margin, y, pageW-margin*2, 22, 3, 3, 'FD');
      doc.setFont('helvetica','bold');
      doc.setFontSize(9);
      doc.setTextColor(6,95,70);
      doc.text('UPI TRANSACTION REFERENCE (UTR)', margin+6, y+8);
      doc.setFontSize(14);
      doc.text(d.utr, margin+6, y+16);
      y += 30;

      // Provisional disclaimer
      doc.setFillColor(255,251,235);
      doc.setDrawColor(252,211,77);
      doc.roundedRect(margin, y, pageW-margin*2, 30, 3, 3, 'FD');
      doc.setFont('helvetica','bold');
      doc.setFontSize(9);
      doc.setTextColor(146,64,14);
      doc.text('IMPORTANT — VALIDITY OF THIS INVOICE', margin+6, y+6);
      doc.setFont('helvetica','normal');
      doc.setFontSize(8.5);
      doc.setTextColor(120,53,15);
      [
        'This invoice is provisional in nature and becomes valid only upon successful verification of the',
        'UTR above against the CSVN bank statement. Until such verification is completed, this document',
        'does not constitute final proof of payment or confirmed activation of the requested listing.',
        'For verification status or queries, contact info@csvn.in within 24 business hours.'
      ].forEach((line,i)=>doc.text(line, margin+6, y+12+i*4.2));
      y += 38;

      // Terms
      doc.setFont('helvetica','bold');
      doc.setFontSize(9);
      doc.setTextColor(15,23,42);
      doc.text('Terms & Notes', margin, y);
      y += 5;
      doc.setFont('helvetica','normal');
      doc.setFontSize(8.5);
      doc.setTextColor(100,116,139);
      [
        '1. This is a computer-generated invoice. No physical signature is required.',
        '2. Listing activation occurs within 24 business hours of successful UTR verification.',
        '3. The listing is valid for a period of 12 months from the date of activation.',
        '4. Refunds are governed by the CSVN Refund Policy available at csvn.in/refund.',
        '5. This invoice is issued under the provisions of the CGST Act, 2017.',
        '6. Any dispute shall be subject to the exclusive jurisdiction of courts in Pune, Maharashtra.',
        '7. For queries, write to info@csvn.in or call +91 87939 32827 (Mon–Sat, 10 AM – 6 PM IST).'
      ].forEach(line=>{ doc.text(line, margin, y); y += 4.2; });

      // Footer
      y = pageH - 18;
      doc.setDrawColor(226,232,240);
      doc.line(margin, y-4, pageW-margin, y-4);
      doc.setFontSize(7.5);
      doc.setTextColor(148,163,184);
      doc.text(CONFIG.brandName+' | Owned and operated by '+CONFIG.ownerName, margin, y);
      doc.text('Generated '+new Date().toLocaleString('en-IN'), pageW-margin, y, {align:'right'});

      doc.save('CSVN-Invoice-'+d.ref+'.pdf');
      showToast('Invoice downloaded','success');
    } catch(err){
      console.error('PDF error:', err);
      showToast('Could not generate PDF. Please try again.','error');
    } finally {
      if(btn) btn.classList.remove('loading');
    }
  };

  /* Copy */
  window.copyText = function(text, btn){
    const done = ()=>{
      const orig = btn.textContent;
      btn.textContent = '✓ Copied';
      btn.classList.add('copied');
      showToast('Copied to clipboard','success');
      setTimeout(()=>{ btn.textContent = orig; btn.classList.remove('copied'); }, 1800);
    };
    if(navigator.clipboard && navigator.clipboard.writeText){
      navigator.clipboard.writeText(text).then(done).catch(()=>fallbackCopy(text, done));
    } else fallbackCopy(text, done);
  };
  function fallbackCopy(text, cb){
    const ta = document.createElement('textarea');
    ta.value = text; ta.style.position='fixed'; ta.style.opacity='0';
    document.body.appendChild(ta); ta.select();
    try{ document.execCommand('copy'); cb(); }catch(e){ showToast('Copy failed','error'); }
    document.body.removeChild(ta);
  }

  /* Download QR */
  window.downloadQR = function(btn){
    if(btn) btn.classList.add('loading');
    fetch(CONFIG.qrUrl, {mode:'cors'})
      .then(r=>r.blob())
      .then(blob=>{
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url; a.download = 'CSVN-Payment-QR.png';
        document.body.appendChild(a); a.click(); document.body.removeChild(a);
        URL.revokeObjectURL(url);
        showToast('QR downloaded','success');
      })
      .catch(()=>{ window.open(CONFIG.qrUrl,'_blank'); })
      .finally(()=>{ if(btn) btn.classList.remove('loading'); });
  };

  /* FAQ */
  window.toggleFaq = function(el){ el.classList.toggle('open'); };

  /* Toast */
  function showToast(msg, type){
    const icons = {
      success: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
      error: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>',
      info: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>'
    };
    const c = document.getElementById('toastContainer');
    while(c.children.length>=3) c.removeChild(c.firstChild);
    const t = document.createElement('div');
    t.className = 'toast '+(type||'info');
    t.innerHTML = (icons[type]||icons.info)+'<span>'+msg+'</span>';
    c.appendChild(t);
    setTimeout(()=>{
      t.style.transition='opacity .3s ease,transform .3s ease';
      t.style.opacity='0'; t.style.transform='translateY(20px)';
      setTimeout(()=>t.remove(),300);
    }, 2800);
  }

  /* Reset */
  window.resetForm = function(){
    if(!confirm('Clear this submission and start a new payment?')) return;
    localStorage.removeItem(STORAGE_KEY);
    location.reload();
  };

  /* UPI deep link */
  const isMobile = /Android|iPhone|iPad|iPod/i.test(navigator.userAgent);
  if(isMobile){
    const link = document.getElementById('upiLinkBtn');
    if(link){
      const params = new URLSearchParams({
        pa: CONFIG.upiId, pn: CONFIG.payeeName,
        am: CONFIG.amount.toFixed(2), cu: 'INR',
        tn: 'CSVN Listing'
      });
      link.href = 'upi://pay?'+params.toString();
      link.style.display = 'inline-flex';
    }
  }

  /* Scroll header */
  const topBar = document.getElementById('topBar');
  window.addEventListener('scroll', ()=>{
    if(window.scrollY > 10) topBar.classList.add('scrolled');
    else topBar.classList.remove('scrolled');
  }, {passive:true});

  /* Init */
  loadState();
  Object.entries(state.form).forEach(([k,v])=>{
    const el = document.getElementById(k);
    if(el && v) el.value = v;
  });
  if(state.submittedRef && state.receiptData){
    document.getElementById('successRef').textContent = 'Invoice: '+state.submittedRef;
    document.getElementById('successState').classList.add('show');
    document.getElementById('paymentForm').style.display='none';
    document.getElementById('section-4').style.display='block';
    showStep(3);
    document.querySelectorAll('.step').forEach(el=>{
      const s = parseInt(el.dataset.step);
      el.classList.toggle('done', s<=3);
    });
  } else {
    showStep(state.step || 1);
  }
})();
</script>
</body>
</html>
