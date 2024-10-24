class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        
        
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        last = self.head 
        while last.next:
            last = last.next
        last.next = new_node
        
    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
            
        if not temp:
            return
        prev.next = temp.next
        temp = None
        
        
    def print_list(self):
        if not self.head:
            return
        temp  = self.head
        while temp:
            print(temp.head, end = " ->")
            temp = temp.next
        
        
# ----------------------------------- Linked Listga oid masalalar--------------


#listA - The first linked list.
#listB - The second linked list.
#skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
#skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.

#The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.



class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        def get_length(head):
            len = 0
            while head:
                head = head.next
                len +=1
            return len

        len_a = get_length(headA)
        len_b = get_length(headB)
        while len_a > len_b:
            headA = headA.next
            len_a -= 1
        while len_b > len_a:
            headB = headB.next
            len_b -= 1

        while headA.next and headB.next:
            if headA== headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None