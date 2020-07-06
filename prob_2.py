# 5min

# define linked list
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def addTwoNumbers(l1, l2):
    pseudoHead = ListNode(-1)
    ret = pseudoHead
    carry = 0
    while l1 and l2:
        ret.next = ListNode(-1)
        carry, ret.next.val = divmod(l1.val + l2.val + carry, 10)
        l1, l2, ret = l1.next, l2.next, ret.next
    while l1:
        ret.next = ListNode(-1)
        carry, ret.next.val = divmod(l1.val + carry, 10)
        l1, ret = l1.next, ret.next
    while l2:
        ret.next = ListNode(-1)
        carry, ret.next.val = divmod(l2.val + carry, 10)
        l2, ret = l2.next, ret.next
    if carry:
        ret.next = ListNode(1)
    return pseudoHead.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
print(addTwoNumbers(l1, l2).val)

