class Node:  
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
  
  
class LinkedList: 
    
    def __init__(self):
        self.head = None  

    def List_1(self, new_data):          
        new_node = Node(new_data)          
        new_node.next = self.head       
        if self.head is not None:
            self.head.prev = new_node        
        self.head = new_node

    def reverse(self):
        temp = None
        current = self.head          
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev        
        if temp is not None:
            self.head = temp.prev    
  
    def printList(self, node):
        while(node is not None):
            print(node.data)
            node = node.next  


l1 = LinkedList()
l1.List_1(1)
l1.List_1(2)
l1.List_1(3)
l1.List_1(4)
  
print ("Заданный список")
l1.printList(l1.head)
l1.reverse()  
print ("Перевернутый список")
l1.printList(l1.head)
