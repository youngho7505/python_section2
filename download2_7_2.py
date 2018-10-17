from bs4 import BeautifulSoup
import sys
import io
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://finance.naver.com/sise/"
html = req.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
top = soup.select("table#siselist_tab_0 > tr")
#top = soup.select("table#siselist_tab_0 > tr > td > a")

i = 1
for e in top:
    if e.find("a") is not None:
        print(i, e.select_one(".tltle").string)
        print(e.select_one("td:nth-of-type(9)").string)
        print(e.select_one("td:nth-of-type(10)").string)
        print(e.select_one("td:nth-of-type(11)").string)
        i += 1

#for i,e in enumerate(top,1):
#    print(i, e.string)
