from bs4 import BeautifulSoup
import requests
import json

recordings = []

url = "http://research.culturalequity.org/get-audio-detailed-recording.do?recordingId=23457"

alan_lomax = requests.get(url)
page_url = alan_lomax.text

lomax_scrape = BeautifulSoup(page_url, "html.parser")

trs = lomax_scrape.find_all("tr")

for recording_info in trs:
	print(recording_info)

	data = recording_info.find_all("td", attrs={"class": "NormalPad5"})
	for td in data:
		print(td.text)

	





































#url = "http://research.culturalequity.org/get-audio-ix.do?ix=session&id=11&idType=collectionId&sortBy=abc"

#bessie_jones = requests.get(url)
#page_url = bessie_jones.text

#jones_scrape = BeautifulSoup(page_url, "html.parser")

#trs = jones_scrape.find_all("tr", attrs={"class":"odd"})

#for recordings in trs:
	#print(recordings)

#	tds = recordings.find_all("td")
#	name = tds[0].text



	#artist = findall("a"})
	#date = findall("td", attrs={"class":"displayTagTDCol"})
	#location = findall("")