# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=""
        s2=""
        while(l1):
            s1=s1+str(l1.val)
            l1 = l1.next
        first_number = int(s1[::-1])
        while(l2):
            s2=s2+str(l2.val)
            l2 = l2.next
        second_number = int(s2[::-1])
        result_number= first_number+second_number
        #result_number = int(str(result)[::-1])
        #print(result_number)
        head = None
        list_pointer = ListNode()
        while(result_number):
            remainder = result_number % 10
            result_number = result_number // 10
            node = ListNode(remainder)
            if head == None:
                head = node
                list_pointer = head
            else:
                while(head.next):
                    head = head.next
                head.next = node
        return list_pointer


        
