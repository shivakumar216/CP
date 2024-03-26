class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def insert_at_position(self,data,position):
        if position==0:
            self.prepend(data)
            return
        new_node=Node(data)
        current_node=self.head
        for i in range(position-1):
            if current_node is None:
                print("position isout of range")
                return
            current_node=current_node.next
        if current_node is None:
            print("position is out of range")
            return
        new_node.next=current_node.next
        current_node.next=new_node
    def delete(self,data):
            current_node=self.head
            if current_node and current_node.data==data:
                self.head=current_node.next
                current_node=None
                return
            prev_node =None
            while current_node and current_node.data!=data:
                prev_node=current_node
                current_node=current_node.next
            if current_node is None:
                return
            prev_node.next = current_node.next
            current_node=None
    def delete_at_begining(self):
            if self.head:
                self.head=self.head.next
    def delete_at_end(self):
            current_node=self.head
            if current_node and not current_node.next:
                self.head=None
                return
            prev_node=None
            while current_node.next:
                prev_node=current_node
                current_node=current_node.next
            prev_node.next=None
    def delete_at_position(self,position):
            if position==0:
                self.delete_at_begining()
                return
            current_node=self.head
            for i in range(position-1):
                if current_node is None:
                    print("position is out of range")
                    return
                current_node=current_node.next
            if current_node is None or current_node.next is None:
                print("position is out of range")
                return
            current_node.next=current_node.next.next
    def print_list(self):
            current_node=self.head
            while current_node:
                print(current_node.data,end='')
                current_node=current_node.next
                print()

if __name__=="__main__":
    linked_list=LinList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(4)
    linked_list.append(6)
    linked_list.insert_at_position(2,3)
    print("linked list after insertion:")
    linked_list.print_list() 
    linked_list.delete(3)
    linked_list.delete_at_begining()
    linked_list.delete_at_end()
    linked_list.delete_at_position(1)
    print("linked list after deletion:")
    linked_list.print_list()
