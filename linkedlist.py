class ListNode:
 def __init__(self, x):
     self.val = x
     self.next = None

class Solution:
    def addTwoNumbers(self, first_linked, second_linked):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
      
        remainder = 0
        head = node = ListNode(None)

        while first_linked or second_linked:
            
            l1_val = 0 if first_linked ==  None  else first_linked.val
            l2_val = 0 if second_linked == None  else second_linked.val
            _sum =l1_val + l2_val + remainder
            temp = ListNode( _sum % 10 )
            remainder = 0 if _sum <=9 else 1

            node.next = temp
            node = temp

            first_linked = first_linked.next if first_linked != None else None
            second_linked = second_linked.next if second_linked != None else None

            if remainder != 0 and (not first_linked and not second_linked ):
                node.next = ListNode(remainder)
        
        head = head.next
        return head

solution = Solution()

node_1 = ListNode(2)
node_1.next = ListNode(4)
node_1.next.next = ListNode(3)
##node_1.next.next.next = ListNode(0)
node_2 = ListNode(5)
node_2.next = ListNode(6)
node_2.next.next = ListNode(4)
x = solution.addTwoNumbers(node_1, node_2)
while x:
    print(x.val)
    x = x.next




