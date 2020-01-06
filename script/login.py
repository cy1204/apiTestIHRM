"""
登录成功
"""
import unittest, logging, app
from api.login_api import LoginApi
from utils import assert_common


class TestLoginSuccess(unittest.TestCase):
    """登录成功测试类"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_login_success(self):
        """登录成功测试方法"""
        response = self.login_api.login("13800000002", "123456")
        json_data = response.json()  # 接收返回的json数据
        logging.info("登录接口返回的数据为：{}".format(json_data))  # 输出日志，只能用{}占位符

        # 断言
        # self.assertEqual(200, response.status_code)  # 断言响应状态码
        # self.assertEqual(True, json_data.get("success"))  # 断言success
        # self.assertEqual(10000, json_data.get("code"))  # 断言code
        # self.assertIn("操作成功", json_data.get("message"))  # 断言message

        assert_common(self, response, 200, True, 10000, "操作成功")

        # 获取令牌，并拼接成以[Bearer ]开头的令牌字符串
        token = json_data.get("data")
        print("token为：", token)
        # 保存令牌到全局变量
        app.HEADERS["Authorization"] = "Bearer " + token
        logging.info("保存的令牌是：{}".format(app.HEADERS))
