# Company-Website-Scraper
Overview

This project is a lightweight web scraper that converts a company website URL into a structured Company Info Record.

The goal is not exhaustive scraping, but reliable extraction of business-relevant signals such as:

1.What the company does

2.Its offerings and target customers

3.Proof points (pages, signals, social links)

4.Contact and hiring signals

The system prioritizes truthful extraction, explicitly marking data as "Not found" when unavailable.

Objective

Input:

A single company website URL (publicly accessible)

Output:

A structured JSON-like object containing:

*Company identity

*Business summary


*Evidence & proof signals

*Contact & location details

*Hiring signals

*Scrape metadata

Features

Scrapes only publicly accessible pages (no logins)

Crawls a maximum of 10–15 internal pages

Prioritizes business-critical pages:

/about, /products, /solutions, /industries, /pricing, /contact, /careers

Handles:

Timeouts

Broken links

Missing pages

Logs limitations transparently (e.g., JS-heavy sites)

Tech Stack

Python 3.9+

requests

BeautifulSoup4
