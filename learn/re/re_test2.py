# coding:utf-8

import re


def check_url(url):
    result = re.findall('[a-zA-Z]://\w*\.*\w+\.\w+', url)
    if result:
        return True
    else:
        return False


def get_url(url):
    result = re.findall('[http://|https://](\w*\.*\w+\.\w+)', url)
    if result:
        return result[0]
    else:
        return ''


def get_email(email):
    result = re.findall('.+@.+\.[a-zA-Z]+', email)
    return result


def get_html(html):
    result = re.findall('style="(.*?)"', html)
    return result


def get_all_html(html):
    result = re.findall('="(.+?)"', html)
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

    html = '<div class="s-top-nav" style="display:none;">''</div><div class="s-center-box"></div>'
    result = get_all_html(html)
    print(result)
