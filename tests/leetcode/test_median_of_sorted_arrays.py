from solutions.leetcode.median_of_sorted_arrays import find_median_sorted_arrays

def test_find_median_sorted_arrays_example1():
    nums1 = [1, 3]
    nums2 = [2]
    assert find_median_sorted_arrays(nums1, nums2) == 2.00000

def test_find_median_sorted_arrays_example2():
    nums1 = [1,2]
    nums2 = [3,4]
    assert find_median_sorted_arrays(nums1, nums2) == 2.50000
