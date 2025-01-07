from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time


def website_scraper(website_url):
    print("Connecting to Chrome...")

    chrome_driver_path = "./chromedriver"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website_url)
        print("Loading website...")
        html = driver.page_source
        time.sleep(10)

        return html

    except Exception as e:
        print(f"Error: {e}")
        driver.quit()
        return


def extract_body_content(html):
    """
    Extracts the body content from the given HTML.
    """
    soup = BeautifulSoup(html, "html.parser")
    body = soup.body
    if body:

        return str(body)
    else:
        return "No body content found"


def clean_body_content(body):
    """
    Cleans the body content by removing scripts and styles, and formatting the text.
    """
    soup = BeautifulSoup(body, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    clean_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in clean_content.splitlines() if line.strip()
    )

    return cleaned_content


def chunk_cleaned_content(cleaned_content, chunk_size=6000):
    """
    Chunks the cleaned content into smaller parts based on the specified chunk size.
    """
    return [
        cleaned_content[x : x + chunk_size]
        for x in range(0, len(cleaned_content), chunk_size)
    ]
