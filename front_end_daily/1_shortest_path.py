"""
给出任意一个九宫格转换成一个横竖斜都相等的九宫格，得出最短路径
例如:

转化前
5 3 4
1 5 8
6 4 2

转化后
8 3 4
1 5 9
6 7 2

最短路径为
|5-8| + |8-9| + |4-7| = 7
"""
import copy
import math
import itertools

PATH = None


def get_shortest(lst, odd, even):
    """
    :param lst:
    :param odd:  奇数
    :param even: 偶数
    :return:
    """
    global PATH
    copy_lst = copy.deepcopy(lst)
    corner = [[0, 0], [0, 2], [2, 0], [2, 2]]
    border = [[0, 1], [1, 0], [1, 2], [2, 1]]
    # odd = [1, 3, 7, 9]
    # even = [2, 4, 6, 8]  #

    path = math.fabs(5 - lst[1][1])
    copy_lst[1][1] = 5

    for bd in border:
        temp = odd.pop()
        path += math.fabs(lst[bd[0]][bd[1]] - temp)
        copy_lst[bd[0]][bd[1]] = temp

    for cn in corner:
        temp = even.pop()
        path += math.fabs(lst[cn[0]][cn[1]] - temp)
        copy_lst[cn[0]][cn[1]] = temp

    if is_jiugongge(copy_lst):
        if PATH is None or PATH > path:
            PATH = path


def is_jiugongge(lst):
    for line in range(3):
        line_num = sum(lst[line])
        column_sum = lst[0][line] + lst[1][line] + lst[2][line]
        if line_num != 15 or column_sum != 15:
            return False

    top_left_2_bottom_right = lst[0][0] + lst[1][1] + lst[2][2]
    top_right_2_bottom_left = lst[0][2] + lst[1][1] + lst[2][0]

    if top_left_2_bottom_right != 15 or top_right_2_bottom_left != 15:
        return False

    return True


def get_out_of_order(odd, even):
    out_order_odd = itertools.permutations(odd)
    out_order_even = itertools.permutations(even)
    odd_list = []
    even_list = []
    for l in zip(out_order_odd, out_order_even):
        odd_list.append(list(l[0]))
        even_list.append(list(l[1]))

    return odd_list, even_list


if __name__ == '__main__':
    lst = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
    odd = [1, 3, 7, 9]
    even = [2, 4, 6, 8]
    odd_list, even_list = get_out_of_order(odd, even)
    for odd in odd_list:
        for even in even_list:
            get_shortest(list(lst), list(odd), list(even))

    print(PATH)
