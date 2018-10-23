class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def addEnd(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else: 
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node             
        self.size += 1

    def printLl(self):
        result = ''
        temp = self.head
        while temp.next != None: 
            result += str(temp.value)+'->'
            temp = temp.next
        result += str(temp.value)
        print(result)

    def insertAfter(self,prev_node, value):
        if prev_node is None:
            print('Previous node not on linked list')
            return
        new_node=Node(value)
        new_node.next=prev_node.next
        prev_node.next=new_node

    def insertIdx(self, value, idx):
        new_node=Node(value)
        count=0
        if self.head==None:
            self.head=new_node
        else: 
            temp1=self.head
            temp2=self.head
            while temp1.next and temp2.next != None:
                temp1=temp1.next
                temp2=temp2.next
                count+=1 
                if count==idx-1:
                    temp1.next=new_node
                if count==idx+1:
                    new_node=temp2
        self.size+=1

                
                
        
newLl = LinkedList()

newLl.addEnd(2)
newLl.addEnd(3)
newLl.addEnd(4)
newLl.addEnd(5)
newLl.addEnd(6)
newLl.addEnd(7)
newLl.addEnd(8)
newLl.addEnd(9)

newLl.insertIdx(10,3)

newLl.printLl()

