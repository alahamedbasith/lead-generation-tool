import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def fetch(session, url):
    try:
        async with session.get(url, timeout=10) as res:
            html = await res.text()
            soup = BeautifulSoup(html, "html.parser")
            # Remove scripts and styles
            for script_or_style in soup(["script", "style"]):
                script_or_style.decompose()
            text = soup.get_text(separator=" ", strip=True)
            return url, text
    except:
        return url, ""

async def scrape_all(urls):
    connector = aiohttp.TCPConnector(limit=10)

    async with aiohttp.ClientSession(
        connector=connector,
        headers={"User-Agent": "Mozilla/5.0"}
    ) as session:

        tasks = [fetch(session, u) for u in urls]
        results = await asyncio.gather(*tasks)

        return dict(results)