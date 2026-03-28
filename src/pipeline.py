import asyncio
import re

from src.query_builder import build_queries
from src.serp import search_links
from src.scraper import scrape_all
from src.ai import extract_ai_batch
from src.scorer import score_lead, is_good
from src.saver import save


def run_pipeline(profession, location=None):

    print(f"🔍 {profession} | {location}")

    queries = build_queries(profession, location)

    all_links = []
    for q in queries:
        all_links.extend(search_links(q))

    print(f"🌐 Total links: {len(all_links)}")

    import random
    # Shuffle to ensure we get a mix of LinkedIn, Facebook, Instagram, Reddit etc.
    random.shuffle(all_links)
    
    print(f"🌐 Processing all {len(all_links)} mixed links from all platforms...")
    pages = asyncio.run(scrape_all(all_links))

    print("🤖 Processing all pages in one AI batch request...")
    ai_batch_results = extract_ai_batch(pages)

    results = []

    for url, text in pages.items():

        emails = re.findall(r"\S+@\S+", text)
        phones = re.findall(r"\+?\d[\d\s\-]{8,}\d", text)

        ai = ai_batch_results.get(url, {})

        lead = {
            "name": ai.get("name"),
            "company": ai.get("company"),
            "url": url,
            "email": ai.get("email") or (emails[0].strip() if emails else ""),
            "phone": ai.get("phone") or (phones[0].strip() if phones else "")
        }

        lead["score"] = score_lead(lead)

        if not is_good(lead):
            continue

        results.append(lead)

    save(results)

    print("✅ Done! Check output/leads.csv")