#For my first project, I used Quotes to Scrape, a site designed for data extraction practice. This little project is my first attempt at data extraction.

import requests  #Imported the request library

from bs4 import BeautifulSoup  #Imported the BeautifulSoup class from the bs4 library

headers_param= {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Safari/605.1.15"}  #Prevented the target website from detecting the request as a bot

glasdor= requests.get("https://quotes.toscrape.com")  #Requested the page content and stored it in the 'glasdor' variable

print(glasdor.status_code)  #Successfully retrieved the page content and printed the response (200)

quotes= glasdor.content  #Retrieved the page content as raw data (bytes) and stored it in the 'quotes' variable
soup= BeautifulSoup(quotes,"html.parser") #Parsed the raw data with BeautifulSoup, converted it into a Python-readable object, and stored it in the 'soup' variable

print(soup.find("a").text) #Extracted and printed the text of the first <a> tag (page's main title)

print(soup.find_all("div")) #Extracted all <div> tags from the HTML and printed their content

all_quotes=soup.find_all("div",class_="quote") #Extracted all <div class="quote"> blocks and saved them into a variable

for quote in all_quotes:
    print(quote.find("small", class_="author").text)  #Used a for loop to extract the text of <small> elements with class "author" from each quote block and printed them. These are the authors of the quotes.

for quote in all_quotes:
    print(quote.span.text) #Used a for loop to extract the text of <span> elements from each quote block and printed them. These are the quote texts.

for quote in all_quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    print(f"{text} — {author}") #Displayed each quote and its corresponding author together on one line




