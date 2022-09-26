import pytest

from common_read_file import CommonReadFile


@pytest.mark.parametrize('name, age, gender', [['tina', '36', '女'], ['wangmin', '35', '女']])
def test01(name, age, gender):
    print("name=%s, age=%s, gender=%s" % (name, age, gender))


@pytest.mark.parametrize('name, age, gender, birth', CommonReadFile().get_data_csv('test.csv'))
def test_02(name, age, gender, birth):
    print("name=%s, age=%s, gender=%s, birth=%s" % (name, age, gender, birth))


@pytest.mark.parametrize('name,age,gender', CommonReadFile().get_data_json_arr('test_json_array.json'))
def test_03(name, age, gender):
    print("name=%s, age=%s, gender=%s" % (name, age, gender))


if __name__ == '__main__':
    pytest.main(['-sv', 'pytest_csv.py'])
