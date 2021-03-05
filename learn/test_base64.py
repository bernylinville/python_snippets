# coding:utf-8

import base64

replace_one = '%'
replace_two = '$'

def test_encode(data):
    if isinstance(data, str):
        data = data.encode('utf-8')
    elif isinstance(data, bytes):
        pass
    else:
        raise TypeError('data need bytes or str')

    _data = base64.encodebytes(data).decode('utf-8')
    _data = _data.replace('a', replace_one).replace('8',replace_two)
    return _data


def test_decode(data):
    if not isinstance(data, bytes):
        raise TypeError('data need bytes')

    replace_one_b = replace_one.encode('utf-8')
    replace_two_b = replace_two.encode('utf-8')

    data = data.replace(replace_one_b, b'a').replace(replace_two_b, b'8')

    return base64.decodebytes(data).decode('utf-8')

if __name__ == '__main__':
    # result = test_encode(1)
    result = test_encode('hello')
    print(result)
    new_result = test_decode(result.encode('utf-8'))
    print(new_result)
