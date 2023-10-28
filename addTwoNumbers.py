# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next: ListNode = next
class Solution(object):
    def __init__(self):
        self.carry = 0

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        """
        return self.recursivelyAdd(l1, l2)

    def recursivelyAdd(self, node1, node2):
        val1 = None if node1 == None else node1.val
        val2 = None if node2 == None else node2.val
        next1 = None if node1 == None else node1.next
        next2 = None if node2 == None else node2.next

        if next1 == None and next2 == None and val1 == None and val2 == None:
            if self.carry == 1:
                return ListNode(1, None)
            else:
                return None
        else:
            return ListNode(self.getSum(val1, val2), self.recursivelyAdd(next1, next2))

    def getSum(self, v1, v2):
        val1 = 0 if v1 == None else v1
        val2 = 0 if v2 == None else v2
        res = val1 + val2 + self.carry
        if res >= 10:
            self.carry = 1
            return int(str(res)[1])
        else:
            self.carry = 0
            return res


# l1 = ListNode(2, ListNode(4, ListNode(3, None)))
# l2 = ListNode(5, ListNode(6, ListNode(4, None)))

l1 = ListNode(0, None)
l2 = ListNode(0, None)

res = Solution().addTwoNumbers(l1, l2)

print(res.val)
# print(res.next.val)
# print(res.next.next.val)