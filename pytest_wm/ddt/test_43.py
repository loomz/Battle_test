import  pytest

# 列表
data = ['tina','124']
@pytest.mark.parametrize('pwd',data)
def test01(pwd):
    print(pwd)


# 元组
data2 = [(1,2,3),
         (4,5,6),
         (7,8,9)]
@pytest.mark.parametrize('a,b,c',data2)
def test02(a,b,c):
    print(a,b,c)
# 字典
data3 = (
    {
        "user": 1,
        "pwd": 123456
    },
    {
        "age": 19,
        "email":'lzzoz@126.com'
    }
)

@pytest.mark.parametrize('dick',data3)
def test03(dick):
    print(dick)

data_1 = [
    pytest.param(1,2,3, id=("(a+b):pass")),
    pytest.param(4,5,10, id=("(a+b):fail"))
]
def add (a,b):
    return  a + b
class parametrize(object):
    @pytest.mark.parametrize('a,b,expect',data_1)
    def test_parametrize(self,a,b,expect):
        assert  add(a,b) == expect


if __name__ == '__main__':
    pytest.main(['-sv','test_43.py'])
