from python.sorting.insertion_sort import insertion_sort


def test_insertion_sort():
    assert insertion_sort([4, 2, 1]) == [1, 2, 4]
    assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert insertion_sort([6, 5, 4, 2, 1]) == [1, 2, 4, 5, 6]
    assert insertion_sort([4, 0, -1]) == [-1, 0, 4]
    assert insertion_sort([0, 0, 0]) == [0, 0, 0]

