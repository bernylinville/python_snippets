# coding:utf-8

import re


def check_url(url):
    re_g = re.compile('[a-zA-Z]://\w*\.*\w+\.\w+')
    print(re_g)
    result = re_g.findall(url)
    if result:
        return True
    else:
        return False


def get_url(url):
    re_g = re.compile('[http://|https://](\w*\.*\w+\.\w+)')
    result = re_g.findall(url)
    if result:
        return result[0]
    else:
        return ''


def get_email(email):
    re_g = re.compile('.+@.+\.[a-zA-Z]+')
    result = re_g.findall(email)
    return result


def get_html(html):
    re_g = re.compile('style="(.*?)"')
    result = re_g.findall(html)
    return result


def get_all_html(html):
    re_g = re.compile('style="(.+?)"')
    result = re_g.findall(html)
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

    re_g = re.compile(
        '<div class="(.+?)" style="(.+?)">''</div><div class="(.+?)"></div>')
    result = re_g.search(html)
    print(result.groups())
    print(result.group(1))
    print(result.group(2))
    print(result.group(3))

    re_g = re.compile('\s')
    result = re_g.split(html)
    print(result)

    re_g = re.compile('<div class="(.+?)"')
    result = re_g.match(html)
    print(result.group())
    print(result.span())
    print(html[:22])
