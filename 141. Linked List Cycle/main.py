# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head == None or head.next == None:
            return False

        lp, rp = head, head.next

        while True:

            if rp == None or rp.next == None:
                return False

            if lp == rp:
                return True
            
            lp = lp.next
            rp = rp.next.next