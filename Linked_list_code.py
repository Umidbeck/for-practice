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


