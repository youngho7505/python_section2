from bs4 import BeautifulSoup
import sys
import io
import urllib.parse as rep
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

baseUrl = "https://www.inflearn.com/"
param = rep.quote_plus("추천-강좌")
url = baseUrl+param
html = req.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

top10 = soup.select("ul.slides")[0]

for i,e in enumerate(top10,1):
    print(i, e.select_one("h4.block_title > a").string)
