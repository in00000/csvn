#!/usr/bin/env python3
"""
Dummy client generator for CSVN.

Runs during GitHub Actions builds to populate the site with
placeholder vendors. Every dummy has "_dummy": true and its file
name starts with "DUMMY-".

TO REMOVE ALL DUMMY DATA PERMANENTLY:
  1. Delete this file from the repo
  2. Commit
That's it. The next build will skip dummy generation.
"""
import json
import random
import re
from pathlib import Path

PER_CATEGORY = 10   # ← change to 30 (or any number) if you want more

random.seed(20260101)   # deterministic — same output on every run

root = Path(__file__).resolve().parent.parent
cats_file = root / "data" / "categories.json"
out_dir = root / "data" / "clients"
out_dir.mkdir(parents=True, exist_ok=True)

PREFIXES = [
    "Vertex","Zenith","Cascade","Brightline","Meridian","Northwind",
    "Skyline","Baseline","Ironwood","Copperfield","Stonebridge",
    "Clearwater","Evergreen","Bluewave","Redwood","Sunridge","Oakfield",
    "Lakeside","Harborview","Fairmont","Glenmark","Brookside","Ridgeway",
    "Westbridge","Crestline","Silverbay","Goldcrest","Ambertech",
    "Platinum","Emerald","Sapphire","Crystal","Onyx","Aurora",
    "Beacon","Compass","Anchor","Pinnacle","Summit","Horizon",
    "Novus","Veritas","Primeo","Nexora","Quanta","Vantix",
    "Corevault","Optivo","Gridwise","Truebridge",
]

SUFFIXES = [
    "Services","Solutions","Enterprises","Industries","Associates",
    "Group","Networks","Systems","Corp","India Pvt Ltd",
]

CITIES = [
    ("Mumbai","Maharashtra"),("Pune","Maharashtra"),
    ("Bangalore","Karnataka"),("Chennai","Tamil Nadu"),
    ("Hyderabad","Telangana"),("Gurgaon","Haryana"),
    ("Noida","Uttar Pradesh"),("Ahmedabad","Gujarat"),
    ("Kolkata","West Bengal"),("Jaipur","Rajasthan"),
    ("Indore","Madhya Pradesh"),("Coimbatore","Tamil Nadu"),
]

REVIEWERS = [
    "Rahul Sharma","Priya Patel","Amit Kumar","Sneha Reddy","Vikram Singh",
    "Anita Desai","Rohan Mehta","Kavita Nair","Suresh Iyer","Meera Joshi",
    "Arjun Verma","Divya Rao","Karan Chopra","Pooja Kapoor","Nikhil Gupta",
    "Riya Banerjee","Aditya Malhotra","Neha Singh","Sameer Khan","Pallavi Deshmukh",
]

REVIEW_TEXTS = [
    "Excellent service, professional team, highly recommend.",
    "On time, reasonable pricing, would hire again.",
    "Prompt response, quality work, satisfied with the service.",
    "Very professional, handled the job quickly and efficiently.",
    "Good experience overall, would recommend to colleagues.",
    "Reliable team, transparent pricing, no hidden charges.",
    "Great communication and follow-up, solved our issue.",
    "Clean work, courteous staff, will use again.",
    "Fast turnaround, competitive rates, professional attitude.",
    "Positive experience from start to finish.",
]

CLIENT_COMPANIES = [
    "Aurelia Industries","Bharatline Logistics","Crestview Corp",
    "Duneshore Retail","Eastway Manufacturing","Falconfield Tech",
    "Greenacre Foods","Havenbrook Realty","Induspoint Chemicals",
    "Junction Motors","Kingsway Pharma","Lighthouse Media",
    "Meadowridge IT","Northgate Auto","Opalstone Builders",
    "Pinecrest Hotels","Quarrylane Steel","Riverstone Textiles",
    "Silverbrook Bank","Thornfield Energy","Unionbay Shipping",
    "Valleyforge Cement","Westmark Foods","Yarrowhill Retail",
]

def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def phone():
    return f"+91 {random.randint(70,99)}{random.randint(10000000,99999999)}"

def gen_name(cat_name, used):
    for _ in range(200):
        p = random.choice(PREFIXES)
        s = random.choice(SUFFIXES)
        base = cat_name.split("&")[0].split("/")[0].strip()
        n = f"{p} {base} {s}"
        if n not in used:
            used.add(n)
            return n
    return f"{cat_name} {random.randint(1000,9999)}"

def gen_client(cat, idx, used):
    name = gen_name(cat["name"], used)
    city, state = random.choice(CITIES)
    ph = phone()
    r = random.random()
    tier = "Featured" if r < 0.15 else ("Premium" if r < 0.40 else "Standard")
    slug = slugify(name)
    return {
        "_dummy": True,
        "id": slug,
        "name": name,
        "tagline": f"Trusted {cat['name'].lower()} provider serving businesses across {city}.",
        "category": cat["slug"],
        "tier": tier,
        "order": idx + 1,
        "city": city,
        "area": state,
        "rating": round(random.uniform(4.0, 5.0), 1),
        "reviewCount": random.randint(5, 120),
        "since": random.randint(2005, 2022),
        "experience": f"{random.randint(3, 20)}+ Years",
        "status": "Verified",
        "phone": ph,
        "whatsapp": ph,
        "email": f"info@{slug[:20]}.example.com",
        "website": f"https://{slug[:20]}.example.com",
        "address": f"{random.randint(1,999)} {random.choice(['MG Road','Industrial Area','Sector 5','MIDC','Main Road'])}, {city}",
        "hours": "Mon-Sat: 9 AM - 7 PM",
        "mapUrl": f"https://maps.google.com/?q={city}",
        "about": [
            f"{name} is a leading {cat['name'].lower()} provider based in {city}, {state}. "
            f"With {random.randint(3,20)}+ years of experience, we serve corporate offices, "
            f"factories, warehouses, and commercial establishments with reliable, professional service."
        ],
        "services": [
            f"{cat['name']} Consultation",
            f"{cat['name']} Service",
            f"{cat['name']} Maintenance",
            "Annual Maintenance Contract",
            "Emergency Support",
        ],
        "catalogues": [
            {"title": "Product Catalogue", "subtitle": "Full product range", "url": "https://example.com/cat1.pdf"},
            {"title": "Price List",         "subtitle": "Current pricing",    "url": "https://example.com/cat2.pdf"},
        ],
        "clients": random.sample(CLIENT_COMPANIES, 3),
        "reviews": [
            {"name": random.choice(REVIEWERS), "rating": 5, "text": random.choice(REVIEW_TEXTS)}
            for _ in range(2)
        ],
        "social": {"facebook": "", "instagram": "", "youtube": ""},
    }

def main():
    with open(cats_file, encoding="utf-8") as f:
        cats_data = json.load(f)

    total = 0
    for cat in cats_data["categories"]:
        used = set()
        clients = [gen_client(cat, i, used) for i in range(PER_CATEGORY)]
        out_file = out_dir / f"DUMMY-{cat['slug']}.json"
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(clients, f, indent=2, ensure_ascii=False)
        total += len(clients)

    print(f"Generated {total} dummy clients across {len(cats_data['categories'])} categories")

    # Remove the old single-file sample if present
    old = out_dir / "clients-01.json"
    if old.exists():
        old.unlink()
        print("Removed legacy clients-01.json sample")

if __name__ == "__main__":
    main()
