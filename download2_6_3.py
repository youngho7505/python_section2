from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp = open("cars.html",encoding='utf-8')
bsObj = BeautifulSoup(fp, "html.parser")
print(bsObj.select("li")[3].string)
print(bsObj.find_all("li")[3].string)
print(bsObj.find_all("li")[3].attrs['id'])
def car_func(selector):
    print("selected car >>", bsObj.select_one(selector).string)

car_func("li#ge")
car_func("#av")
car_func("ul > #so")
car_func("ul > li#tu")
car_func("#cars > li#gr")
car_func("ul#cars > li#av")
car_func("#cars #ge")
car_func("li[id='gr']")
car_func("li:nth-of-type(2)")
