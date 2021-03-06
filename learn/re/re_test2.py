# coding:utf-8

import re


def check_url(url):
    result = re.findall('[a-zA-Z]://\w*\.*\w+\.\w+', url)
    if result:
        return True
    else:
        return False


def get_url(url):
    result = re.findall('https://(\w*\.*\w+\.\w+)', url)
    if result:
        return result[0]
    else:
        return ''


def get_email(email):
    result = re.findall('[0-9a-zA-Z_]+@[0-9a-zA-Z]+\.[a-zA-Z]+', email)
    return result


if __name__ == "__main__":
    # url = 'https://blog.devopsthink.org/'
    # url = 'https://github.com'
    url = 'https://www.github.com'
    # url = 'http://bl5og.devop-st2hink.or2g/'
    result = check_url(url)
    print(result)

    result = get_url(url)
    print(result)

    email = 'bernylinville@devopsthink.org'
    result = get_email(email)
    print(result)
