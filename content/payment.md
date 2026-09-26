---
title: "Payment"
description: "Pay ₹999 for your CSVN Standard listing via UPI. Scan QR code or use our UPI ID directly."
layout: "page"
---

## Complete Your Payment — ₹999

You're one step away from getting listed on CSVN. Complete your ₹999 payment using any UPI app below.

<div style="background: linear-gradient(135deg, #4f46e5 0%, #3730a3 100%); border-radius: 16px; padding: 2rem; color: #fff; margin: 2rem 0; text-align: center; box-shadow: 0 20px 40px -12px rgba(79, 70, 229, 0.4);">
  <div style="font-size: 0.7rem; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; opacity: 0.8; margin-bottom: 0.5rem;">Amount to Pay</div>
  <div style="font-size: 3rem; font-weight: 800; line-height: 1;">₹999</div>
  <div style="font-size: 0.85rem; opacity: 0.9; margin-top: 0.5rem;">CSVN Standard Listing — 1 Year</div>
</div>

## Scan QR Code to Pay

Open any UPI app (PhonePe, Google Pay, Paytm, BHIM, or your bank's app) and scan the QR code below.

<div style="background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 16px; padding: 2rem; margin: 2rem 0; text-align: center;">

  <!-- QR CODE — replace the src below with your QR code image -->
  <img src="/payment-qr.png" alt="CSVN Payment QR Code" style="width: 260px; height: 260px; margin: 0 auto 1rem; display: block; background: #fff; padding: 12px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);">

  <div style="font-size: 0.85rem; color: #64748b; margin-top: 0.5rem;">Scan with any UPI app</div>

  <div style="display: inline-flex; align-items: center; gap: 0.5rem; background: #fff; border: 1px solid #e2e8f0; border-radius: 100px; padding: 0.5rem 1rem; margin-top: 1rem; font-size: 0.75rem; font-weight: 600; color: #475569;">
    <span style="display: inline-block; width: 6px; height: 6px; background: #10b981; border-radius: 50%;"></span>
    PhonePe · Google Pay · Paytm · BHIM · Any UPI App
  </div>

</div>

## Or Pay Using UPI ID

Don't want to scan? Send payment directly to our UPI ID:

<div style="background: #fff; border: 2px solid #e2e8f0; border-radius: 12px; padding: 1.5rem; margin: 2rem 0;">
  <div style="font-size: 0.7rem; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; color: #64748b; margin-bottom: 0.5rem;">CSVN UPI ID</div>
  <div style="display: flex; align-items: center; gap: 0.75rem; flex-wrap: wrap;">
    <code id="upi-id" style="background: #f1f5f9; color: #4f46e5; padding: 0.75rem 1rem; border-radius: 8px; font-size: 1rem; font-weight: 700; font-family: 'JetBrains Mono', monospace; flex: 1; min-width: 200px;">sachin@okhdfcbank</code>
    <button onclick="copyUPI()" id="copy-btn" style="background: #4f46e5; color: #fff; border: 0; padding: 0.75rem 1.25rem; border-radius: 8px; font-weight: 700; font-size: 0.8rem; cursor: pointer; display: inline-flex; align-items: center; gap: 0.5rem;">Copy UPI ID</button>
  </div>
</div>

**Steps:**

1. Copy the UPI ID above
2. Open your UPI app
3. Choose "Pay to UPI ID" or "Send Money"
4. Paste the UPI ID
5. Enter amount: **₹999**
6. Add note: **CSVN Listing — [Your Business Name]**
7. Confirm and pay

## After Payment — Send Us the Confirmation

Once you've paid, email us the payment screenshot at [info@csvn.in](mailto:info@csvn.in?subject=Payment%20Confirmation%20-%20%E2%82%B9999%20CSVN%20Listing&body=Business%20Name%3A%0AUPI%20Transaction%20ID%3A%0AAmount%20Paid%3A%20%E2%82%B9999%0APayment%20Date%3A%0A%0A(Please%20attach%20your%20payment%20screenshot)%0A) with:

- **Business name**
- **UPI transaction ID** (from your payment app)
- **Amount paid** (₹999)
- **Payment date**
- **Screenshot of the payment confirmation** (attach to the email)

We'll verify and activate your listing within 24 hours.

## Need Help With Payment?

If you have any trouble with the payment, contact us before sending money:

**Email:** [info@csvn.in](mailto:info@csvn.in)
**Phone/WhatsApp:** +91 87939 32827
**Hours:** Mon–Sat, 10 AM – 6 PM IST

## Payment Security Notes

**Before paying, please verify:**

- Our UPI ID is **sachin@okhdfcbank** (update this with your real UPI ID)
- You're paying exactly **₹999**
- You're on the official CSVN website (**csvn.in**)
- You can reach us at **info@csvn.in** or **+91 87939 32827** before paying

**We will never:**

- Ask you to pay a different amount
- Ask for your UPI PIN, OTP, or bank password
- Send payment requests from a different UPI ID
- Ask you to pay via gift cards or crypto

If anyone contacts you claiming to be from CSVN and asks for something different, please report it to [report@csvn.in](mailto:report@csvn.in) immediately.

## What Happens After Payment

| Step | Timeline |
| :--- | :--- |
| You send payment confirmation email | — |
| We verify your payment | Within 4 business hours |
| We confirm your business details | Within 1 business day |
| Your listing goes live | Within 24 hours of payment |
| You receive confirmation email + invoice | Same day as listing activation |

## Refund Policy

Payments for CSVN listings are governed by our [Refund Policy](/refund/). In brief:

- Full refund within 7 days if you haven't received any inquiries
- Partial refund between 8–15 days
- No refund after 15 days

---

*CSVN — Corporate Services Vendor Network is owned and operated by Sachin Ambekar, based in Nigdi, Pimpri-Chinchwad, Pune, Maharashtra, India.*

<script>
function copyUPI() {
  const upiId = document.getElementById('upi-id').textContent.trim();
  const btn = document.getElementById('copy-btn');

  const done = () => {
    const original = btn.innerHTML;
    btn.innerHTML = '✓ Copied!';
    btn.style.background = '#10b981';
    setTimeout(() => {
      btn.innerHTML = original;
      btn.style.background = '#4f46e5';
    }, 1800);
  };

  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(upiId).then(done).catch(() => fallback(upiId, done));
  } else {
    fallback(upiId, done);
  }
}

function fallback(text, cb) {
  const ta = document.createElement('textarea');
  ta.value = text;
  document.body.appendChild(ta);
  ta.select();
  document.execCommand('copy');
  document.body.removeChild(ta);
  cb();
}
</script>
