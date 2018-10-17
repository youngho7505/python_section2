import sys
import io
import urllib.request as req
from urllib.parse import urlencode

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

api = "https://api.ipify.org"
#api = "http://ip-api.com/json"
values = {
    'format' : 'json'
}
#print("before" ,values)
params = urlencode(values)
#print("after", params)

url = api + '?' + params
#print(url)
reqData = req.urlopen(url).read().decode('utf-8')
print(reqData)
