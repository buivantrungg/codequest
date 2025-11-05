from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    middle = (len(nums1) + len(nums2)) / 2
    count = 0
    nums1_step = 0
    nums2_step = 0
    res = 0
    while count <= middle:
        if nums1_step >= len(nums1):
            temp = nums2[nums2_step]
            nums2_step += 1
        elif nums2_step >= len(nums2):
            temp = nums1[nums1_step]
            nums1_step += 1
        elif nums1[nums1_step] <= nums2[nums2_step]:
            temp = nums1[nums1_step]
            nums1_step += 1
        else:
            temp = nums2[nums2_step]
            nums2_step += 1
        if count == middle - 1:
            res += temp
        elif count == middle - 0.5:
            return temp
        elif count == middle:
            return (res + temp) / 2
        count += 1
    return 0


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    print(find_median_sorted_arrays(nums1, nums2))