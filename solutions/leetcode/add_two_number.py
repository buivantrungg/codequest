from typing import Optional

from solutions.common.dto import ListNode, from_list, to_list

def add_two_number(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    head = None
    temp = head
    carry = 0
    while l1 or l2:
        sum = carry
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next
        carry = 0 if sum < 10 else 1
        new_node = ListNode(sum if sum < 10 else sum - 10)
        if temp:
            temp.next = new_node
            temp = temp.next
        else:
            head = temp = new_node
    if carry != 0:
        temp.next = ListNode(carry)
    return head

if __name__ == '__main__':
    list1 = from_list([2, 4, 3])
    list2 = from_list([5, 6, 4])
    print(to_list(add_two_number(list1, list2)))