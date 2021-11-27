import json
import unittest
from common import Common
import HTMLTestRunner


class TestBattle(unittest.TestCase):
    #定义comm
    comm = None

    def setUp(self) -> None:
        # 实例化自己的Common
        comm = Common('http://127.0.0.1:8088')
        self.comm = comm

    def test_index(self):
        # 建立uri_index的变量，存储战场的首页路由
        url_index = '/index'
        # 调用你自己在Common封装的get方法 ，返回结果存到了response_index中
        response_index = self.comm.get(url_index)
        print('response_index请求内容：' + response_index.text)
        # 通过返回值的code判断是否成功，0为成功，非0则抛出异常
        responsejson = json.loads(response_index.text)
        assert responsejson['code'] == 0

    def test_login(self):
        # url_login的变量，存储战场登录
        url_login = '/login'
        # 拼凑body的参数
        payload = {'username': 'criss', 'password': 'criss'}
        # 调用你自己在Common封装的get方法 ，返回结果存到了response_login中
        response_login = self.comm.post_json(url_login, params=payload)
        print('response_login内容：' + response_login.text)
        responseJson = json.loads(response_login.text)
        assert responseJson['code'] == 0

    def test_selectEq(self):
        # url_selecteq的变量，存储选择武器
        url_selecteq = '/selectEq/%s'
        equipmentid = '10003'
        # 拼凑body的参数
        url_selecteq = url_selecteq % equipmentid
        respone_eq = self.comm.get(url_selecteq)
        print('respone_eq内容:' + respone_eq.text)
        # 通过返回值的code判断是否成功，0为成功，非0则抛出异常
        responseJson = json.loads(respone_eq.text)
        assert responseJson['code'] == 0
        
    def test_kill(self):
        # uri_kill存储战场的选择武器
        uri_kill = '/kill'
        # enemyid = '20002'
        # equipmentid = '10002'
        # payload = 'enemyid=' + enemyid + "&equipmentid=" + equipmentid
        # respone_kill = self.comm.post(uri_kill,params= payload )
        payload = {'enemyid': '20002', 'equipmentid': '10002'}
        respone_kill = self.comm.post_json(uri_kill,params=payload)
        print('respone_kill内容：' + respone_kill.text)

        # 通过返回值的code判断是否成功，0为成功，非0则抛出异常
        responejson = json.loads(respone_kill.text)
        assert  responejson['code'] == 0

    def tearDown(self) -> None:
        print('tearDown')
        comm = None;

if __name__ == '__main__':
    # 测试用例目录
    case_dirs = r"D:\Pychram_Wordspace\battle_test_git\Battle_test"
    # 加载测试用例
    discover = unittest.defaultTestLoader.discover(case_dirs, "unittestTest_wm.py")
    # 运行测试用例同时保存测试报告
    test_report_path = r"D:\Pychram_Wordspace\battle_test_git\Battle_test\report_wm01.html"
    with open(test_report_path, "wb") as report_file:
        runner = HTMLTestRunner.HTMLTestRunner(stream=report_file, title="自动化测试报告", description="XX应用功能测试")
        runner.run(discover)


# if __name__ == "__main__":
#     # 测试用例保存的目录
#     case_dirs = r"D:\Pychram_Wordspace\battle_test_git\Battle_test"
#     # 加载测试用例
#     discover = unittest.defaultTestLoader.discover(case_dirs, "unittestTest_wm.py")
#     # 运行测试用例同时保存测试报告
#     test_report_path = r"D:\Pychram_Wordspace\battle_test_git\Battle_test\report.txt"
#     with open(test_report_path, "a") as report_file:
#         runner = unittest.TextTestRunner(stream=report_file, verbosity=2)
#         runner.run(discover)

