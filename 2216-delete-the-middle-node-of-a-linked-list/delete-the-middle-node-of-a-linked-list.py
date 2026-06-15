# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counting = head
        length = 0
        while counting:
            length += 1
            counting = counting.next
        middle = length // 2  
            
        idx = 0
        prev = head
        while prev:
            idx += 1
            if idx == middle:
                prev.next = prev.next.next
                return head
            prev = prev.next


        
            

       