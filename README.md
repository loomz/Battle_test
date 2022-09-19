# Battle test手册
pip install pytest

pip install allure-pytest

# allure执行命令

pytest.main(['-sv',__file__,'--alluredir','./report','--clean-alluredir'])