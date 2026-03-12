# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # current1 = head
        # count = 0
        # while current1:
        #     count += 1
        #     current1 = current1.next
        # current2 = head
        # steps = count//2
        # while steps:
        #     current2 = current2.next
        #     steps -= 1
        # return current2

        one_step = two_steps = head
        while two_steps and two_steps.next:
            one_step = one_step.next
            two_steps = two_steps.next.next
        return one_step