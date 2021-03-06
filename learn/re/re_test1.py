# coding:utf-8

import re

def had_number(data):
    result = re.findall('\d', data)
    if result:
        return True
    else:
        return False

def remove_number(data):
    result = re.findall('\D', data)
    print(result)
    return ''.join(result)

def start_with(sub, data):
    _sub = '\A%s' % sub
    result = re.findall(_sub, data)
    for i in result:
        return True
    return False

def end_with(sub, data):
    _sub = '%s\Z' % sub
    result = re.findall(_sub, data)
    if len(result) != 0:
        return True
    else:
        return False

def real_lenth(data):
    result = re.findall('\S', data)
    return len(result)

if __name__ == '__main__':
    data = 'adg d4g rgdf45   adsgf dafgr'
    result = had_number(data)
    print(result)
    result = remove_number(data)
    print(result)

    data = 'hello, i am 27 year\'s old'
    print(re.findall('\W', data))

    result = start_with('hll', data)
    print(result)

    result = end_with('olda', data)
    print(result)

    print(len(data))
    print(re.findall('.', data))
    print(real_lenth(data))
    print(re.findall('\S', data))
