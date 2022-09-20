import  pytest
import csv

def get_data():
    #with opn 打开某文件 定义别名 f
    with open('test.cvs') as f:
        #读取里面值
        lst =csv.reader(f)
        my_data = []
        for row in lst:
             my_data.extend(row)
        return my_data

@pytest.mark.parametrize('name',get_data())
def test01(name):
    print(name)

if __name__ == '__main__':
    #print(get_data())
    pytest.main(['-s','-v', 'pytest_cvs.py'])