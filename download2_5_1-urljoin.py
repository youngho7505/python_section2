from urllib.parse import urljoin

baseUrl = "http://www.test.com/html/a.html"
print(">> ", urljoin(baseUrl, "b.html"))
print(">> ", urljoin(baseUrl, "sub/b.html"))
print(">> ", urljoin(baseUrl, "../index.html"))
print(">> ", urljoin(baseUrl, "../img/image.jpg"))
print(">> ", urljoin(baseUrl, "../css/style.css"))
