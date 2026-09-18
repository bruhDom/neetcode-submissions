# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        

        p1 = head
        p2 = head

        while p1 is not None and p2 is not None:

            if p1.next is not None:
                p1 = p1.next
            else:
                break
           
            if p2.next is not None and p2.next.next is not None:
                p2 = p2.next.next
            else:
                break

            if p1 is p2:
                return True


        return False
