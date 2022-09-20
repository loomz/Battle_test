import json
import pytest
from common import Common
import os


class TestPytest:
    comm = None

    def setup(self):
        print('程序开始了')
        # 实例化自己的common
        comm = Common('http://127.0.0.1:8088')
        self.comm = comm

    @pytest.mark.website
    def test_index(self):
        # 建立uri_index的变量，存储战场的首页路由
        url_index = '/index'
        # 调用你自己在Common封装的get方法 ，返回结果存到了response_index中
        response_index = self.comm.get(url_index)
        print('Responseu首页地址内容：' + response_index.text)
        # 存储返回的response_index对象的text属性存储了访问主页的response信息，通过下面打印出来
        response_json = json.loads(response_index.text)
        assert response_json['code'] == 0

    def test_login(self):
        # 建立uri_login的变量，存储登录
        uri_login = '/login'
        # 拼凑body的参数
        payload = {'username': 'criss', 'password': 'criss'}
        response_login = self.comm.post_json(uri_login, params=payload)
        print('Response_login内容：' + response_login.text)
        response_json = json.loads(response_login.text)
        assert response_json['code'] == 0

    def test_seletceq(self):
        # uri_selectEq存储战场的选择武器
        url_selectEq = '/selectEq/%s'
        # 武器编号变量存储用户名参数
        equipmentid = '10003'
        url_selectEq = url_selectEq % equipmentid
        response_seleteq = self.comm.get(url_selectEq)
        print('response_seleteq请选择武器:' + response_seleteq.text)
        response_json = json.loads(response_seleteq.text)
        assert response_json['code'] == 0

    def test_kill(self):
        url_kill = '/kill'
        payload = {"enemyid": "20001", "equipmentid": "10003"}
        response_kill = self.comm.post_json(url_kill, params=payload)
        print('Response内容：' + response_kill.text)

        # 通过返回值的code判断是否成功，0为成功，非0则抛出异常
        response_Json = json.loads(response_kill.text);
        assert response_Json['code'] == 0;

if __name__ == '__main__':
    # 生成html报告
    # pytest.main(['-s', 'test_test_wm.py', '--html=pytest3.html'])
    # pytest.main(['-s','pytest_test_wm.py','-v', '--html=pytest6.html'])

    # 测试当前文件中用例且生成报告./report,每次运行之前先清理报告所有的目录
    pytest.main(['-sv', __file__, '--alluredir', './report', '--clean-alluredir'])
    # 查看执行，运行allure serve 报告所在目录
    os.system('allure serve ./report')