from bs4 import BeautifulSoup
import requests
website = input("Please Enter the websites url or type eg for the exsaple website: ")
if website == "eg":
    website = ("https://warthunder.com/en")
result = requests.get(website)
content = result.text
print(content)
EXIT = input("Done. Press Enter to Exit the Program")
txtfile = open("Website.txt", "w", encoding="utf-8") 
txtfile.write(content)
htmlfile = open("Website.html", "w", encoding="utf-8") 
htmlfile.write(content)
EXIT = input("Done. Press Enter to Exit the Program")