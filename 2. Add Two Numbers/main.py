# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        firstSum = l1.val + l2.val
        carry = False if firstSum < 10 else True
        
        result = ListNode(firstSum - (10 if carry else 0))

        l1 ,l2 = l1.next, l2.next

        count = result

        while l1 != None or l2 != None:
            
            currSum = 1 if carry else 0
            carry = False

            if l1 != None:
                currSum += l1.val
                l1 = l1.next

            if l2 != None:
                currSum += l2.val
                l2 = l2.next

            if currSum > 9:
                carry = True
                currSum -= 10
            
            count.next = ListNode(currSum)
            count = count.next


        if carry:
            count.next = ListNode(1)
            count = count.next

        carry = False
        return result