# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Traverse each list
        # Have a dummy node since we are making new list
        # Check values, choose smaller value, move that pointer across
        # continue until one pointer reaches tail, then just add remaining list to tail

        dummy = ListNode()
        head = dummy
        
        p1 = list1
        p2 = list2


        while p1 is not None and p2 is not None:

            if p1.val <= p2.val:
                head.next = p1
                p1 = p1.next
            elif p1.val >= p2.val:
                head.next = p2
                p2 = p2.next
            
            head = head.next

        while p1 is not None:
            head.next = p1
            p1 = p1.next
            head = head.next

        
        while p2 is not None:
            head.next = p2
            p2 = p2.next
            head = head.next

        return dummy.next



        