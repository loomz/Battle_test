import MySQLdb
import pytest

conn = MySQLdb.connect(
    usr='root',
    passwd='root',
    host='192.168.3.189',
    port=3354,
    db='testing_db'
)


def get_data():
    query_sql = 'select id,usrname,pwd from user_btl'
    lst = []
    try:
        # 获取游标
        cursor = conn.cursor()
        # 通过游标执行SQL语
        cursor.execute(query_sql)
        # 获取所有数据
        r = cursor.fetchall()
        for x in r:
            # x[0]第一列，X[1]第二列，X[2]第三列
            u = (x[0], x[1], x[2])
            lst.append(u)
        return lst
    finally:
        cursor.close()  # 关闭游标
        conn.close()  # 关闭数据库


@pytest.mark.parametrize('id,name,pwd', get_data())
def test1(id, name, pwd):
    print(id, name, pwd)


if __name__ == '__main__':
    pytest.main(['-sv'])
