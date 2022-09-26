import  pytest
from common_read_file import CommonReadFile


@pytest.mark.parametrize("name, passwd, gender, birth", CommonReadFile().get_data_excel('data.xlsx', sheet=0))
def test01(name, passwd, gender, birth):
    print("name=%s, passwd=%s, gender=%s, birth=%s" % (name, passwd, gender, birth))


if __name__ == '__main__':
    pytest.main(['-sv', 'test_execl_01.py'])