import requests  #request kütüphanesini içe aktardım

from bs4 import BeautifulSoup  #bs4 paketi içerisinden BeautifulSoup sınıfını içe aktardım

headers_param= {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Safari/605.1.15"}  #istek gönderilen sitenin bot algılamasını engelledim

glasdor= requests.get("https://quotes.toscrape.com")  #sayfanın içeriğini istedim ve glasdor değişkenine atadım

print(glasdor.status_code)  #sayfa içeriğini başarıyla aldım (200)

jobs= (glasdor.content)  #sayfanın içeriğini ham veri (bytes) olarak aldım
soup= BeautifulSoup(jobs,"html.parser") #ham veriyi BeautifulSoup ile parçaladım ve Python’un anlayacağı bir obje hâline getirdim

print((soup.find("a")).text) #HTML içindeki ilk <a> etiketini buldum ve içerisindeki metni çektim. Bu sayfanın en üstündeki ana başlıktır.


all_jobs=soup.find_all("div",class_="quote") #tüm <div> etiketli ve "quote" sınıflı parçaları çektim