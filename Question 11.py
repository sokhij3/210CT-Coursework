class Node(object):
    def __init__(self, value):
        self.value=value
        self.next=None
        self.prev=None

class List(object):
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,n,x):
        #Not actually perfect: how do we prepend to an existing list?
        if n!=None:
            x.next=n.next
            n.next=x
            x.prev=n
            if x.next!=None:
                x.next.prev=x
        if self.head==None:
            self.head=self.tail=x
            x.prev=x.next=None
        elif self.tail==n:
            self.tail=x
    def delete(self, n):                        #while the current value is not None,
        current = self.head                     #if it == the value you want to delete
        previous = None                         #and if previous is not none, the current
        while current != None:                  #value becomes the next value in the list 
            if current.value == n:              #therefore deleting the value.
                if previous != None:            #if the previous node does == none then the current node
                   previous.next = current.next #(self.head, the top value) becomes the next node.
                else:
                    current = current.next      # It then iterates through the list
            previous = current
            current = current.next

    def display(self):
        values=[]
        n=self.head
        while n!=None:
            values.append(str(n.value))
            n=n.next
        print("List: ",",".join(values))

if __name__ == '__main__':
    l=List()
    l.insert(None, Node(4))
    l.insert(l.head,Node(6))
    l.insert(l.head,Node(8))
    l.delete(8)
    l.display()
    
