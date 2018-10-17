import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "http://blogfiles.naver.net/20140204_137/friderike_13915211608965CKS4_JPEG/37b4477c6e10c3b0cfeca5150509fc62.jpg"
htmlUrl = "http://google.com"
savePath1 = "e:/download/test3.jpg"
savePath2 = "e:/download/google.html"

f = dw.urlopen(imgUrl).read()

saveFile1 = open(savePath1, 'wb') # w : write, r : read, a : add
saveFile1.write(f)
saveFile1.close()

with open(savePath1, 'wb') as saveFile1:
    saveFile1.write(f)

f2 = dw.urlopen(htmlUrl).read()

saveFile2 = open(savePath2, 'wb')
saveFile2.write(f2)
saveFile2.close()

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)

print('다운로드 완료')
