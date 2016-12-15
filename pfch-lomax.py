from bs4 import BeautifulSoup
import requests
import json
import csv

recordings = []

#GOALS: 
#1. organize by description 
#2. scrape all the individual recording pages
#3. find year and location of each one 
#4. place in map/timeline 
#5. import other relevant data?

current_page = 10000
#how do i scrape multiple pages when i dont know the total number of pages or the order of the pages?
#if else
	#continue

while current_page <= 21649:

	url = "http://research.culturalequity.org/get-audio-detailed-recording.do?recordingId=" + str(current_page)
	#url = "http://research.culturalequity.org/get-audio-detailed-recording.do?recordingId=21649"
	print(url)
	current_page = current_page + 1
	#problem with while loop ---> how do i loop through each page and then stop the loop?

	alan_lomax = requests.get(url)
	page_url = alan_lomax.text
	lomax_scrape = BeautifulSoup(page_url, "html.parser")

	#data = lomax_scrape.find_all(text=True)
	trs = lomax_scrape.find_all("tr")
	a_recording = {}
	for recording_info in trs:
	#print(recording_info)
		scrape = recording_info.find_all("td")
		if len(scrape) != 0:
			if ":: Title ::" in scrape[0].text:
				a_recording["Title"] = scrape[1].text
			if ":: Performers & Instruments ::" in scrape[0].text:
				a_recording["Artist"] = scrape[1].text	
			if ":: Group Name ::" in scrape[0].text:
				a_recording["Group"] = scrape[1].text
			if ":: Location ::" in scrape[0].text:
				a_recording["Location"] = scrape[1].text
			if ":: Date ::" in scrape[0].text:
				a_recording["Date"] = scrape[1].text
			if current_page >= 10000:
				a_recording["Page"] = current_page #page id (page number) into recording data

	if "Title" in a_recording:
		recordings.append(a_recording)
	#print(recordings)	
		#for x in scrape:
		#	print(x.text)

	with open("recordings.json", "w") as outfile:
		outfile.write(json.dumps(recordings, indent=4))







