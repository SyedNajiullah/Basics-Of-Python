class Node:
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev

class Linked_List:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        if self.head == None:
            self.head = Node(data, None, None)
        else:
            new_node = Node(data, None, None)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_at_tail(self, data):
        if self.head == None:
            self.head = Node(data, None, None)
        else:
            i = self.head
            while i.next != None:
                i = i.next
            new_node = Node(data, None, None)
            i.next = new_node
            new_node.prev = i        

    def delete_from_head(self):
        if self.head == None:
            print("Linked List is empty")
        elif self.head.next == None:
            i = self.head.data
            del self.head
            self.head = None
            return i
        else:
            i = self.head.data
            self.head = self.head.next
            del self.head.prev
            self.head.prev = None
            return i
        
    def delete_from_tail(self):
        if self.head == None:
            print("likned List is empty")
        elif self.head.next == None:
            i = self.head.data
            del self.head
            self.head = None
            return i
        else:
            i = self.head
            while i.next.next != None:
                i = i.next
            rv = i.next.data
            del i.next
            i.next = None
            return rv

    def display(self):
        if self.head == None:
            print("Linked List is empty")
        else:
            i = self.head
            while i != None:
                print(i.data, end = " ")
                i = i.next
            print()
        
    def delete_all_nodes(self):
        while self.head != None:
            if self.head.next == None:
                del self.head
                self.head = None
            else:
                self.head = self.head.next
                del self.head.prev
                self.head.prev = None

def main():
    linked_list = Linked_List()

    while True:
        print("enter 1: insert at head")
        print("enter 2: insert at tail")
        print("enter 3: delete from head")
        print("enter 4: delete from tail")
        print("enter 5: display")
        print("enter 6: break")
        i = int(input("Enter Here :-"))
        if i == 1:
            data = input("Enter data here :-")
            linked_list.insert_at_head(data)
        elif i == 2:
            data = input("Enter data here :-")
            linked_list.insert_at_tail(data)
        elif i == 3:
            print("Deleted info :-", linked_list.delete_from_head())
        elif i == 4:
            print("Deleted info :-", linked_list.delete_from_tail())
        elif i == 5:
            linked_list.display()
        elif i == 6:
            break
        else:
            print("Invalid input enter again")
    
    linked_list.delete_all_nodes()


if __name__ == "__main__":
    main()