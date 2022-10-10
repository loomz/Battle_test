import pytest
import os

if __name__ == '__main__':
    # 生成html报告
    # pytest.main(['-s', 'test_test_wm.py', '--html=pytest3.html'])
    # pytest.main(['-s','pytest_test_wm.py','-v', '--html=pytest6.html'])

    # 测试当前文件中用例且生成报告./report,每次运行之前先清理报告所有的目录bbbvssssssssss
    pytest.main(['-sv', 'pytest_test_wm.py', __file__, '--alluredir', './allure-report', '--clean-alluredir'])
    # 查看执行，运行allure serve 报告所在目录
    # os.system('allure serve ./allure-report')