class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

p1 = node1
prev = None

while p1

n1 = node1
while n1 is not None:
    print(n1.data,end=" -> ")
    n1 = n1.next
print("None")