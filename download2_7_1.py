from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://finance.daum.net/?nil_stock=refresh"
html = req.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
jongmok = soup.select("ul#topMyListNo1 > li")

for i,e in enumerate(jongmok,1):
    print(i,e.find("a").string," : ",e.find("span").string," : ",e.select_one(".rate > span").string)
