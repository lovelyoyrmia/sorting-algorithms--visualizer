from draw import draw_list


def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_list(
                    draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True)
                yield True

    return lst


def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(1, len(lst)):
        current = lst[i]

        while True:
            ascending_sort = i > 0 and lst[i - 1] > current and ascending
            descending_sort = i > 0 and lst[i - 1] < current and not ascending

            if not ascending_sort and not descending_sort:
                break

            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] = current
            draw_list(draw_info, {i - 1: draw_info.GREEN,
                      i: draw_info.RED}, True)
            yield True

    return lst


def merge_sort(draw_info, ascending=True):
    lst = draw_info.lst

    if len(lst) > 1:
        left_lst = lst[:len(lst)//2]
        right_lst = lst[len(lst)//2:]

        # Recursion
        merge_sort(left_lst)
        merge_sort(right_lst)

        # Merge
        i = 0
        j = 0
        k = 0
        while i < len(left_lst) and j < len(right_lst):
            if left_lst[i] < right_lst[i]:
                lst[k] = left_lst[i]
                i += 1
            else:
                lst[k] = right_lst[j]
                j += 1
            k += 1

        while i < len(left_lst):
            lst[k] = left_lst[i]
            i += 1
            k += 1

        while j < len(right_lst) - 1:
            lst[k] = right_lst[j]
            j += 1
            k += 1

        draw_list(draw_info, {}, True)
