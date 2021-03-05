# coding:utf-8

import hashlib
import time

base_sign = 'mooc'

def test_hashlib():
    a_timestamp = int(time.time())
    _token = '%s%s' % (base_sign, a_timestamp)
    hashobj = hashlib.sha1(_token.encode('utf-8'))
    a_token = hashobj.hexdigest()
    return a_token, a_timestamp

def b_service_check(token, timestamp):
    _token = _token = '%s%s' % (base_sign, timestamp)
    b_token = hashlib.sha1(_token.encode('utf-8')).hexdigest()
    if token == b_token:
        return True
    else:
        return False

if __name__ == '__main__':
    need_help_token, timestamp = test_hashlib()
    time.sleep(1)
    # result = b_service_check(need_help_token, timestamp)
    result = b_service_check(need_help_token, time.time())
    if result:
        print('a合法')
    else:
        print('a不合法')
