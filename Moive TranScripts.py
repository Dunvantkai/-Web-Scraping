from bs4 import BeautifulSoup
import requests

website = input("Please Enter the websites url or type eg for the exsaple website")
if website == "eg":
    website = ("https://subslikescript.com/movie/Shrek-126029")
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())