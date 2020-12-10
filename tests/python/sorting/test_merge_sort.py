from python.sorting.merge_sort import merge_sort


def test_merge_sort():
    arr = [6, 5, 3, 1, 8, 7, 2, 4]
    merge_sort(arr)
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8]
