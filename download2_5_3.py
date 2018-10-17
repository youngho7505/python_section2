from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

html = """
    <html>
        <body>
            <ul>
                <li><a href="http://www.naver.com">naver</a></li>
                <li><a href="http://www.daum.net">Daum</a></li>
                <li><a href="http://www.daum.com">Daum</a></li>
                <li><a href="https://www.google.com">Google</a></li>
                <li><a href="https://www.tistory.com">Tistory</a></li>
            </ul>
        </body>
    </html>
"""

bsObj = BeautifulSoup(html, "html.parser")
links = bsObj.find_all("a")
#links1 = bsObj.find_all("a", string="Daum")
#links2 = bsObj.find_all("a", limit=3)
#links4 = bsObj.find_all(string=["naver","Google"])
#print(links1)
#print(links2)
#print(links4)
for a in links:
    #print('a',type(a),a)
    href = a.attrs['href']
    txt = a.string
    print("txt >> ",txt,", href >> ", href)
