import requests
import pystache
import jsonpath
import yaml


class Test_demo:
    def test_get(self):
        r = requests.get('http://httpbin.testing-studio.com/get')
        print("json:" + r.text)
        print(r.json())
        print("request:" + str(r.request))
        print("cookies:" + str(r.cookies))
        print(r.headers)
        assert r.status_code == 200

    def test_html(self):
        html = """
        <html lang="en">
            <head>
                <meta charset="utf-8">
                 <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
                    <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
            </body>
        </html>"""
        header = {'Content-Type': 'application/html'}
        r = requests.post('http://httpbin.org/post', data=html, headers=header)
        pystache.render({
            "errcode": 0,
            "errmsg": "ok",
            "userid": "{{userid}}"
        })
        yaml.safe_load()
        yaml.load()
