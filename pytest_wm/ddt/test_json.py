import  pytest
import json


def get_data():
    with open('test.json') as f:
        lit = []
        data = json.load(f)
        #extend 追加
        lit.extend(data['key'])
        lit.extend(data['key1'])
        return  lit
        #print(data)
@pytest.mark.parametrize('name',get_data())
def test01(name):
    print(name)




if __name__ == '__main__':
   # print(get_data())
    pytest.main(['-sv','test_json.py'])