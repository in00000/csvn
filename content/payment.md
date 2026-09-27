---
title: "Payment"
description: "Pay ₹999 for your CSVN Standard listing via UPI. Instant invoice, 24-hour activation, verified payee."
layout: "page"
---

<style>
.csvn-wrap *{box-sizing:border-box}
.csvn-wrap{max-width:920px;margin:0 auto;font-family:'Inter',system-ui,-apple-system,sans-serif;color:#1e293b;line-height:1.6;-webkit-font-smoothing:antialiased}
.csvn-wrap .csvn-hero{margin-top:1.5rem;background:linear-gradient(135deg,#1e1b4b 0%,#4f46e5 55%,#7c3aed 100%);border-radius:24px;padding:36px 28px;color:#fff;position:relative;overflow:hidden;box-shadow:0 24px 48px -16px rgba(79,70,229,.45)}
.csvn-wrap .csvn-hero h1{font-size:clamp(24px,4vw,34px);font-weight:900;letter-spacing:-.03em;margin:16px 0 8px;line-height:1.1;color:#fff}
.csvn-wrap .csvn-hero-label{display:inline-block;font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;background:rgba(255,255,255,.15);padding:6px 12px;border-radius:100px;border:1px solid rgba(255,255,255,.15)}
.csvn-wrap .csvn-hero-sub{font-size:14px;opacity:.85;max-width:520px}
.csvn-wrap .csvn-hero-amt{font-size:clamp(44px,8vw,68px);font-weight:900;letter-spacing:-.045em;margin-top:22px;line-height:1;color:#fff}
.csvn-wrap .csvn-hero-amt small{font-size:15px;font-weight:600;opacity:.7;display:block;margin-top:8px;letter-spacing:0}
.csvn-wrap .csvn-hero-meta{display:flex;gap:18px;flex-wrap:wrap;margin-top:24px;font-size:12px;opacity:.9;font-weight:500}
.csvn-wrap .csvn-hero-meta span{display:inline-flex;align-items:center;gap:6px}
.csvn-wrap .csvn-steps{display:flex;gap:6px;margin:1.75rem 0 1.25rem;background:#fff;padding:8px;border-radius:14px;border:1px solid #e2e8f0;box-shadow:0 1px 3px rgba(15,23,42,.06);overflow-x:auto;scrollbar-width:none}
.csvn-wrap .csvn-steps::-webkit-scrollbar{display:none}
.csvn-wrap .csvn-step{flex:1;min-width:130px;display:flex;align-items:center;gap:10px;padding:10px 14px;border-radius:10px;font-size:12px;font-weight:600;color:#64748b;cursor:pointer;transition:all .25s ease;white-space:nowrap;user-select:none}
.csvn-wrap .csvn-step:hover{background:#f1f5f9}
.csvn-wrap .csvn-step.active{background:#eef2ff;color:#4f46e5;font-weight:700}
.csvn-wrap .csvn-step.done{color:#334155}
.csvn-wrap .csvn-step-num{width:24px;height:24px;border-radius:50%;background:#e2e8f0;color:#64748b;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:800;flex-shrink:0;transition:all .3s ease}
.csvn-wrap .csvn-step.active .csvn-step-num{background:#4f46e5;color:#fff}
.csvn-wrap .csvn-step.done .csvn-step-num{background:#10b981;color:#fff}
.csvn-wrap .csvn-step.done .csvn-step-num::before{content:'✓';font-size:13px;font-weight:900}
.csvn-wrap .csvn-step.done .csvn-step-num span{display:none}
.csvn-wrap .csvn-card{background:#fff;border:1px solid #e2e8f0;border-radius:16px;padding:26px;box-shadow:0 1px 3px rgba(15,23,42,.06);margin-bottom:16px}
.csvn-wrap .csvn-card-title{font-size:16px;font-weight:800;color:#0f172a;letter-spacing:-.015em;margin-bottom:6px;display:flex;align-items:center;gap:10px}
.csvn-wrap .csvn-badge{display:inline-flex;align-items:center;justify-content:center;width:26px;height:26px;border-radius:8px;background:#eef2ff;color:#4f46e5;font-size:12px;font-weight:800;flex-shrink:0}
.csvn-wrap .csvn-card-desc{font-size:13px;color:#64748b;margin-bottom:18px;line-height:1.6}
.csvn-wrap .csvn-form-grid{display:grid;gap:14px}
.csvn-wrap .csvn-form-row{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.csvn-wrap .csvn-field label{display:block;font-size:12px;font-weight:700;color:#0f172a;margin-bottom:6px}
.csvn-wrap .csvn-field label .req{color:#ef4444;margin-left:2px}
.csvn-wrap .csvn-field label .opt{color:#64748b;font-weight:500;font-size:11px}
.csvn-wrap .csvn-field input,.csvn-wrap .csvn-field select{width:100%;padding:12px 14px;border:1.5px solid #e2e8f0;border-radius:10px;font-size:14px;font-family:inherit;color:#0f172a;background:#fff;transition:all .15s ease;outline:none;-webkit-appearance:none;appearance:none}
.csvn-wrap .csvn-field select{background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath fill='%2364748b' d='M6 8L0 0h12z'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 14px center;background-size:10px;padding-right:36px}
.csvn-wrap .csvn-field input:focus,.csvn-wrap .csvn-field select:focus{border-color:#4f46e5;box-shadow:0 0 0 4px rgba(79,70,229,.12)}
.csvn-wrap .csvn-field input.error,.csvn-wrap .csvn-field select.error{border-color:#ef4444;box-shadow:0 0 0 4px rgba(239,68,68,.1)}
.csvn-wrap .csvn-hint{font-size:11px;color:#64748b;margin-top:6px;line-height:1.5}
.csvn-wrap .csvn-err{font-size:11.5px;color:#ef4444;margin-top:6px;font-weight:600;display:none}
.csvn-wrap .csvn-err.show{display:block}
.csvn-wrap .csvn-btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:12px 22px;border-radius:10px;font-size:13.5px;font-weight:700;font-family:inherit;cursor:pointer;border:none;transition:all .2s ease;text-decoration:none;white-space:nowrap;position:relative;overflow:hidden}
.csvn-wrap .csvn-btn:disabled{opacity:.55;cursor:not-allowed}
.csvn-wrap .csvn-btn-primary{background:linear-gradient(135deg,#4f46e5 0%,#6366f1 100%);color:#fff;box-shadow:0 6px 16px -4px rgba(79,70,229,.4)}
.csvn-wrap .csvn-btn-primary:hover:not(:disabled){transform:translateY(-2px);box-shadow:0 12px 24px -8px rgba(79,70,229,.5)}
.csvn-wrap .csvn-btn-ghost{background:#fff;color:#0f172a;border:1.5px solid #e2e8f0}
.csvn-wrap .csvn-btn-ghost:hover:not(:disabled){border-color:#4f46e5;color:#4f46e5}
.csvn-wrap .csvn-btn-block{width:100%}
.csvn-wrap .csvn-btn-row{display:flex;gap:10px;flex-wrap:wrap;justify-content:center}
.csvn-wrap .csvn-btn.loading{pointer-events:none;color:transparent}
.csvn-wrap .csvn-btn.loading::after{content:'';position:absolute;width:16px;height:16px;border:2px solid rgba(255,255,255,.3);border-top-color:#fff;border-radius:50%;animation:csvnSpin .7s linear infinite}
@keyframes csvnSpin{to{transform:rotate(360deg)}}
.csvn-wrap .csvn-payee{background:linear-gradient(135deg,#f0fdf4 0%,#ecfdf5 100%);border:1.5px solid #86efac;border-radius:12px;padding:18px;margin-bottom:16px}
.csvn-wrap .csvn-payee-head{display:flex;align-items:center;gap:9px;margin-bottom:12px}
.csvn-wrap .csvn-payee-check{width:22px;height:22px;border-radius:50%;background:#10b981;color:#fff;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:900;flex-shrink:0}
.csvn-wrap .csvn-payee-title{font-size:12px;font-weight:800;color:#065f46;letter-spacing:.05em;text-transform:uppercase}
.csvn-wrap .csvn-payee-row{display:flex;justify-content:space-between;align-items:center;padding:9px 0;border-bottom:1px solid #d1fae5;font-size:13px;gap:12px}
.csvn-wrap .csvn-payee-row:last-child{border-bottom:0}
.csvn-wrap .csvn-payee-row .lbl{color:#047857;font-weight:500;flex-shrink:0}
.csvn-wrap .csvn-payee-row .val{color:#065f46;font-weight:800;text-align:right;word-break:break-all}
.csvn-wrap .csvn-payee-row .val.mono{font-family:ui-monospace,Monaco,Menlo,monospace;font-size:12px}
.csvn-wrap .csvn-qr{text-align:center;padding:26px 16px;background:linear-gradient(135deg,#fafbff 0%,#f5f3ff 100%);border-radius:12px;border:1.5px dashed #e0e7ff;margin-bottom:16px}
.csvn-wrap .csvn-qr img{width:220px;height:220px;background:#fff;padding:12px;border-radius:14px;box-shadow:0 8px 24px -6px rgba(79,70,229,.18);display:inline-block;transition:transform .3s ease}
.csvn-wrap .csvn-qr img:hover{transform:scale(1.04)}
.csvn-wrap .csvn-qr-hint{font-size:12px;color:#64748b;margin-top:14px;font-weight:500}
.csvn-wrap .csvn-upi-apps{display:inline-flex;align-items:center;gap:8px;background:#fff;border:1px solid #e2e8f0;padding:8px 14px;border-radius:100px;font-size:11px;font-weight:700;color:#64748b;margin-top:14px}
.csvn-wrap .csvn-upi-apps .dot{width:6px;height:6px;border-radius:50%;background:#10b981}
.csvn-wrap .csvn-upi-box{display:flex;align-items:center;gap:10px;background:#f1f5f9;border:1.5px solid #e2e8f0;border-radius:10px;padding:10px 12px;margin-bottom:14px}
.csvn-wrap .csvn-upi-box code{flex:1;font-family:ui-monospace,Monaco,Menlo,monospace;font-size:12px;font-weight:700;color:#4f46e5;background:transparent;word-break:break-all;padding:6px 2px}
.csvn-wrap .csvn-copy-btn{background:#4f46e5;color:#fff;border:none;padding:8px 14px;border-radius:8px;font-size:11px;font-weight:800;cursor:pointer;font-family:inherit;transition:all .18s ease;flex-shrink:0;white-space:nowrap}
.csvn-wrap .csvn-copy-btn:hover{background:#3730a3}
.csvn-wrap .csvn-copy-btn.copied{background:#10b981}
.csvn-wrap .csvn-upload{border:2px dashed #e2e8f0;border-radius:12px;padding:26px 16px;text-align:center;cursor:pointer;transition:all .2s ease;background:#f1f5f9;display:block}
.csvn-wrap .csvn-upload:hover{border-color:#4f46e5;background:#eef2ff}
.csvn-wrap .csvn-upload input{display:none}
.csvn-wrap .csvn-upload svg{width:32px;height:32px;color:#64748b;margin:0 auto 8px}
.csvn-wrap .csvn-upload .fu-title{font-size:13px;font-weight:700;color:#0f172a;margin-bottom:4px}
.csvn-wrap .csvn-upload .fu-desc{font-size:11px;color:#64748b}
.csvn-wrap .csvn-file-preview{display:none;margin-top:12px;padding:12px;background:#fff;border:1px solid #e2e8f0;border-radius:10px;align-items:center;gap:12px}
.csvn-wrap .csvn-file-preview.show{display:flex}
.csvn-wrap .csvn-file-preview img{width:52px;height:52px;object-fit:cover;border-radius:8px;border:1px solid #e2e8f0}
.csvn-wrap .csvn-file-preview .info{flex:1;min-width:0}
.csvn-wrap .csvn-file-preview .name{font-size:12px;font-weight:700;color:#0f172a;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.csvn-wrap .csvn-file-preview .size{font-size:11px;color:#64748b;margin-top:2px}
.csvn-wrap .csvn-file-preview .remove{background:none;border:none;color:#ef4444;font-size:11.5px;font-weight:700;cursor:pointer;font-family:inherit;padding:7px 11px;border-radius:6px}
.csvn-wrap .csvn-summary{background:#f1f5f9;border:1px solid #e2e8f0;border-radius:12px;padding:18px;margin-bottom:18px}
.csvn-wrap .csvn-summary h4{font-size:11.5px;font-weight:800;color:#64748b;text-transform:uppercase;letter-spacing:.06em;margin-bottom:12px;display:flex;align-items:center;justify-content:space-between}
.csvn-wrap .csvn-summary .edit-link{font-size:11px;font-weight:700;color:#4f46e5;text-transform:none;letter-spacing:0;cursor:pointer;text-decoration:none}
.csvn-wrap .csvn-summary-row{display:flex;justify-content:space-between;padding:8px 0;font-size:13px;gap:12px;border-bottom:1px solid #e2e8f0}
.csvn-wrap .csvn-summary-row:last-child{border-bottom:0}
.csvn-wrap .csvn-summary-row .k{color:#64748b;font-weight:500}
.csvn-wrap .csvn-summary-row .v{color:#0f172a;font-weight:700;text-align:right;word-break:break-word}
.csvn-wrap .csvn-summary-row.total{border-top:2px solid #e2e8f0;border-bottom:0;padding-top:14px;margin-top:8px}
.csvn-wrap .csvn-summary-row.total .k{color:#0f172a;font-weight:800;font-size:14px}
.csvn-wrap .csvn-summary-row.total .v{color:#4f46e5;font-size:18px;font-weight:900}
.csvn-wrap .csvn-success{display:none;text-align:center;padding:32px 16px}
.csvn-wrap .csvn-success.show{display:block}
.csvn-wrap .csvn-success-icon{width:72px;height:72px;border-radius:50%;background:linear-gradient(135deg,#10b981 0%,#059669 100%);color:#fff;display:inline-flex;align-items:center;justify-content:center;margin-bottom:20px;box-shadow:0 16px 32px -8px rgba(16,185,129,.5)}
.csvn-wrap .csvn-success-icon svg{width:34px;height:34px;stroke-width:3}
.csvn-wrap .csvn-success h3{font-size:22px;font-weight:900;color:#0f172a;margin-bottom:10px;letter-spacing:-.025em}
.csvn-wrap .csvn-success p{font-size:14px;color:#64748b;max-width:460px;margin:0 auto 20px;line-height:1.65}
.csvn-wrap .csvn-success-ref{display:inline-block;background:#eef2ff;border:1px dashed #e0e7ff;padding:10px 16px;border-radius:10px;font-family:ui-monospace,Monaco,monospace;font-size:12.5px;font-weight:800;color:#4f46e5;margin-bottom:22px}
.csvn-wrap .csvn-info{background:linear-gradient(135deg,#eef2ff 0%,#f5f3ff 100%);border:1px solid #e0e7ff;border-radius:12px;padding:14px 16px;margin-bottom:16px;display:flex;gap:11px;align-items:flex-start}
.csvn-wrap .csvn-info svg{width:18px;height:18px;color:#4f46e5;flex-shrink:0;margin-top:1px}
.csvn-wrap .csvn-info p{font-size:12.5px;color:#3730a3;line-height:1.65;margin:0}
.csvn-wrap .csvn-trust-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin-top:8px}
.csvn-wrap .csvn-trust{background:#fff;border:1px solid #e2e8f0;border-radius:12px;padding:16px;display:flex;gap:12px;align-items:flex-start}
.csvn-wrap .csvn-trust .ti-icon{width:38px;height:38px;border-radius:10px;background:#eef2ff;color:#4f46e5;display:flex;align-items:center;justify-content:center;flex-shrink:0;font-weight:900;font-size:13px}
.csvn-wrap .csvn-trust .ti-title{font-size:13px;font-weight:800;color:#0f172a;margin-bottom:3px}
.csvn-wrap .csvn-trust .ti-desc{font-size:11.5px;color:#64748b;line-height:1.55}
.csvn-wrap .csvn-warn{background:#fef2f2;border:1.5px solid #fecaca;border-radius:12px;padding:16px;margin-top:14px}
.csvn-wrap .csvn-warn h4{font-size:13px;font-weight:800;color:#991b1b;margin-bottom:10px;display:flex;align-items:center;gap:8px}
.csvn-wrap .csvn-warn h4 svg{width:16px;height:16px;flex-shrink:0}
.csvn-wrap .csvn-warn ul{list-style:none;padding:0;display:grid;gap:6px;margin:0}
.csvn-wrap .csvn-warn li{font-size:12px;color:#7f1d1d;padding-left:18px;position:relative;line-height:1.6}
.csvn-wrap .csvn-warn li::before{content:'✗';position:absolute;left:0;top:0;color:#ef4444;font-weight:900;font-size:12px}
.csvn-wrap .csvn-faq-item{border-bottom:1px solid #e2e8f0;padding:16px 0;cursor:pointer}
.csvn-wrap .csvn-faq-item:last-child{border-bottom:0}
.csvn-wrap .csvn-faq-q{display:flex;justify-content:space-between;align-items:center;gap:16px;font-size:14px;font-weight:700;color:#0f172a}
.csvn-wrap .csvn-faq-q svg{width:16px;height:16px;color:#64748b;transition:transform .3s ease;flex-shrink:0}
.csvn-wrap .csvn-faq-item.open .csvn-faq-q svg{transform:rotate(180deg);color:#4f46e5}
.csvn-wrap .csvn-faq-a{max-height:0;overflow:hidden;transition:max-height .35s ease,padding .35s ease;font-size:13px;color:#64748b;line-height:1.7}
.csvn-wrap .csvn-faq-item.open .csvn-faq-a{max-height:500px;padding-top:10px}
.csvn-wrap .csvn-toast-wrap{position:fixed;bottom:24px;left:50%;transform:translateX(-50%);z-index:9999;display:flex;flex-direction:column;gap:8px;pointer-events:none;align-items:center}
.csvn-wrap .csvn-toast{background:#0f172a;color:#fff;padding:12px 18px;border-radius:11px;font-size:13px;font-weight:600;box-shadow:0 20px 40px -12px rgba(15,23,42,.15);display:flex;align-items:center;gap:10px;pointer-events:auto;max-width:calc(100vw - 32px)}
.csvn-wrap .csvn-toast.success{background:linear-gradient(135deg,#10b981 0%,#059669 100%)}
.csvn-wrap .csvn-toast.error{background:linear-gradient(135deg,#ef4444 0%,#dc2626 100%)}
.csvn-wrap .csvn-toast svg{width:16px;height:16px;flex-shrink:0}
@media (max-width:600px){
.csvn-wrap .csvn-hero{padding:28px 22px;border-radius:20px}
.csvn-wrap .csvn-card{padding:20px;border-radius:14px}
.csvn-wrap .csvn-qr img{width:190px;height:190px}
.csvn-wrap .csvn-form-row{grid-template-columns:1fr}
.csvn-wrap .csvn-btn-row .csvn-btn{flex:1 1 calc(50% - 5px);min-width:0}
.csvn-wrap .csvn-step{min-width:auto;padding:9px 11px;font-size:11px}
.csvn-wrap .csvn-step .step-label{display:none}
.csvn-wrap .csvn-step.active .step-label{display:inline}
}
</style>

<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>

<div class="csvn-wrap" id="csvnApp">
<div class="csvn-hero"><span class="csvn-hero-label">Complete Your Listing</span><h1>CSVN Standard Listing</h1><p class="csvn-hero-sub">Get your business listed on India's verified B2B vendor network with priority placement and unlimited customer inquiries for 12 months.</p><div class="csvn-hero-amt">₹999<small>One-time payment · 12 months validity</small></div><div class="csvn-hero-meta"><span>✓ Instant activation</span><span>✓ GST invoice</span><span>✓ 7-day refund</span></div></div>

<div class="csvn-steps"><div class="csvn-step active" data-step="1"><div class="csvn-step-num"><span>1</span></div><span class="step-label">Your Details</span></div><div class="csvn-step" data-step="2"><div class="csvn-step-num"><span>2</span></div><span class="step-label">Pay ₹999</span></div><div class="csvn-step" data-step="3"><div class="csvn-step-num"><span>3</span></div><span class="step-label">Generate Invoice</span></div><div class="csvn-step" data-step="4"><div class="csvn-step-num"><span>4</span></div><span class="step-label">Confirmation</span></div></div>

<div class="csvn-card" id="csvn-section-1"><div class="csvn-card-title"><span class="csvn-badge">1</span>Tell Us About Your Business</div><p class="csvn-card-desc">We'll use these details to prepare your invoice and activate your listing. All information is kept confidential.</p><div class="csvn-info"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg><p>Please enter details exactly as you want them to appear on your invoice and public listing. You'll be able to review everything in Step 3.</p></div><form id="csvnBusinessForm" onsubmit="csvnSubmitBusiness(event)" novalidate><div class="csvn-form-grid"><div class="csvn-field"><label for="csvn-bizName">Business Name <span class="req">*</span></label><input type="text" id="csvn-bizName" placeholder="e.g. Shree Ganesh Electricals Pvt Ltd" required><div class="csvn-err" id="csvn-err-bizName">Please enter your business name (min. 2 characters)</div></div><div class="csvn-field"><label for="csvn-contactName">Account Holder / Contact Person <span class="req">*</span></label><input type="text" id="csvn-contactName" placeholder="e.g. Rahul Sharma" required><div class="csvn-err" id="csvn-err-contactName">Please enter the account holder name</div></div><div class="csvn-form-row"><div class="csvn-field"><label for="csvn-email">Email Address <span class="req">*</span></label><input type="email" id="csvn-email" placeholder="you@business.com" required><div class="csvn-hint">Your invoice and confirmation will be emailed here.</div><div class="csvn-err" id="csvn-err-email">Please enter a valid email address</div></div><div class="csvn-field"><label for="csvn-phone">WhatsApp Number <span class="req">*</span></label><input type="tel" id="csvn-phone" placeholder="10-digit mobile number" maxlength="10" inputmode="numeric" required><div class="csvn-err" id="csvn-err-phone">Please enter a valid 10-digit mobile number</div></div></div><div class="csvn-form-row"><div class="csvn-field"><label for="csvn-category">Business Category <span class="req">*</span></label><select id="csvn-category" required><option value="">Select your category</option><option>Accounting &amp; Taxation</option><option>Legal &amp; Compliance</option><option>IT &amp; Software Services</option><option>Marketing &amp; Advertising</option><option>HR &amp; Recruitment</option><option>Logistics &amp; Supply Chain</option><option>Manufacturing &amp; Industrial</option><option>Real Estate &amp; Construction</option><option>Financial Services</option><option>Consulting &amp; Advisory</option><option>Other Corporate Services</option></select><div class="csvn-err" id="csvn-err-category">Please select a category</div></div><div class="csvn-field"><label for="csvn-city">City / Area <span class="req">*</span></label><input type="text" id="csvn-city" placeholder="e.g. Pimpri-Chinchwad, Pune" required><div class="csvn-err" id="csvn-err-city">Please enter your city</div></div></div><div class="csvn-form-row"><div class="csvn-field"><label for="csvn-website">Business Website <span class="opt">(optional)</span></label><input type="url" id="csvn-website" placeholder="https://yourbusiness.com"></div><div class="csvn-field"><label for="csvn-gst">GST Number <span class="opt">(optional)</span></label><input type="text" id="csvn-gst" placeholder="27ABCDE1234F1Z5" maxlength="15" style="text-transform:uppercase"></div></div></div><button type="submit" class="csvn-btn csvn-btn-primary csvn-btn-block" style="margin-top:22px">Continue to Payment →</button></form></div>

<div class="csvn-card" id="csvn-section-2" style="display:none"><div class="csvn-card-title"><span class="csvn-badge">2</span>Pay ₹999 via UPI</div><p class="csvn-card-desc">Scan the QR code with any UPI app, or pay directly to our verified UPI ID. Complete the payment, then continue to Step 3.</p><div class="csvn-payee"><div class="csvn-payee-head"><div class="csvn-payee-check">✓</div><div class="csvn-payee-title">Verified Payee — Confirm Before Paying</div></div><div class="csvn-payee-row"><span class="lbl">Account Holder</span><span class="val">Sachin Ambekar</span></div><div class="csvn-payee-row"><span class="lbl">Business Name</span><span class="val">CSVN — Corporate Services Vendor Network</span></div><div class="csvn-payee-row"><span class="lbl">Payment Gateway</span><span class="val">BharatPe (Yes Bank)</span></div><div class="csvn-payee-row"><span class="lbl">UPI ID</span><span class="val mono">BHARATPE09B9S1M8C3G33183@yesbankltd</span></div></div><p style="font-size:13px;color:#64748b;margin-bottom:16px">When you scan the QR or paste the UPI ID, your app will display the payee as <strong style="color:#0f172a">Sachin Ambekar</strong>. This is the only correct account for CSVN payments.</p><div class="csvn-qr"><img id="csvnQr" src="/qr.png" alt="CSVN Payment QR Code" loading="lazy"><div class="csvn-qr-hint">Scan with any UPI app</div><div class="csvn-upi-apps"><span class="dot"></span>PhonePe · GPay · Paytm · BHIM</div><div class="csvn-btn-row" style="margin-top:16px"><button type="button" class="csvn-btn csvn-btn-ghost" onclick="csvnDownloadQR(this)">↓ Download QR</button><a class="csvn-btn csvn-btn-primary" id="csvnUpiLink" href="#" style="display:none">Open UPI App</a></div></div><p style="font-size:11.5px;font-weight:700;color:#64748b;text-transform:uppercase;letter-spacing:.06em;margin-bottom:8px">Or pay to this UPI ID</p><div class="csvn-upi-box"><code>BHARATPE09B9S1M8C3G33183@yesbankltd</code><button type="button" class="csvn-copy-btn" onclick="csvnCopy('BHARATPE09B9S1M8C3G33183@yesbankltd',this)">Copy</button></div><p style="font-size:11.5px;font-weight:700;color:#64748b;text-transform:uppercase;letter-spacing:.06em;margin:18px 0 8px">Amount to pay</p><div class="csvn-upi-box"><code style="color:#10b981">₹999.00</code><button type="button" class="csvn-copy-btn" onclick="csvnCopy('999',this)">Copy</button></div><div class="csvn-info" style="margin-top:16px"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg><p>After completing the payment, keep your UPI app open — you'll need the <strong>UTR / Transaction ID</strong> for the next step.</p></div><button type="button" class="csvn-btn csvn-btn-primary csvn-btn-block" style="margin-top:18px" onclick="csvnNextStep(3)">I've Paid · Continue to Invoice →</button></div>

<div class="csvn-card" id="csvn-section-3" style="display:none"><div class="csvn-card-title"><span class="csvn-badge">3</span>Confirm Payment &amp; Generate Invoice</div><p class="csvn-card-desc">Enter your UPI Transaction ID (UTR) and upload a screenshot of your payment. We'll generate your invoice instantly.</p><div class="csvn-summary"><h4>Your Business Details <a class="edit-link" onclick="csvnShowStep(1)">Edit →</a></h4><div class="csvn-summary-row"><span class="k">Business Name</span><span class="v" id="csvn-sum-biz">—</span></div><div class="csvn-summary-row"><span class="k">Account Holder</span><span class="v" id="csvn-sum-name">—</span></div><div class="csvn-summary-row"><span class="k">Email</span><span class="v" id="csvn-sum-email">—</span></div><div class="csvn-summary-row"><span class="k">WhatsApp</span><span class="v" id="csvn-sum-phone">—</span></div><div class="csvn-summary-row"><span class="k">Category</span><span class="v" id="csvn-sum-category">—</span></div><div class="csvn-summary-row"><span class="k">City</span><span class="v" id="csvn-sum-city">—</span></div><div class="csvn-summary-row total"><span class="k">Amount</span><span class="v">₹999.00</span></div></div><form id="csvnPaymentForm" onsubmit="csvnSubmitPayment(event)" novalidate><div class="csvn-form-grid"><div class="csvn-field"><label for="csvn-utr">UPI Transaction ID / UTR <span class="req">*</span></label><input type="text" id="csvn-utr" placeholder="12-digit reference from your UPI app" maxlength="20" inputmode="numeric" required><div class="csvn-hint">Find this in your UPI app → tap the payment → copy the Transaction ID.</div><div class="csvn-err" id="csvn-err-utr">Please enter a valid UTR (8–20 characters)</div></div><div class="csvn-field"><label>Payment Screenshot <span class="req">*</span></label><label class="csvn-upload" id="csvnUpload" for="csvn-screenshot"><input type="file" id="csvn-screenshot" accept="image/*" onchange="csvnHandleFile(this)"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg><div class="fu-title">Click to upload or drag &amp; drop</div><div class="fu-desc">PNG, JPG up to 5 MB</div></label><div class="csvn-file-preview" id="csvnFilePreview"><img id="csvnFileThumb" src="" alt=""><div class="info"><div class="name" id="csvnFileName"></div><div class="size" id="csvnFileSize"></div></div><button type="button" class="remove" onclick="csvnRemoveFile()">Remove</button></div><div class="csvn-err" id="csvn-err-screenshot">Please attach a payment screenshot</div></div></div><button type="submit" class="csvn-btn csvn-btn-primary csvn-btn-block" style="margin-top:22px" id="csvnSubmitBtn">Confirm Payment · Generate Invoice</button></form><div class="csvn-success" id="csvnSuccess"><div class="csvn-success-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg></div><h3>Invoice Generated Successfully</h3><p>We've received your payment details. A confirmation email with your invoice has been sent to both you and our team. We'll verify the UTR and activate your listing within 24 business hours.</p><div class="csvn-success-ref" id="csvnSuccessRef">Invoice: CSVN-XXXX-XXXX</div><div class="csvn-btn-row" style="margin-bottom:16px"><button type="button" class="csvn-btn csvn-btn-primary" onclick="csvnDownloadInvoice(this)" id="csvnDownloadBtn">↓ Download Invoice (PDF)</button><button type="button" class="csvn-btn csvn-btn-ghost" onclick="window.print()">Print</button><button type="button" class="csvn-btn csvn-btn-ghost" onclick="csvnReset()">New Payment</button></div><p style="font-size:12px;color:#64748b">Questions? Email <a href="mailto:info@csvn.in" style="color:#4f46e5;font-weight:700">info@csvn.in</a> or WhatsApp <a href="tel:+918793932827" style="color:#4f46e5;font-weight:700">+91 87939 32827</a></p></div></div>

<div class="csvn-card" id="csvn-section-4" style="display:none"><div class="csvn-card-title"><span class="csvn-badge">4</span>What Happens Next</div><p class="csvn-card-desc">Your payment confirmation has reached our team. Here's our verification and activation timeline.</p><div style="display:grid;gap:10px"><div class="csvn-trust"><div class="ti-icon">1</div><div><div class="ti-title">Payment Verification</div><div class="ti-desc">We match your UTR against our bank statement. Typically within <strong>4 business hours</strong>.</div></div></div><div class="csvn-trust"><div class="ti-icon">2</div><div><div class="ti-title">Business Details Confirmation</div><div class="ti-desc">We verify your business name, address, and category. Within <strong>1 business day</strong>.</div></div></div><div class="csvn-trust"><div class="ti-icon">3</div><div><div class="ti-title">Listing Goes Live</div><div class="ti-desc">Your business appears on CSVN with priority placement. Within <strong>24 hours</strong>.</div></div></div><div class="csvn-trust"><div class="ti-icon">4</div><div><div class="ti-title">GST Invoice Email</div><div class="ti-desc">A GST-compliant invoice is emailed to you. Sent the <strong>same day</strong> as activation.</div></div></div></div></div>

<div class="csvn-card"><div class="csvn-card-title">Your Payment Is Protected</div><p class="csvn-card-desc">We follow strict verification practices to keep your money and data safe.</p><div class="csvn-trust-grid"><div class="csvn-trust"><div class="ti-icon">🔒</div><div><div class="ti-title">Verified Payee</div><div class="ti-desc">Registered under Sachin Ambekar via BharatPe.</div></div></div><div class="csvn-trust"><div class="ti-icon">✓</div><div><div class="ti-title">7-Day Refund</div><div class="ti-desc">Full refund if no inquiries received.</div></div></div><div class="csvn-trust"><div class="ti-icon">⏱</div><div><div class="ti-title">24-Hour Activation</div><div class="ti-desc">Your listing goes live the same day.</div></div></div><div class="csvn-trust"><div class="ti-icon">✉</div><div><div class="ti-title">GST Invoice</div><div class="ti-desc">Emailed automatically after activation.</div></div></div></div><div class="csvn-warn"><h4><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>We will NEVER ask you for:</h4><ul><li>Your UPI PIN, OTP, CVV, or bank password</li><li>Payment to any UPI ID other than the one on this page</li><li>Payment via gift cards, crypto, or unusual methods</li><li>Payment requests over WhatsApp or social media DMs</li></ul><p style="font-size:12px;color:#7f1d1d;margin-top:12px;line-height:1.6">If anyone contacts you claiming to be from CSVN and asks for something different, report it to <a href="mailto:report@csvn.in" style="color:#991b1b;font-weight:800">report@csvn.in</a> immediately.</p></div></div>

<div class="csvn-card"><div class="csvn-card-title">Frequently Asked Questions</div><div class="csvn-faq-item" onclick="this.classList.toggle('open')"><div class="csvn-faq-q">What if I paid but didn't receive a confirmation?<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></div><div class="csvn-faq-a">Email us at info@csvn.in with your UTR and business name. We'll verify manually and confirm within 2 business hours.</div></div><div class="csvn-faq-item" onclick="this.classList.toggle('open')"><div class="csvn-faq-q">Can I pay from a different UPI app?<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></div><div class="csvn-faq-a">Yes. Any UPI app works — PhonePe, Google Pay, Paytm, BHIM, Amazon Pay, WhatsApp Pay, or your bank's app. Just make sure the payee name shows "Sachin Ambekar".</div></div><div class="csvn-faq-item" onclick="this.classList.toggle('open')"><div class="csvn-faq-q">Is the payment refundable?<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></div><div class="csvn-faq-a">Yes — full refund within 7 days if you haven't received any customer inquiries, partial refund between 8–15 days, no refund after 15 days. See our full <a href="/refund/" style="color:#4f46e5;font-weight:700">Refund Policy</a>.</div></div><div class="csvn-faq-item" onclick="this.classList.toggle('open')"><div class="csvn-faq-q">How long does activation take?<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></div><div class="csvn-faq-a">Typically within 24 hours of receiving your payment confirmation. You'll get an email with your listing URL and invoice as soon as it's live.</div></div><div class="csvn-faq-item" onclick="this.classList.toggle('open')"><div class="csvn-faq-q">Do I get a GST invoice?<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg></div><div class="csvn-faq-a">Yes. A GST-compliant invoice is emailed to the address you provide, on the same day your listing is activated.</div></div></div>

<p style="text-align:center;font-size:12px;color:#64748b;padding:36px 16px 8px;line-height:1.7"><strong style="color:#0f172a">CSVN</strong> — Corporate Services Vendor Network<br>Owned and operated by Sachin Ambekar · Nigdi, Pimpri-Chinchwad, Pune<br><a href="mailto:info@csvn.in" style="color:#4f46e5;font-weight:700">info@csvn.in</a> · <a href="tel:+918793932827" style="color:#4f46e5;font-weight:700">+91 87939 32827</a> · Mon–Sat, 10 AM – 6 PM IST</p>

</div>

<div class="csvn-toast-wrap" id="csvnToasts"></div>

<script>
(function(){
'use strict';
var CONFIG={
  brandName:'CSVN — Corporate Services Vendor Network',
  ownerName:'Sachin Ambekar',
  upiId:'BHARATPE09B9S1M8C3G33183@yesbankltd',
  payeeName:'Sachin Ambekar',
  amount:999,
  qrUrl:'/qr.png',
  supportEmail:'info@csvn.in',
  supportPhone:'+91 87939 32827',
  product:'CSVN Standard Listing — 12 Months',
  adminEndpoint:'https://formsubmit.co/ajax/pcmcdiary@gmail.com'
};
var STORAGE_KEY='csvn_payment_v1';
var state={step:1,form:{},hasScreenshot:false,submittedRef:null,receiptData:null};
function saveState(){try{localStorage.setItem(STORAGE_KEY,JSON.stringify({step:state.step,form:state.form,submittedRef:state.submittedRef,receiptData:state.receiptData}));}catch(e){}}
function loadState(){try{var raw=localStorage.getItem(STORAGE_KEY);if(!raw)return;Object.assign(state,JSON.parse(raw));}catch(e){}}

var progressBar=document.getElementById('progressBar');
function showProgress(){}
function hideProgress(){}

function showStep(n){
  state.step=Math.max(1,Math.min(4,n));saveState();
  for(var i=1;i<=4;i++){
    var el=document.getElementById('csvn-section-'+i);if(!el)continue;
    if(i===3 && document.getElementById('csvnSuccess').classList.contains('show')){el.style.display='block';}
    else{el.style.display=(i===state.step)?'block':'none';}
  }
  var steps=document.querySelectorAll('.csvn-step');
  for(var j=0;j<steps.length;j++){
    var s=parseInt(steps[j].getAttribute('data-step'));
    steps[j].classList.toggle('active',s===state.step);
    steps[j].classList.toggle('done',s<state.step);
  }
  requestAnimationFrame(function(){requestAnimationFrame(scrollToActiveSection);});
}
function scrollToActiveSection(){
  var target=document.getElementById('csvn-section-'+state.step);
  if(state.step===3 && document.getElementById('csvnSuccess').classList.contains('show')){target=document.getElementById('csvnSuccess');}
  if(!target)return;
  var rect=target.getBoundingClientRect();
  var offset=90;
  if(rect.top>=offset && rect.top<=window.innerHeight/2)return;
  var y=rect.top+window.pageYOffset-offset;
  window.scrollTo({top:Math.max(0,y),behavior:'smooth'});
}
window.csvnShowStep=showStep;
window.csvnNextStep=function(n){showStep(n);if(n===3)refreshSummary();};
var stepEls=document.querySelectorAll('.csvn-step');
for(var k=0;k<stepEls.length;k++){
  stepEls[k].addEventListener('click',function(){
    var n=parseInt(this.getAttribute('data-step'));
    if(n>1 && !state.form.bizName){csvnToast('Please complete Step 1 first','error');return;}
    showStep(n);if(n===3)refreshSummary();
  });
}
function showFieldError(id,show){
  var err=document.getElementById('csvn-err-'+id);
  var inp=document.getElementById('csvn-'+id);
  if(err)err.classList.toggle('show',show);
  if(inp)inp.classList.toggle('error',show);
}
function isFieldValid(id,v){
  switch(id){
    case 'bizName':case 'contactName':case 'city':return v.length>=2;
    case 'email':return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v);
    case 'phone':return /^\d{10}$/.test(v);
    case 'category':return v.length>0;
    default:return true;
  }
}
['bizName','contactName','email','phone','category','city','website','gst'].forEach(function(id){
  var el=document.getElementById('csvn-'+id);if(!el)return;
  function handler(){state.form[id]=el.value;saveState();if(el.classList.contains('error'))showFieldError(id,false);}
  el.addEventListener('input',handler);
  el.addEventListener('change',handler);
});
window.csvnSubmitBusiness=function(e){
  e.preventDefault();
  var ok=true;
  ['bizName','contactName','email','phone','category','city'].forEach(function(id){
    var el=document.getElementById('csvn-'+id);
    var v=el?el.value.trim():'';
    if(!isFieldValid(id,v)){showFieldError(id,true);ok=false;}else showFieldError(id,false);
  });
  if(!ok){csvnToast('Please fix the highlighted fields','error');return;}
  ['bizName','contactName','email','phone','category','city','website','gst'].forEach(function(id){
    var el=document.getElementById('csvn-'+id);if(el)state.form[id]=el.value;
  });
  saveState();
  var btn=e.target.querySelector('button[type="submit"]');
  btn.classList.add('loading');
  setTimeout(function(){btn.classList.remove('loading');csvnToast('Business details saved','success');window.csvnNextStep(2);},350);
};
function refreshSummary(){
  var f=state.form;
  document.getElementById('csvn-sum-biz').textContent=f.bizName||'—';
  document.getElementById('csvn-sum-name').textContent=f.contactName||'—';
  document.getElementById('csvn-sum-email').textContent=f.email||'—';
  document.getElementById('csvn-sum-phone').textContent=f.phone?'+91 '+f.phone:'—';
  document.getElementById('csvn-sum-category').textContent=f.category||'—';
  document.getElementById('csvn-sum-city').textContent=f.city||'—';
}
var MAX_SIZE=5*1024*1024;
window.csvnHandleFile=function(input){
  var file=input.files && input.files[0];
  if(!file)return;
  if(file.size>MAX_SIZE){csvnToast('File too large. Max 5 MB.','error');input.value='';return;}
  if(!file.type.startsWith('image/')){csvnToast('Please upload an image file','error');input.value='';return;}
  var reader=new FileReader();
  reader.onload=function(e){
    document.getElementById('csvnFileThumb').src=e.target.result;
    document.getElementById('csvnFileName').textContent=file.name;
    document.getElementById('csvnFileSize').textContent=(file.size/1024).toFixed(1)+' KB';
    document.getElementById('csvnFilePreview').classList.add('show');
    document.getElementById('csvnUpload').style.display='none';
    showFieldError('screenshot',false);
    state.hasScreenshot=true;saveState();
  };
  reader.readAsDataURL(file);
};
window.csvnRemoveFile=function(){
  document.getElementById('csvn-screenshot').value='';
  document.getElementById('csvnFilePreview').classList.remove('show');
  document.getElementById('csvnUpload').style.display='block';
  state.hasScreenshot=false;saveState();
};
window.csvnSubmitPayment=function(e){
  e.preventDefault();
  var utr=document.getElementById('csvn-utr').value.trim();
  if(utr.length<8||utr.length>20){showFieldError('utr',true);csvnToast('Please enter a valid UTR','error');return;}
  showFieldError('utr',false);
  if(!state.hasScreenshot){showFieldError('screenshot',true);csvnToast('Please attach the payment screenshot','error');return;}
  showFieldError('screenshot',false);
  var btn=document.getElementById('csvnSubmitBtn');
  btn.classList.add('loading');
  var ref='CSVN-'+Date.now().toString(36).toUpperCase().slice(-6)+'-'+Math.random().toString(36).slice(2,6).toUpperCase();
  state.submittedRef=ref;
  var f=state.form;
  state.receiptData={ref:ref,business:f.bizName||'',name:f.contactName||'',email:f.email||'',phone:f.phone||'',category:f.category||'',city:f.city||'',website:f.website||'',gst:f.gst||'',utr:utr,amount:CONFIG.amount,paidAt:new Date().toISOString()};
  saveState();
  sendEmails(state.receiptData).then(function(){csvnToast('Invoice generated & emailed','success');}).catch(function(err){console.error(err);csvnToast('Invoice generated (email may be delayed)','info');});
  document.getElementById('csvnPaymentForm').style.display='none';
  document.getElementById('csvnSuccessRef').textContent='Invoice: '+ref;
  document.getElementById('csvnSuccess').classList.add('show');
  document.getElementById('csvn-section-4').style.display='block';
  var steps2=document.querySelectorAll('.csvn-step');
  for(var i=0;i<steps2.length;i++){
    var s=parseInt(steps2[i].getAttribute('data-step'));
    steps2[i].classList.toggle('done',s<=3);
    steps2[i].classList.toggle('active',s===4);
  }
  state.step=3;saveState();
  btn.classList.remove('loading');
  requestAnimationFrame(function(){requestAnimationFrame(scrollToActiveSection);});
};
function sendEmails(d){
  var dateStr=new Date(d.paidAt).toLocaleString('en-IN',{dateStyle:'medium',timeStyle:'short'});
  var jsonSnippet=JSON.stringify({id:d.ref.toLowerCase().replace(/[^a-z0-9]/g,'-'),name:d.business,phone:d.phone,city:d.city,category:(d.category||'').toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,''),tier:'Standard',order:999,website:d.website||'',gst:d.gst||'',email:d.email},null,2);
  var payload={
    _subject:'🟡 PENDING VERIFICATION — '+d.business+' (₹'+d.amount+') — UTR: '+d.utr+' | CSVN',
    _template:'table',
    _captcha:'false',
    _replyto:d.email,
    _cc:d.email,
    'Invoice No.':d.ref,
    'Business Name':d.business,
    'Account Holder':d.name,
    'Email':d.email,
    'WhatsApp':'+91 '+d.phone,
    'Category':d.category,
    'City':d.city,
    'Website':d.website||'—',
    'GST Number':d.gst||'—',
    'Amount Paid':'Rs. '+d.amount,
    'UPI / UTR':d.utr,
    'Payment Date':dateStr,
    'Status':'⚠ PENDING VERIFICATION',
    'Next Action':'1) Verify UTR against BharatPe. 2) Paste JSON below into data/clients/real-XX.json. 3) Push to GitHub.',
    '--- JSON for data/clients/ ---':jsonSnippet
  };
  return fetch(CONFIG.adminEndpoint,{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(payload)}).then(function(res){if(!res.ok)throw new Error('Email failed: '+res.status);return res;});
}
window.csvnDownloadInvoice=function(btn){
  var d=state.receiptData;
  if(!d){csvnToast('No invoice data available','error');return;}
  if(btn)btn.classList.add('loading');
  try{
    var jsPDF=window.jspdf.jsPDF;
    var doc=new jsPDF({unit:'mm',format:'a4'});
    var pageW=doc.internal.pageSize.getWidth();
    var pageH=doc.internal.pageSize.getHeight();
    var margin=16;
    var y=0;
    doc.setFillColor(79,70,229);doc.rect(0,0,pageW,40,'F');
    doc.setTextColor(255,255,255);doc.setFont('helvetica','bold');doc.setFontSize(22);doc.text('CSVN',margin,18);
    doc.setFont('helvetica','normal');doc.setFontSize(9);
    doc.text('Corporate Services Vendor Network',margin,25);
    doc.text('Nigdi, Pimpri-Chinchwad, Pune, Maharashtra',margin,30.5);
    doc.text('info@csvn.in  |  +91 87939 32827',margin,36);
    doc.setFont('helvetica','bold');doc.setFontSize(16);doc.text('TAX INVOICE',pageW-margin,20,{align:'right'});
    doc.setFontSize(9);doc.setFont('helvetica','normal');doc.text('Original for Recipient',pageW-margin,27,{align:'right'});
    y=56;
    doc.setTextColor(15,23,42);doc.setFont('helvetica','bold');doc.setFontSize(11);doc.text('Invoice Details',margin,y);
    y+=3;doc.setDrawColor(226,232,240);doc.line(margin,y,pageW-margin,y);y+=7;
    [['Invoice No.',d.ref],['Invoice Date',new Date(d.paidAt).toLocaleDateString('en-IN',{dateStyle:'medium'})],['Payment Method','UPI / BharatPe (Yes Bank)'],['Payment Status','Paid — Awaiting Verification']].forEach(function(row){
      doc.setFont('helvetica','normal');doc.setTextColor(100,116,139);doc.text(row[0],margin,y);
      doc.setFont('helvetica','bold');doc.setTextColor(15,23,42);doc.text(String(row[1]),margin+42,y);y+=7;
    });
    y+=6;
    doc.setFont('helvetica','bold');doc.setFontSize(11);doc.setTextColor(15,23,42);doc.text('Billed To',margin,y);
    y+=3;doc.line(margin,y,pageW-margin,y);y+=7;
    var custRows=[['Business Name',d.business],['Account Holder',d.name],['Email',d.email],['Phone','+91 '+d.phone],['Category',d.category],['City',d.city]];
    if(d.gst)custRows.push(['GST Number',d.gst]);
    if(d.website)custRows.push(['Website',d.website]);
    doc.setFontSize(10);
    custRows.forEach(function(row){
      doc.setFont('helvetica','normal');doc.setTextColor(100,116,139);doc.text(row[0],margin,y);
      doc.setFont('helvetica','bold');doc.setTextColor(15,23,42);doc.text(String(row[1]),margin+42,y);y+=7;
    });
    y+=6;
    doc.setFont('helvetica','bold');doc.setFontSize(11);doc.text('Services',margin,y);y+=7;
    doc.setFillColor(238,242,255);doc.rect(margin,y-5,pageW-margin*2,9,'F');
    doc.setFontSize(9);doc.setTextColor(79,70,229);doc.text('DESCRIPTION',margin+3,y+1);
    doc.text('AMOUNT',pageW-margin-3,y+1,{align:'right'});y+=10;
    doc.setFont('helvetica','normal');doc.setFontSize(10);doc.setTextColor(15,23,42);
    doc.text(CONFIG.product,margin+3,y);
    doc.setFont('helvetica','bold');doc.text('Rs. '+d.amount+'.00',pageW-margin-3,y,{align:'right'});y+=9;
    doc.setDrawColor(226,232,240);doc.line(margin,y-2,pageW-margin,y-2);y+=6;
    doc.setFillColor(79,70,229);doc.rect(margin,y-5,pageW-margin*2,12,'F');
    doc.setFontSize(12);doc.setTextColor(255,255,255);doc.text('TOTAL PAID',margin+3,y+3);
    doc.text('Rs. '+d.amount+'.00',pageW-margin-3,y+3,{align:'right'});y+=18;
    doc.setFillColor(240,253,244);doc.setDrawColor(134,239,172);doc.roundedRect(margin,y,pageW-margin*2,22,3,3,'FD');
    doc.setFont('helvetica','bold');doc.setFontSize(9);doc.setTextColor(6,95,70);
    doc.text('UPI TRANSACTION REFERENCE (UTR)',margin+6,y+8);doc.setFontSize(14);doc.text(d.utr,margin+6,y+16);
    y+=30;
    doc.setFillColor(255,251,235);doc.setDrawColor(252,211,77);doc.roundedRect(margin,y,pageW-margin*2,30,3,3,'FD');
    doc.setFont('helvetica','bold');doc.setFontSize(9);doc.setTextColor(146,64,14);
    doc.text('IMPORTANT — VALIDITY OF THIS INVOICE',margin+6,y+6);
    doc.setFont('helvetica','normal');doc.setFontSize(8.5);doc.setTextColor(120,53,15);
    ['This invoice is provisional in nature and becomes valid only upon successful verification of the','UTR above against the CSVN bank statement. Until such verification is completed, this document','does not constitute final proof of payment or confirmed activation of the requested listing.','For verification status or queries, contact info@csvn.in within 24 business hours.'].forEach(function(line,i){doc.text(line,margin+6,y+12+i*4.2);});
    y+=38;
    doc.setFont('helvetica','bold');doc.setFontSize(9);doc.setTextColor(15,23,42);doc.text('Terms & Notes',margin,y);y+=5;
    doc.setFont('helvetica','normal');doc.setFontSize(8.5);doc.setTextColor(100,116,139);
    ['1. This is a computer-generated invoice. No physical signature is required.','2. Listing activation occurs within 24 business hours of successful UTR verification.','3. The listing is valid for a period of 12 months from the date of activation.','4. Refunds are governed by the CSVN Refund Policy available at csvn.in/refund.','5. This invoice is issued under the provisions of the CGST Act, 2017.','6. Any dispute shall be subject to the exclusive jurisdiction of courts in Pune, Maharashtra.','7. For queries, write to info@csvn.in or call +91 87939 32827 (Mon–Sat, 10 AM – 6 PM IST).'].forEach(function(line){doc.text(line,margin,y);y+=4.2;});
    y=pageH-18;doc.setDrawColor(226,232,240);doc.line(margin,y-4,pageW-margin,y-4);
    doc.setFontSize(7.5);doc.setTextColor(148,163,184);
    doc.text(CONFIG.brandName+' | Owned and operated by '+CONFIG.ownerName,margin,y);
    doc.text('Generated '+new Date().toLocaleString('en-IN'),pageW-margin,y,{align:'right'});
    doc.save('CSVN-Invoice-'+d.ref+'.pdf');
    csvnToast('Invoice downloaded','success');
  }catch(err){
    console.error('PDF error:',err);
    csvnToast('Could not generate PDF. Please try again.','error');
  }finally{
    if(btn)btn.classList.remove('loading');
  }
};
window.csvnCopy=function(text,btn){
  function done(){var orig=btn.textContent;btn.textContent='✓ Copied';btn.classList.add('copied');csvnToast('Copied to clipboard','success');setTimeout(function(){btn.textContent=orig;btn.classList.remove('copied');},1800);}
  function fallback(t,cb){var ta=document.createElement('textarea');ta.value=t;ta.style.position='fixed';ta.style.opacity='0';document.body.appendChild(ta);ta.select();try{document.execCommand('copy');cb();}catch(e){csvnToast('Copy failed','error');}document.body.removeChild(ta);}
  if(navigator.clipboard && navigator.clipboard.writeText){navigator.clipboard.writeText(text).then(done).catch(function(){fallback(text,done);});}else fallback(text,done);
};
window.csvnDownloadQR=function(btn){
  if(btn)btn.classList.add('loading');
  fetch(CONFIG.qrUrl,{mode:'cors'}).then(function(r){return r.blob();}).then(function(blob){
    var url=URL.createObjectURL(blob);
    var a=document.createElement('a');a.href=url;a.download='CSVN-Payment-QR.png';
    document.body.appendChild(a);a.click();document.body.removeChild(a);URL.revokeObjectURL(url);
    csvnToast('QR downloaded','success');
  }).catch(function(){window.open(CONFIG.qrUrl,'_blank');}).finally(function(){if(btn)btn.classList.remove('loading');});
};
window.csvnToast=function(msg,type){
  var c=document.getElementById('csvnToasts');if(!c)return;
  var icons={success:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',error:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>',info:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>'};
  while(c.children.length>=3)c.removeChild(c.firstChild);
  var t=document.createElement('div');t.className='csvn-toast '+(type||'info');t.innerHTML=(icons[type]||icons.info)+'<span>'+msg+'</span>';c.appendChild(t);
  setTimeout(function(){t.style.transition='opacity .3s ease,transform .3s ease';t.style.opacity='0';t.style.transform='translateY(20px)';setTimeout(function(){t.remove();},300);},2800);
};
window.csvnReset=function(){if(!confirm('Clear this submission and start a new payment?'))return;localStorage.removeItem(STORAGE_KEY);location.reload();};
var isMobile=/Android|iPhone|iPad|iPod/i.test(navigator.userAgent);
if(isMobile){
  var link=document.getElementById('csvnUpiLink');
  if(link){
    var params=new URLSearchParams({pa:CONFIG.upiId,pn:CONFIG.payeeName,am:CONFIG.amount.toFixed(2),cu:'INR',tn:'CSVN Listing'});
    link.href='upi://pay?'+params.toString();
    link.style.display='inline-flex';
  }
}
loadState();
Object.keys(state.form).forEach(function(k){var el=document.getElementById('csvn-'+k);if(el&&state.form[k])el.value=state.form[k];});
if(state.submittedRef && state.receiptData){
  document.getElementById('csvnSuccessRef').textContent='Invoice: '+state.submittedRef;
  document.getElementById('csvnSuccess').classList.add('show');
  document.getElementById('csvnPaymentForm').style.display='none';
  document.getElementById('csvn-section-4').style.display='block';
  showStep(3);
  var ss=document.querySelectorAll('.csvn-step');
  for(var i2=0;i2<ss.length;i2++){var s2=parseInt(ss[i2].getAttribute('data-step'));ss[i2].classList.toggle('done',s2<=3);}
}else{
  showStep(state.step||1);
}
})();
</script>
