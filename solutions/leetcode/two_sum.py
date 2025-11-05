from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    visited = {}
    for index, num in enumerate(nums) :
        expected = target - num
        if expected not in visited:
            visited[num] = index
        else:
            return [visited[expected], index]
    raise ValueError("nums must contain exactly one pair - which sum up to target")



if __name__ == "__main__":  # pragma: no cover - convenience sanity check
    nums=[2, 7, 11, 15]
    target=9
    print(two_sum(nums, target))
