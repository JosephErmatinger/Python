list = ["https://www.w3schools.com/python/trypython.asp?filename=demo_function_param3", "https://github.com/oz123/awesome-c", "https://www.oracle.com/database/"]

def display():
print("Open Function")
with open("url.txt") as file:
  for url in file:
    print(url)
    
def open(urls):
  print("Open Function")
  for x in urls:
    print(x)
    return x
    
print("Program Started")
display()
open(list)
print("Program Finished")
