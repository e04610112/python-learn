import requests




def login():
    url="http://10.213.3.130:8080/RESTful/login"
    params={
        "password": "string",
        "userName": "yjlin03"
    }
    req=requests.post(url,None,params,timeout=2)
    print "reqtext:"+req.text
    data=req.json()['data']['access_token']
    print data
    return data