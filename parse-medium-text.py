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

# Example usage:
medium_url = 'https://medium.com/@umutbayram380606/dogcat-medium-tryhackme-partial-solution-d80eaa98c806'
parsed_content = parse_medium_page(medium_url)
for item in parsed_content:
    print(item)
