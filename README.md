# Webscraper Project

A simple Python 3 project to scrape elements from any given URL using a CSS selector. Results are appended to a CSV file for reuse and tracking.

## Prerequisites

- **Python 3.7+** (verify with `python3 --version`)
- **pip** (Python package manager)
- **Git** (for cloning the repository)
- **macOS** (instructions are specific, but adaptable to Linux)

## 1. Clone the Repository
```
git clone https://github.com/your-username/webscraper.git
cd webscraper
```

## 2. Setup a Virtual Environment
```
python3 -m venv venv source venv/bin/activate
```

## 3. Install Dependencies
```
pip install -r requirements.txt
```

## 4. Run the Scraper

The script takes two arguments:

- The **URL** (in quotes; include query parameters as needed)
- The **CSS selector** for the elements you want to extract

Example:

```
python3 scraper.py “https://www.example.com” “h2 > a”
```

### Output

- All elements matching the selector are printed to the console.
- Each result is appended as a new row in `scraped_data.csv` in the project directory.
- Each row contains a timestamp, the website domain, and the text of the selected element.

#### Sample Output on Terminal

```
50 items appended to scraped_data.csv.
```

## 5. Example of CSV Contents

| Timestamp           | Domain          | Extracted Value    |
|---------------------|-----------------|--------------------|
| 2025-07-24T23:17:00 | www.example.com  | Value 1              |
| 2025-07-24T23:17:00 | www.example.com  | Value 2     |

## Notes

- To **deactivate** the virtual environment, run:
```
deactivate
```
---
- If you re-run the script, new data is **appended** to `scraped_data.csv` without removing old data.
- All dependencies are local to your project; global Python packages are unaffected.
- The script is designed for static web pages. For JavaScript-heavy pages, consider enhancements with Selenium.

## Troubleshooting

- Make sure your selector matches elements on the page—inspect and test in your web browser first.
- If you encounter SSL or connection errors, ensure you have internet access and the page is reachable.

Happy scraping!
