"""

"""
import app, requests


class EmpApi():
    def __init__(self):
        self.emp_url = app.HOST + "/api/sys/user"
        self.headers = app.HEADERS

    def add_emp(self, username, password):
        """
        添加员工方法
        :param username: 用户名
        :param password: 手机号码
        :return: 响应数据
        """
        data = {
            "username": username,
            "mobile": password,
            "timeOfEntry": "2019-12-02",
            "formOfEmployment": 1,
            "workNumber": "1234",
            "departmentName": "测试",
            "departmentId": "1210411411066695680",
            "correctionTime": "2019-12-15T16:00:00.000Z"
        }
        # 发送添加员工请求，返回响应数据
        response = requests.post(self.emp_url, json=data, headers=self.headers)
        return response

    def query_emp(self):
        """查询员工方法"""
        url = self.emp_url + "/" + app.EMP_ID
        # self.headers是{"Content-Type":"application/json","Authorization":"Brarer xxxx-xxxx-xxxx"}
        response = requests.get(url, headers=self.headers)
        return response

    def modify_emp(self, username):
        """修改员工方法"""
        url = self.emp_url + "/" + app.EMP_ID
        # 从外部接收要修改的username，拼接成json数据
        data = {"username": username}
        response = requests.put(url, json=data, headers=self.headers)
        return response

    def delete_emp(self):
        """删除员工方法"""
        url = self.emp_url + "/" + app.EMP_ID
        response = requests.delete(url, headers=self.headers)
        return response
