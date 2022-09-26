import json
import pytest



class TestEnorll():

    def get_data(self):
        """
        ：读取json文件
        """
        data = []
        with open(self, 'r') as f:
            dict_data = json.load(f.read())
            for i in dict_data:
                data.append(tuple(i.values()))

    @pytest.mark.parametrize("name,email,pwd,pwd_",get_data(BASE_DIR + '\\data' + '\\enrolls.json'),
            ids=['注册成功', '密码不一致', '会员输入框为空', '重命名', '电子邮箱为空', '电子邮箱错误', '密码输入框为空']
    )
    def test_case(self, browser, name, email, pwd, pwd_, url=None):
        obj =Enorrllpage(browser)
        pass

