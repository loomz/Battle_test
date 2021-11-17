# Python代码中引入requests库，引入后才可以在你的代码中使用对应的类以及成员函数
from common import Common

# 建立uri_index的变量，存储战场的首页路由
uri_index = '/index'
# 实例化自己的Common
comm = Common('http://127.0.0.1:8087')
# 调用你自己在Common封装的get方法 ，返回结果存到了response_index中
response_index = comm.get(uri_index)
# 存储返回的response_index对象的text属性存储了访问主页的response信息，通过下面打印出来
print('Response内容：' + response_index.text)

# uri_login存储战场的登录
uri_login = '/login'
# username变量存储用户名参数
username = 'criss'
# password变量存储密码参数
password = 'criss'
# 拼凑body的参数
payload = 'username=' + username + '&password=' + password
response_login = comm.post(uri_login, params=payload)
print('Response内容：' + response_login.text)

# uri_selectEq存储战场的选择武器
uri_selectEq = '/selectEq/'
# 武器编号变量存储用户名参数
equipmentid = '10003'
# 拼凑body的参数
payload = 'equipmentid=' + equipmentid
response_selectEq = comm.post(uri_selectEq, params=payload)
print('Response内容：' + response_selectEq.text)

# uri_kill存储战场的选择武器
uri_kill = '/kill'
# 武器编号变量存储用户名参数
enemyid = '20001'
# 拼凑body的参数
payload = 'enemyid=' + enemyid + "&equipmentid=" + equipmentid
response_kill = comm.post(uri_kill, params=payload)
print('Response内容：' + response_kill.text)
