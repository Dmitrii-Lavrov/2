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

    def printList(self, node):
        while(node is not None):
            print(node.data, end = ' ')
            node = node.next  

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
  
    
def bubbleSort(self):
        swapped = 0
        temp = None    
        
      
        while True:
            swapped = 0
            current = self  
            while (current.next is not temp):       
                if (current.data > current.next.data):           
                    current.data, current.next.data = current.next.data, current.data
                    swapped = 1;       
                current = current.next;       
            temp = current;    
            if swapped == 0:
                break

    

l1 = LinkedList()
l1.List_1(1)
l1.List_1(2)
l1.List_1(5)
l1.List_1(7)
l1.List_1(6)
l1.List_1(9)
l1.List_1(3)
  
print ("Заданный список")
l1.printList(l1.head)
reverse(l1)  
print ("\nПеревернутый список")
l1.printList(l1.head)
bubbleSort(l1.head)
print ("\nОтсортированный список")
l1.printList(l1.head)


