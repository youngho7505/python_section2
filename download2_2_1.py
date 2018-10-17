import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "http://blogfiles.naver.net/20140204_137/friderike_13915211608965CKS4_JPEG/37b4477c6e10c3b0cfeca5150509fc62.jpg"
htmlUrl = "http://google.com"
savePath1 = "e:/download/test2.jpg"
savePath2 = "e:/download/index.html"

dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlUrl, savePath2)

print('다운로드 완료')
