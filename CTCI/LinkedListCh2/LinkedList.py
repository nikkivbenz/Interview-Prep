class Node(object): 
    def __init__(self, data = None, next_node = None): 
        self.data = data
        self.next_node = next_node
    
class LinkedList(object): 

    def __init__(self, head = None): 
        self.head = head

    def toString(self): 
        toString = ""
        current = self.head
        while current != None: 
            toString += f"{str(current.data)} =>" 
            current = current.next_node

        return toString

    def addNode(self, node): 
        current = self.head
        while current.next_node != None: 
            current = current.next_node
        current.next_node = node

    def size(self): 
        size = 0
        current = self.head
        while current != None: 
            size += 1
            current = current.next_node
        return size 

    def insertAtHead(self, node): 
        current = self.head
        self.head = node
        node.next_node = current



