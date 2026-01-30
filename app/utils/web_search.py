import requests
import trafilatura
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from langchain_community.utilities import SerpAPIWrapper
import os

openai_api_key = os.getenv("OPENAI_API_KEY")
serpapi_api_key = os.getenv("SERPAPI_API_KEY")

# ---------- helpers ----------

def fetch_html(url: str) -> str | None:
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; FinSage/1.0)"
        }
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        return r.text
    except Exception:
        return None


def extract_text(html: str) -> str:
    # Primary extractor
    text = trafilatura.extract(
        html,
        include_comments=False,
        include_tables=False
    )
    if text and len(text) > 200:
        return text

    # Fallback extractor
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()
    return soup.get_text(separator=" ", strip=True)


def get_domain(url: str) -> str:
    return urlparse(url).netloc.replace("www.", "")

# ---------- main function ----------

def process_serp_results(results: dict, max_articles: int = 20) -> list[dict]:
    """
    Processes SerpAPI results into clean article texts.

    Returns:
    [
      {
        "url": str,
        "title": str,
        "source": str,
        "snippet": str,
        "content": str
      }
    ]
    """

    processed = []
    seen_urls = set()

    # SerpAPI may return results under different keys
    organic_results = results.get("organic_results", []) \
                      or results.get("news_results", [])

    for item in organic_results:
        if len(processed) >= max_articles:
            break

        url = item.get("link")
        if not url or url in seen_urls:
            continue

        seen_urls.add(url)

        html = fetch_html(url)
        if not html:
            continue

        content = extract_text(html)
        if len(content) < 300:
            continue  # skip low-signal pages

        processed.append({
            "url": url,
            "title": item.get("title", ""),
            "source": get_domain(url),
            "snippet": item.get("snippet", ""),
            "content": content
        })

    return processed

def search_scrape(company: str):
    serp = SerpAPIWrapper(
        serpapi_api_key=serpapi_api_key,
        params={
            "engine": "google_news",
            "num": 50,
            "hl": "en",
            "sort_by": "date"
        }
    )

    results = serp.results(f"{company} earnings OR layoffs OR acquisition")
    articles = process_serp_results(results)
    content = "\n\n".join([a["content"] for a in articles])
    return content