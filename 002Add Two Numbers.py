class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        # for debugging
        return repr(self.val)


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        Algorithm: Two pointers & math
        Two pointers for l1 and l2 respectively
        Math - carry for addition, in the form of new node
        :param l1: linked list head node
        :param l2: linked list head node
        :return: ListNode
        """
        result_head = ListNode(0)

        cur1 = l1
        cur2 = l2
        cur = result_head
        l3s = []
        #print('result_head的值为', result_head,cur,cur1,cur2)
        while cur1 or cur2:
            cur.val = cur.val+self.addNode(cur1, cur2)
            if cur.val < 10:
                if cur1 and cur1.next or cur2 and cur2.next:  # next node
                    cur.next = ListNode(0)
            else:
                cur.val -= 10
                cur.next = ListNode(1)

            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
            #print('当前Cur的值为:', result_head, cur)
            l3s.append(cur)
            cur = cur.next
            #print(l3s)
        return l3s


    def addNode(self, node1, node2):
        """
        Handles None situation
        :param node1: ListNode
        :param node2: ListNode
        :return: integer, summation
        """
        if not node1 and not node2:
            raise Exception("two nodes are None")
        if not node1:
            return node2.val
        if not node2:
            return node1.val
        return node1.val+node2.val


if __name__ == "__main__":
    l1s = [ListNode(2),ListNode(4),ListNode(3)]
    l2s = [ListNode(5), ListNode(6),ListNode(4)]
    for i in range(len(l1s)-1):
        l1s[i].next = l1s[i+1]
    for i in range(len(l2s)-1):
        l2s[i].next = l2s[i+1]
    print(Solution().addTwoNumbers(l1s[0], l2s[0]))
