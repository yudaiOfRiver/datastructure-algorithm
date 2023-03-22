class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList(object):
    
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def insert(self, n, data):
        if n == 0 or not self.length:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node        
            
        else:
            current_node = self.head
            while current_node.next:
                n -= 1
                if n == 0:
                    break
                current_node = current_node.next

            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        self.length += 1

    def __str__(self) -> str:
        elems = ''
        current_node = self.head
        while current_node:
            if current_node.next is None:
                elems += str(current_node.data)
            else:
                elems += str(current_node.data) + ','
            current_node = current_node.next
        return '[' + elems + ']'

    def __len__(self):
        return self.length

if __name__ == '__main__':
    linked_List = LinkedList()
    print(linked_List)

    linked_List.insert(0, "Yudai")
    print(linked_List)

    linked_List.insert(1,"Syota")
    print(linked_List)

    linked_List.insert(2, "Kaito")
    print(linked_List)
    
    linked_List.insert(2, "Kanako")
    print(linked_List)
