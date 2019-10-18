class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepand(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        if self.head is not None:
            new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("There is not previous node exist!!")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def len_iterative(self):
        curr_node = self.head
        count = 0
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count

    def len_recursive(self,node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def delete_node(self,key):
        curr_node = self.head
        
        if curr_node is None:
            print("Linked List is Empty!!")
            return

        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return
        prev = None
        while curr_node and curr_node.data != key:
            prev = curr_node
            curr_node = curr_node.next
        prev.next = curr_node.next
        curr_node = None

    def delete_node_at_position(self,position):
        curr_node = self.head
        if position == 0:
            slef.head = curr_node.next
            curr_node = None
            return
        if curr_node is None:
            print("Linked list is Empty!!")
            return
        count = 1
        prev = None
        while curr_node and count != position:
            prev = curr_node
            curr_node = curr_node.next 
            count+=1
        prev.next = curr_node.next
        curr_node = None
        
    def reverse_ll1(self,value):
        curr_node = value
        if curr_node is None:
            return
        prev = self.reverse_ll(curr_node.next)
        print(curr_node.data)            

    def print_ll(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

llist = LinkedList()
llist.append(20)
llist.append(30)
llist.append(40)
llist.append(50)
llist.prepand(100)
llist.prepand(200)
llist.prepand(300)
llist.prepand(400)
llist.insert_after_node(llist.head.next.next.next.next.next.next, "E")
llist.print_ll()
print("Len of Linked-List:-", llist.len_iterative()+1)
print("len in Recursive_Manner:-",llist.len_recursive(llist.head)+1)
# llist.delete_node(50)
# llist.delete_node(400)
# llist.delete_node_at_position(3)
# llist.print_ll()
llist.reverse_ll1(llist.head)


