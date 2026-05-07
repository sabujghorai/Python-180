class Node :
    def __init__(self,value = None):
        self.data = value
        self.next = None
        self.prev = None

class DoubleLL :
    def __init__(self):
        self.head = None

    def insertAtTheEnd(self,value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        
        t = self.head 
        while(t.next != None):
            t = t.next

        t.next = temp
        temp.prev = t

    def InsertAtBegeining(self,value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def InsertAtMiddle(self,value,x):
        t = self.head

        while(t.next != None):
            if(t.data == x):
                break
            else:
                t = t.next
        temp = Node(value)
        temp.next = t.next
        t.next.prev = next
        t.next = temp
        temp.prev = t

    def deletionDLL(self,value): # the method for deletion the element
        if(self.head == None):
            print("The linked list is empty ")
            return
        
        t = self.head
        if(t.data == value): # code for deletion at the begeinning
            self.head = t.next
            self.head.prev = None #upto this
            return
        
        while(t.next != None): # code for deletion at the middle
            if(t.data == value):
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            else:
                t = t.next # upto this
        if(t.data == value):
            t.prev.next = None

    def printDLL(self):
        t = self.head
        while(t.next != None):
            print(t.data, end= " <--> ")
            t = t.next
        print(t.data)

obj  = DoubleLL()
obj.insertAtTheEnd(10)
obj.insertAtTheEnd(20)
obj.insertAtTheEnd(30)
obj.InsertAtBegeining(5)
obj.InsertAtMiddle(15,10) # insert 15 after 10
obj.InsertAtMiddle(25,20) # insert 25 after 20
obj.deletionDLL(5)
obj.deletionDLL(15)
# obj.deletionDLL(30)
obj.printDLL()