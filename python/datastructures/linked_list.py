class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def addend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else: 
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node             
        self.size += 1

    def print_ll(self):
        result = ''
        temp = self.head
        while temp.next != None: 
            result += str(temp.value)+'->'
            temp = temp.next
        result += str(temp.value)
        print(result)

        
newll = LinkedList()

newll.addend(2)
newll.addend(3)
newll.print_ll()


