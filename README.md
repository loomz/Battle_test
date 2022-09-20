# Battle test手册
pip install pytest

pip install allure-pytest

# 生成html报告
pytest.main(['-s', 'test_test_wm.py', '--html=pytest3.html'])

# allure执行命令
pytest.main(['-sv',__file__,'--alluredir','./report','--clean-alluredir'])