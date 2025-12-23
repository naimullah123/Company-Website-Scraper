import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re
from datetime import datetime

MAX_PAGES = 12

def scrape_company(url):
    visited = set()
    pages_crawled = []
    errors = []

    data = {
        "identity": {
            "company_name": "Not found",
            "website_url": url,
            "tagline": "Not found"
        },
        "business_summary": {
            "what_they_do": "Not found",
            "primary_offerings": [],
            "target_customers": []
        },
        "evidence_proof": {
            "key_pages_detected": [],
            "signals_found": [],
            "social_links": []
        },
        "contact_location": {
            "emails": [],
            "phones": [],
            "address": "Not found",
            "contact_page": "Not found"
        },
        "team_hiring": {
            "careers_page": "Not found",
            "roles_detected": []
        },
        "metadata": {
            "timestamp": datetime.utcnow().isoformat(),
            "pages_crawled": [],
            "errors_or_fallbacks": []
        }
    }

    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        if soup.title:
            data["identity"]["company_name"] = soup.title.text.strip()

        paragraphs = soup.find_all("p")
        if paragraphs:
            data["business_summary"]["what_they_do"] = paragraphs[0].text.strip()

        links = soup.find_all("a", href=True)
        internal_links = []

        domain = urlparse(url).netloc

        for a in links:
            full_url = urljoin(url, a["href"])
            if domain in full_url and full_url not in visited:
                internal_links.append(full_url)

        priority_keywords = ["about", "product", "solution", "industry", "pricing", "career", "contact"]

        for link in internal_links:
            if len(visited) >= MAX_PAGES:
                break

            if any(k in link.lower() for k in priority_keywords):
                visited.add(link)
                pages_crawled.append(link)

                if "career" in link.lower():
                    data["team_hiring"]["careers_page"] = link

                if "contact" in link.lower():
                    data["contact_location"]["contact_page"] = link

                data["evidence_proof"]["key_pages_detected"].append(link)

    except Exception as e:
        errors.append(str(e))

    data["metadata"]["pages_crawled"] = pages_crawled
    data["metadata"]["errors_or_fallbacks"] = errors

    return data
