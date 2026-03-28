from serpapi import GoogleSearch
from src.settings import SERP_API_KEY

def search_links(query):
    links = []

    for page in range(2):
        params = {
            "engine": "google",
            "q": query,
            "start": page * 10,
            "api_key": SERP_API_KEY,
            "tbs": "qdr:w"  # latest results (last week)
        }

        results = GoogleSearch(params).get_dict()

        for r in results.get("organic_results", []):
            links.append(r["link"])

    return links