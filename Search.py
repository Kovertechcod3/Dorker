import requests
from bs4 import BeautifulSoup


def scrape_google_search(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    results = []

    # Extract search results
    search_results = soup.find_all("div", class_="g")
    for result in search_results:
        title = result.find("h3").text
        link = result.find("a")["href"]
        snippet = result.find("span", class_="aCOpRe").text
        item = {
            "title": title,
            "link": link,
            "snippet": snippet
        }
        results.append(item)

    return results
