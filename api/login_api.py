"""

"""
import app, requests


class LoginApi():
    def __init__(self):
        self.login_url = app.HOST + "/api/sys/login"
        self.headers = app.HEADERS

    def login(self, mobile, password):
        """
        登录方法
        :param mobile: 手机号码
        :param password:密码
        :return:响应数据
        """
        data = {"mobile": mobile, "password": password}
        response = requests.post(self.login_url, json=data, headers=self.headers)
        return response
