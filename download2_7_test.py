from bs4 import BeautifulSoup
import sys
import io
import urllib.parse as rep
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://www.daum.net/"
html = req.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

top = soup.select("ol.list_mini  > li")
#print(top)

for i,e in enumerate(top,1):
    print(i,"위 ",e.select_one("span.txt_issue").string," : ", e.select_one("a.link_issue").attrs['href'])
