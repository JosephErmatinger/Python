import time
import hashlib
from urllib.request import urlopen, Request

print("Program Running")

with open("url.txt") as file:
  for url in file:
    print(url)
    response = urlopen(url).read()
    hash1 = hashlib.sha224(response).hexdigest()
    response = urlopen(url).read()
    hash2 = hashlib.sha224(response).hexdigest()
    
print("Program Finished")
