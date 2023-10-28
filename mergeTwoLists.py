# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        # pointer to the current node. We will shift this without shifting head. So head will still point to the top of the node
        curr = head

        if not list1:
            return list2
        if not list2:
            return list1
        if not list1 and not list2:
            return ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        if not list1:
            curr.next = list2
        if not list2:
            curr.next = list1

        return head.next

Solution().mergeTwoLists(ListNode(1, ListNode(2, ListNode(4, None))), ListNode(2, ListNode(3, ListNode(4, None))))