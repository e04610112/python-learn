#!/usr/bin/env python
import LoginUtil
import requests

cookie=LoginUtil.login()

url="http://10.213.3.130:8080/RESTful/cust/fuzzySearchClientList"
params={
    "term": "",
    "userId": "yjlin03"
}

cookies={}
cookies["access_token"]=cookie

req=requests.get(url,params=params,timeout=2,cookies=cookies)
print req.text








