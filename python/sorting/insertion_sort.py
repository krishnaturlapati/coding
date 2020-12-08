"""

pseudo code

for j = 2 in A.length
    key = A[j]
    i = j-1
    while i>0 and A[i] > key
        A[i+1] = A[i]
        i = i-1
    end do
    A[i+1] = key
end for
"""
from typing import List


def insertion_sort(a:List) -> List:
    """
    A unsorted array
    :param a:
    :return: sorted list
    """
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i -= 1
        a[i+1] = key
    return a
