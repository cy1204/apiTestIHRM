import unittest, time, app
from script.login import TestLoginSuccess
from script.test_emp import TestEmp
from tools.HTMLTestRunnerCN import HTMLTestReportCN

# 初始化测试套件
suite = unittest.TestSuite()

# 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestLoginSuccess))
suite.addTest(unittest.makeSuite(TestEmp))

# 使用TestRunner执行测试套件
report_path = app.BASE_DIR + "/report/ihrm{}.html".format(time.strftime("%Y%m%d_%H%M%S"))
with open(report_path, "wb") as f:
    # 初始化HTMLTestReport
    runner = HTMLTestReportCN(f, verbosity=2, title="IHRM人力资源接口")

    # 运行测试套件
    runner.run(suite)
