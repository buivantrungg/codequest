from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def from_list(vals: List[int]):
    tail = None
    for val in reversed(vals):
        tail = ListNode(val, tail)
    return tail

def to_list(node: ListNode) -> List[int]:
    travel = node
    temp = []
    while travel:
        temp.append(travel.val)
        travel = travel.next
    return temp


if __name__ == '__main__':
    head = from_list([1,2,3])
    print(to_list(head))


