import json
import pytest
from common_requests import CommonHttp
import os
from common_read_file import CommonReadFile

comm = CommonHttp('http://127.0.0.1:8088')


def setup():
    print('程序开始了')
    # 实例化自己的common


@pytest.mark.website
def test_index():
    # 建立uri_index的变量，存储战场的首页路由
    url_index = '/index'
    # 调用你自己在Common封装的get方法 ，返回结果存到了response_index中
    response_index = comm.get(url_index)
    print('Responseu首页地址内容：' + response_index.text)
    # 存储返回的response_index对象的text属性存储了访问主页的response信息，通过下面打印出来
    response_json = json.loads(response_index.text)
    assert response_json['code'] == 0


@pytest.mark.parametrize('username,password', CommonReadFile().get_data_csv('test_login.csv'))
def test_login(username, password):
    # 建立uri_login的变量，存储登录
    uri_login = '/login'
    # 拼凑body的参数
    payload = {'username': username, 'password': password}
    response_login =comm.post_json(uri_login, params=payload)
    print('Response_login登录内容：' + response_login.text)
    print('http状态码=%s, response.json=%s ' % (response_login.status_code, response_login.json()))
    response_json = json.loads(response_login.text)
    assert response_json['code'] == 0


@pytest.mark.parametrize('param_name', CommonReadFile().get_data_csv('test_selectEq.csv'))
def test_selectEq(param_name):
    url_selectEq = '/selectEq/%s' % param_name
    print('url_selectEq=%s' % url_selectEq)
    response = comm.get(url_selectEq)
    print('http状态码=%s, response.json=%s ' % (response.status_code, response.json()))
    assert response.status_code == 200 and response.json()['code'] == 0


@pytest.mark.parametrize('enemyId, equipmentId', CommonReadFile().get_data_csv('test_kill.csv'))
def test_kill(enemyId, equipmentId):
    url_kill = '/kill'
    payload = {"enemyid": enemyId, "equipmentid": equipmentId}
    response_kill = comm.post_json(url_kill, params=payload)
    print('Response内容：' + response_kill.text)
    # 通过返回值的code判断是否成功，0为成功，非0则抛出异常
    response_Json = json.loads(response_kill.text)
    assert response_Json['code'] == 0

def teardown():
    print('程序结束')


if __name__ == '__main__':
    # 生成html报告
    # pytest.main(['-s', 'test_test_wm.py', '--html=pytest3.html'])
    # pytest.main(['-s','pytest_test_wm.py','-v', '--html=pytest6.html'])

    # 测试当前文件中用例且生成报告./report,每次运行之前先清理报告所有的目录
    pytest.main(['-sv', __file__, '--alluredir', './allure-report', '--clean-alluredir'])
    # 查看执行，运行allure serve 报告所在目录
    # os.system('allure serve ./allure-report')