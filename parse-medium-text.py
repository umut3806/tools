import sys
import requests
from bs4 import BeautifulSoup

def parse_medium_page(url):
    # Fetch the HTML content of the Medium page
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch the page.")
        return
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract all headers and titles excluding images
    headers_and_titles = []
    for element in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']):
        if element.name == 'img':
            continue
        text = element.get_text().strip()
        if text:
            headers_and_titles.append(text)
    
    return headers_and_titles

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    parsed_content = parse_medium_page(url)
    for item in parsed_content:
        print(item)
