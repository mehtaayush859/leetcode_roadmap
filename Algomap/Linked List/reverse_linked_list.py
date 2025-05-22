# 206. Reverse Linked List

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        prev = None
        curr = head
        
        # 1 -> 2 -> 3 -> None
        #  3 ->  2 -> 1 -> None

        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        return prev

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
input_list = [1,2,3,4,5]
linked_input = list_to_linked_list(input_list)

output_linked_list = res.reverseList(linked_input)
print(linked_list_to_list(output_linked_list))