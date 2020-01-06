"""

"""
import unittest, logging
from api.login_api import LoginApi
from utils import assert_common, read_login_data
from parameterized import parameterized


class TestLogin(unittest.TestCase):
    """登录测试类"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()  # 初始化登录类

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @parameterized.expand(read_login_data())
    def test_login(self, mobile, password, http_code, success, code, message):
        """登录测试方法"""
        response = self.login_api.login(mobile, password)
        json_data = response.json()  # 接收返回的json数据
        logging.info("登录接口返回的数据为：{}".format(json_data))  # 输出日志，只能用{}占位符

        # 断言
        # self.assertEqual(200, response.status_code)  # 断言响应状态码
        # self.assertEqual(True, json_data.get("success"))  # 断言success
        # self.assertEqual(10000, json_data.get("code"))  # 断言code
        # self.assertIn("操作成功", json_data.get("message"))  # 断言message

        assert_common(self, response, http_code, success, code, message)
