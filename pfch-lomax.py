from bs4 import BeautifulSoup
import requests
import json

recordings = []

current_page = 0

url = "http://research.culturalequity.org/get-audio-detailed-recording.do?recordingId=21649" #current_page+1
#problem with while loop ---> how do i loop through each page and then stop the loop?

alan_lomax = requests.get(url)
page_url = alan_lomax.text
lomax_scrape = BeautifulSoup(page_url, "html.parser")

data = lomax_scrape.find_all(text=True)
trs = lomax_scrape.find_all("tr")

for recording_info in trs:
#print(recording_info)
	scrape = recording_info.find_all("td")
	for x in scrape:
		print(x.text)

	





































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