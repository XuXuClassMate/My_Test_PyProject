from test_API.src.Base import Base


class wuwork_api(Base):
    def add_member(self, userid: str, name: str, mobile: str, department: list, **kwargs):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?"
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        data.update(kwargs)
        return self.send("post", url, json=data)

    def get_member(self, userid: str):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}"
        return self.send("get", url)

    def update_muber(self, userid: str, newname: str, **kwargs):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?"
        update_data = {
            "userid": f"{userid}",
            "name": newname, }
        update_data.update(kwargs)
        return self.send("post", url, json=update_data)

    def delete_muber(self, userid: str):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}"
        return self.send("get", url)
