"""

"""
import unittest, logging, app
from api.emp_api import EmpApi
from utils import assert_common, read_add_emp_data, read_query_emp_data, \
    read_modify_emp_data, read_delete_emp_data, DBUtils
from parameterized import parameterized


class TestEmp(unittest.TestCase):
    """员工管理测试类"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.emp_api = EmpApi()  # 初始化员工管理类

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @parameterized.expand(read_add_emp_data())
    def test01_add_emp(self, username, mobile, success, code, message, http_code):
        """添加员工测试方法"""
        response = self.emp_api.add_emp(username, mobile)
        json_data = response.json()
        logging.info("添加员工接口返回的数据为：{}".format(json_data))

        # 断言
        assert_common(self, response, http_code, success, code, message)

        # 获取员工ID保存在全局变量
        app.EMP_ID = json_data.get("data").get("id")

    @parameterized.expand(read_query_emp_data())
    def test02_query_emp(self, success, code, message, http_code):
        """查询员工测试方法"""
        response = self.emp_api.query_emp()
        json_data = response.json()
        logging.info("查询员工接口返回的数据为：{}".format(json_data))

        # 断言
        assert_common(self, response, http_code, success, code, message)

    @parameterized.expand(read_modify_emp_data())
    def test03_modify_emp(self, username, success, code, message, http_code):
        """修改员工测试方法"""
        response = self.emp_api.modify_emp(username)
        json_data = response.json()
        logging.info("修改员工接口返回的数据为：{}".format(json_data))
        with DBUtils() as db_utils:
            # 执行查询语句，查询修改之后的username
            sql = "select username from bs_user where id={}".format(app.EMP_ID)
            db_utils.execute(sql)
            # 获取执行结果
            result = db_utils.fetchone()[0]
            logging.info("从数据库中查询出的员工的用户名是：{}".format(result))

        # 断言
        assert_common(self, response, http_code, success, code, message)

    @parameterized.expand(read_delete_emp_data())
    def test04_delete_emp(self, success, code, message, http_code):
        """删除员工测试方法"""
        response = self.emp_api.delete_emp()
        json_data = response.json()
        logging.info("删除员工接口返回的数据为：{}".format(json_data))

        # 断言
        assert_common(self, response, http_code, success, code, message)
