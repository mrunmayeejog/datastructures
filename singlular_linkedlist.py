class sll_node:
     def __init__(self, value):
        self.data = value
        self.next = None


class sll:
    def __init__(self):
        self.head = None

    def print_list(self):
        if not self.head:
            print("Linked list is empty")
            return

        curr = self.head
        print("Linked list -->", end = " ")
        while curr:
            print("" + str(curr.data) + " --->", end = " ")
            curr = curr.next
        print("NULL")

    def insert_node(self, value):
        new_node = sll_node(value)
        if not self.head:
            self.head = new_node
            print("Head created")
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def insert_at_position(self, index, value):
        new_node = sll_node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head.next
            prev = self.head
            i = 1
            while curr:
                if i == index:
                    prev.next = new_node
                    new_node.next = curr
                    print("New value " + str(value) + " inserted at position " + str(i))
                    return
                prev = curr
                curr = curr.next
                i += 1
            if i == index:
                self.insert_node(value)
                return
            print("Invalid index " + str(index))

    def search_node(self, value):
        curr = self.head
        i = 0
        while curr:
            if curr.data == value:
                print("Value " + str(value) + " found at " + str(i) + " position")
                return
            i += 1
            curr = curr.next

        print("Value "+ str(value) + " not found in Linked List")

    def delete_by_index(self, index):
        if index == 0:
            value = self.head.data
            self.head = self.head.next
            print("Value " + str(value) + " at index " + str(index) + " deleted")
        else:
            curr = self.head.next
            i = 1
            prev = self.head
            while curr:
                if i == index:
                    value = curr.data
                    prev.next = curr.next
                    print("Value " + str(value) + " at index " + str(i) + " deleted")
                    return
                prev = curr
                curr = curr.next
                i += 1
            print("invalid index " + str(index))

    def delete_by_value(self, value):
        curr = self.head
        prev = None
        if curr.data == value:
            self.head = curr.next
            print("Value " + str(value) + " at position 0 deleted")
        else:
            i = 1
            while curr:
                if curr.data == value:
                    prev.next = curr.next
                    print("Value " + str(value) + " at position" + str(i) + " deleted")
                    return
                prev = curr
                curr = curr.next
                i += 1
            print("Value " + str(value) + " not found in linkedlist")

    def reverse(self):
        if self.head is None:
            print("List is empty")
        prev = self.head
        if prev.next is None:
            return
        curr = prev.next
        prev.next = None
        nextn = curr.next
        while curr:
            curr.next = prev
            prev = curr
            if nextn:
                curr = nextn
                nextn = curr.next
            else:
                break
        self.head = curr

if __name__ == "__main__":
    s = sll()
    s.insert_node(1)
    s.insert_node(2)
    s.insert_node(3)
    s.insert_node(4)
    s.print_list()
    s.reverse()
    s.print_list()