
def max_list_iter(int_list):
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError
    if len(int_list) is 0:
        return None
    idx = 0
    for i in range(len(int_list)):
        if int_list[i] > int_list[idx]:
            idx = i
    return int_list[idx]


def reverse_rec(int_list):
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError
    if len(int_list) is 0:
        return []
    return reverse_rec(int_list[1:]) + [int_list[0]]


def bin_search(target, low, high, int_list):
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    if low > high:
        return None
    if len(int_list) is 0:
        return None
    mid = (low + high) // 2
    if int_list[mid] == target:
        return mid
    if target > int_list[mid]:
        return bin_search(target, mid + 1, high, int_list)
    else:
        return bin_search(target, low, mid - 1, int_list)
