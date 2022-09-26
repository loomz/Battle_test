import  pytest
 class TestEnorll():
 2
 3     def get_data(self):
 4         """
 5         读取json文件
 6         :return:
 7         """
 8         data = []
 9         with open(self, 'r') as f:
10             dict_data = json.loads(f.read())
11             for i in dict_data:
12                 data.append(tuple(i.values()))
13         return data
14
15     @pytest.mark.parametrize(
16         "name, email, pwd, pwd_",
17         get_data(BASE_DIR + '\\data' + '\\enorlluser.json'),
18         ids=['注册成功', '密码不一致', '会员输入框为空', '重名注册', '电子邮箱为空', '电子邮箱错误', '密码输入框为空']
19     )
20     def test_case(self, browser, name, email, pwd, pwd_, url=None):
           obj = Enorllpage(browser)
           pass