from bs4 import BeautifulSoup
import sys
import io
import re #regex

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
    <html>
        <body>
            <ul>
                <li><a id="naver" href="http://www.naver.com">naver</a></li>
                <li><a href="http://www.daum.net">Daum</a></li>
                <li><a href="http://www.daum.com">Daum</a></li>
                <li><a href="https://www.google.com">Google</a></li>
                <li><a href="https://www.tistory.com">Tistory</a></li>
            </ul>
        </body>
    </html>
"""

bsObj = BeautifulSoup(html, "html.parser")
print(bsObj.find(id="naver").attrs['href'])
print(bsObj.find_all(href=re.compile(r"da")))
links = bsObj.find_all(href=re.compile(r"^http"))
#links = bsObj.find_all(href=re.compile(r"^https://"))
for i in links:
    href = i.attrs['href']
    txt = i.string
    print(txt, " - ", href)
