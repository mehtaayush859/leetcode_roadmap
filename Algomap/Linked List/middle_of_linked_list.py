# 876. Middle of the Linked List

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.


# Example 2:
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

#Note: So, as we check for cycle using two pointer,  we do same for this problem. if fast.next.next -> then slow would be its half. Foe ex: fast = 2, then slow = 1, it half which is middle, we return slow.

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
        
        

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

output_linked_list = res.middleNode(linked_input)
print(linked_list_to_list(output_linked_list))