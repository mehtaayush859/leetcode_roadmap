# 21. Merge Two Sorted Lists


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy= ListNode(-1)
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        
        if list2:
            curr.next = list2

        return dummy.next


def list_to_linked_list(lst: List[int]) -> Optional[ListNode]:
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

res = Solution()
input_list = [1,2,4]
second_list = [1,3,4]
linked_input = list_to_linked_list(input_list)
linked_input1 = list_to_linked_list(second_list)

output_linked_list = res.mergeTwoLists(linked_input, linked_input1)
print(linked_list_to_list(output_linked_list))