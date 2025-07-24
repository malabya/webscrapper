import argparse
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
from urllib.parse import urlparse

def scrape_selector(url, selector):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch page: {response.status_code}")
        return []
    soup = BeautifulSoup(response.text, "html.parser")
    elements = soup.select(selector)
    return [element.get_text(strip=True) for element in elements]

def save_to_csv(data, source_url, filename="scraped_data.csv"):
    domain = urlparse(source_url).netloc
    timestamp = datetime.now().isoformat()
    with open(filename, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow([timestamp, domain, row])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape elements matching a CSS selector and append results to a CSV.")
    parser.add_argument("url", help="Target URL")
    parser.add_argument("selector", help="CSS selector to extract")
    args = parser.parse_args()

    results = scrape_selector(args.url, args.selector)
    if results:
        save_to_csv(results, args.url)
        print(f"{len(results)} items appended to scraped_data.csv.")
    else:
        print("No data found.")
