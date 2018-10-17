import sys
import io
import urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "https://ssl.pstatic.net/tveta/libs/1207/1207266/3e27ac22eb1cbce02b24_20181004171952011.png"
filePath1 = "e:/download/naver_image.jpg"
videoUrl = 'https://movie.naver.com/movie/bi/mi/mediaView.nhn?code=164147&mid=40158#'
filePath2 = "e:/download/son.mp4"

urllib.request.urlretrieve(imgUrl, filePath1)
urllib.request.urlretrieve(videoUrl, filePath2)


print('다운로드 및 저장 완료!')
