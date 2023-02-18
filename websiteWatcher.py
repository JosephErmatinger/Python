import time
import hashlib
from urllib.request import urlopen, Request

url = Request('https://realpython.com/urllib-request/'
      headers={'User-Agent': 'Mozilla/5.0'})

response = urlopen(url).read()

currentHash = hashlib.sha224(response).hexdigest()
print("Program Running")
time.sleep(10)
while True:
	try:
		response = urlopen(url).read()
		currentHash = hashlib.sha224(response).hexdigest()

		time.sleep(60)

		response = urlopen(url).read()
		newHash = hashlib.sha224(response).hexdigest()

		if newHash == currentHash:
			continue
		else:
			print("Website changed")
			response = urlopen(url).read()
			currentHash = hashlib.sha224(response).hexdigest()
			time.sleep(30)
			continue
	except Exception as e:
		print("error")
        
with open("url.txt") as file:
  for url in file:
    print(url)
    response = urlopen(url).read()
    