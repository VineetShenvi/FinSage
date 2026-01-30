from newspaper import Article

def scrape_url(url: str) -> str:
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception:
        return ""
