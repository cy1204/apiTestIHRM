import app, json, pymysql


def assert_common(self, response, http_code, success, code, message):
    """
    断言方法（函数）
    :param self:
    :param response:
    :param http_code:http响应状态码
    :param success:是否成功
    :param code:
    :param message:
    :return:无
    """
    self.assertEqual(http_code, response.status_code)  # 断言响应状态码
    self.assertEqual(success, response.json().get("success"))  # 断言success
    self.assertEqual(code, response.json().get("code"))  # 断言code
    self.assertIn(message, response.json().get("message"))  # 断言message


def read_login_data():
    """读取登录数据方法（函数）"""
    data_path = app.BASE_DIR + "/data/login_data.json"
    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        data_list = list()
        for i in data:
            data_list.append((i.get("mobile"),
                              i.get("password"),
                              i.get("http_code"),
                              i.get("success"),
                              i.get("code"),
                              i.get("message")))
    return data_list


def read_add_emp_data():
    """读取添加员工数据方法（函数）"""
    data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        data_list = list()
        data_list.append((data.get("add_emp").get("username"),
                          data.get("add_emp").get("mobile"),
                          data.get("add_emp").get("success"),
                          data.get("add_emp").get("code"),
                          data.get("add_emp").get("message"),
                          data.get("add_emp").get("http_code")))
    return data_list


def read_query_emp_data():
    """读取查询员工数据方法（函数）"""
    data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        data_list = list()
        data_list.append((data.get("query_emp").get("success"),
                          data.get("query_emp").get("code"),
                          data.get("query_emp").get("message"),
                          data.get("query_emp").get("http_code")))
    return data_list


def read_modify_emp_data():
    """读取修改员工数据方法（函数）"""
    data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        data_list = list()
        data_list.append((data.get("modify_emp").get("username"),
                          data.get("modify_emp").get("success"),
                          data.get("modify_emp").get("code"),
                          data.get("modify_emp").get("message"),
                          data.get("modify_emp").get("http_code")))
    return data_list


def read_delete_emp_data():
    """读取删除员工数据方法（函数）"""
    data_path = app.BASE_DIR + "/data/emp_data.json"
    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        data_list = list()
        data_list.append((data.get("delete_emp").get("success"),
                          data.get("delete_emp").get("code"),
                          data.get("delete_emp").get("message"),
                          data.get("delete_emp").get("http_code")))
    return data_list


class DBUtils():
    def __init__(self, host="182.92.81.159", user="readuser", password="iHRM_user_2019", database="ihrm"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    # __enter__ 和 __exit__ 是一对魔法方法，主要和with结合使用
    # 如：with DBUtils as db
    def __enter__(self):
        self.conn = pymysql.connect(self.host, self.user, self.password, self.database)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()


if __name__ == '__main__':
    print(read_add_emp_data())
