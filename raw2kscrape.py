import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import urllib.request
from csv import reader, writer

car = []

indexmachine = {}
var = 1

weburl = f"https://www.raw2k.co.uk/vehicle-auctions?ends=2&starts=yes&page={var}"

res = requests.get(weburl)

if res:
	soup = BeautifulSoup(res.text, "html.parser")
	results = soup.find(id="searchlistings")

tags = {tag.name for tag in results.find_all()} # a way to get the tags associated with the link, using tuple comprehensiom to avoid duplocates killing the screen

#print(tags)

carnames = results.find_all('div', class_ = 'col listingitem s12 bargain')

#working
for n in range (11):
	weburl = f"https://www.raw2k.co.uk/vehicle-auctions?ends=2&starts=yes&page={var}"
	res = requests.get(weburl)
	print(f'\npage {n + 1}')
	var = var+1

	if res:
		soup = BeautifulSoup(res.text, "html.parser")
		results = soup.find(id="searchlistings")

	carnames = results.find_all('div', class_ = 'col listingitem s12 bargain')
	for l in carnames:
		if l.has_attr('data-title'): #find the attribute
			indexer = l.attrs['data-title'] #use the attribute
	
		if l.has_attr('data-category'):
			datacag = l.attrs['data-category']
	
		if l.has_attr('data-drives'):
			datadr = l.attrs['data-drives']
	
		if l.has_attr('data-starts'):
			datast = l.attrs['data-starts']
	
		if l.has_attr('data-odometer'):
			dataodom = l.attrs['data-odometer']
	
		if l.has_attr('data-price'):
			price = l.attrs['data-price']
	
		if l.has_attr('data-transmission'):
			transmission = l.attrs['data-transmission']
	
		if l.has_attr('data-type'):
			saloon = l.attrs['data-type']

		if l.has_attr('data-fuel'):
			fuel = l.attrs['data-fuel']

		if l.has_attr('href'):
			print(l.attrs['href'])

		print(f'Car: {indexer}, Strts? {datast}, Drv? {datadr}, Cat: {datacag}, Odom: {dataodom}, Price: £{price}, Tran: {transmission}, type? It is a {fuel} {saloon}')

	time.sleep(2)


# for i in sinps:
# 	if i.has_attr("class"): #attribute searching
# 		i.find_all()
# file = open('cars.txt', 'w')
# file.write(results.prettify())
# file.close()