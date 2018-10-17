from bs4 import BeautifulSoup
import sys
import io
import urllib.parse as rep
import urllib.request as req
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

opener = req.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
req.install_opener(opener)

srcItem = input('검색어 입력 : ')
base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
param = rep.quote_plus(srcItem)
url = base + param
savePath = "e:\\imageDown\\"

try:
    if (not os.path.isdir(savePath)):
        os.makedirs(os.path.join(savePath))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더만들기 실퍠")
        raise

html = req.urlopen(url)
soup = BeautifulSoup(html, "html.parser")
img_list = soup.select("div.img_area > a.thumb._thumb > img")
for i,il in enumerate(img_list,1):
    #print(il['data-source'])
    fullFileName = os.path.join(savePath, srcItem+str(i)+'.jpg')
    req.urlretrieve(il['data-source'], fullFileName)

print('다운로드 완료')
