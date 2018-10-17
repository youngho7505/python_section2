from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp = open("food-list.html",encoding='utf-8')
bsObj = BeautifulSoup(fp, "html.parser")

print("1", bsObj.select_one("li:nth-of-type(8)").string) #li(8번째 리스트태그의 스트링 값을 가져옴)
print("2", bsObj.select_one("#ac-list > li:nth-of-type(4)").string)
print("3", bsObj.select("#ac-list > li[class='alcohol']")[3].attrs['data-lo'])
print("4", bsObj.select("#ac-list > li.alcohol.high")[0].string)
param = {"data-lo":"cn","class":"alcohol"}
print("5", bsObj.find("li",param).string)
print("6", bsObj.find(id="ac-list").find("li", param).string)

for ac in bsObj.find_all("li"):
    if ac['data-lo'] == 'ko':
        print(ac.string, ac.attrs['class'][0])
