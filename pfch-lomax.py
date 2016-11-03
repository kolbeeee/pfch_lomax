from bs4 import BeautifulSoup
import requests

url = "http://research.culturalequity.org/get-audio-ix.do?ix=session&id=11&idType=collectionId&sortBy=abc"

bessie_jones = requests.get(url)
page_url = bessie_jones.html

jones_scrape = BeautifulSoup(page_html, "html.parser")

dates = soup.findall("td": "class", attrs={"a": "href"})

	for recordings in dates:
		print(dates)