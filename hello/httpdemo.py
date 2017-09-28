import requests

def baidu_func(url):
    headers={}
    params={}
    req=requests.get(url, headers=headers, params=params)
    req.encoding='utf-8'
    print (req.status_code)
    print (req.text)
    print (req.cookies)

url="http://10.213.3.130:8080/swagger-ui.html"
baidu_func(url)