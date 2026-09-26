import re
from collections import Counter

EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
URL_RE = re.compile(r"https?://[^\s]+")
DATE_RE = re.compile(r"\b(\d{1,2}/\d{1,2}/\d{2,4}|\d{4}-\d{2}-\d{2})\b")

NAMES = {"avery", "jordan", "casey", "taylor", "riley", "morgan"}
COMPANIES = {"orbit labs", "northwind", "solstice", "atlas", "aurora"}


def extract_entities(text):
    emails = EMAIL_RE.findall(text)
    urls = URL_RE.findall(text)
    dates = DATE_RE.findall(text)

    words = re.findall(r"[a-zA-Z]+", text.lower())
    names = [word for word in words if word in NAMES]
    companies = []
    for company in COMPANIES:
        if company in text.lower():
            companies.append(company)

    return {
        "emails": emails,
        "urls": urls,
        "dates": dates,
        "names": list(Counter(names).keys()),
        "companies": companies,
    }
