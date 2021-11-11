import unittest
from common import Common

class TestBattle(unittest.TestCase) :
    # 定义 comm
    comm = None

    def setUp(self) -> None:
        print('setUp')
        # 实例化自己的Common
        comm = Common('http://127.0.0.1:8088')
        self.comm = comm;

    def test_index(self) :
        # 建立uri_index的变量，存储战场的首页路由
        uri_index = '/index'

        # 调用你自己在Common封装的get方法 ，返回结果存到了response_index中
        response_index = self.comm.get(uri_index)
        # 存储返回的response_index对象的text属性存储了访问主页的response信息，通过下面打印出来
        print('Response内容：' + response_index.text)

    def test_login(self) :
        # uri_login存储战场的登录
        uri_login = '/login'
        # username变量存储用户名参数
        username = 'criss'
        # password变量存储密码参数
        password = 'criss'
        # 拼凑body的参数
        payload = 'username=' + username + '&password=' + password
        response_login = self.comm.post_json(uri_login, params=payload)
        print('Response内容：' + response_login.text)

    def test_selectEq(self) :
        # uri_selectEq存储战场的选择武器
        uri_selectEq = '/selectEq'
        # 武器编号变量存储用户名参数
        equipmentid = '10003'
        # 拼凑body的参数
        payload = 'equipmentid=' + equipmentid
        response_selectEq = self.comm.get(uri_selectEq, params=payload)
        print('Response内容：' + response_selectEq.text)

    def test_kill(self) :
        # uri_kill存储战场的选择武器
        uri_kill = '/kill'
        # 武器编号变量存储用户名参数
        enemyid = '20001'
        equipmentid = '10003'
        # 拼凑body的参数
        payload = 'enemyid=' + enemyid + "&equipmentid=" + equipmentid
        response_kill = self.comm.post(uri_kill, params=payload)
        print('Response内容：' + response_kill.text)


    def tearDown(self) -> None:
        print('tearDown')
        comm = None;