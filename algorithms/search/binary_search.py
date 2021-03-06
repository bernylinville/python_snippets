# coding:utf-8

def binary_search(list, item):
    '''非递归实现二分查找，输入的列表必须是有序的（比如，从小到大排列）'''
    start = 0
    end = len(list) - 1
    found = False

    while start <= end and not found:
        mid = (start + end) // 2
        print('start = {}, end = {}, mid = {}'.format(start, end, mid))  # 测试

        if list[mid] == item:
            found = True
        else:
            if item < list[mid]:
                end = mid - 1
            else:
                start = mid + 1

    return found


if __name__ == '__main__':
    list = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    item = 31
    # item = 32  # 测试
    print('{} 是否在列表中: {}'.format(item, binary_search(list, item)))
