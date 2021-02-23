import requests


class demo:
    r = requests.get('http://httpbin.testing-studio.com/get')
    print("json:" + r.json())
    print("json:" + r.text)
    print("request:" + r.request)
    print("cookies:" + r.cookies)
    print("headers:" + r.headers)
    assert r.status_code == 200
