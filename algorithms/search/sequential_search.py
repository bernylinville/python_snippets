# coding:utf-8

def sequential_search(list, item):
    '''顺序查找，输入的列表是无序的'''
    pops = 0
    found = False

    while pops < len(list) and not found:
        if list[pops] == item:
            found = True
        else:
            pops += 1

    return found

if __name__ == '__main__':
    list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    item = 31
    # item = 100  # 测试
    print('{} 是否在列表中: {}'.format(item, sequential_search(list, item)))
