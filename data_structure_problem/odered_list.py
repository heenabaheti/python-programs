class Node:
    # constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class OrderedList:
    # constructor
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def print(self):
        if self.head is None:
            print("list is empty")
            return
        itr = self.head
        lstr = ' '
        while itr:
            lstr += str(itr.data) + "-->"
            itr = itr.next
        print(lstr)

    def insert_value(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >=self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def search(self, data):
        if self.head is None:
            print("list Is empty")
        itr = self.head
        count = 0
        while itr:
            if itr.data == data:
                print("element fount at location:", count)
                break
            itr = itr.next
            count += 1

if __name__ == "__main__":
    ll = OrderedList()
    while True:
        print("Enter Operation To be perform On Ordered list")
        print("1. create list")
        print("2. Insert into the list")
        print("3. Delete from list")
        print("4. Search element into the list")
        print("5. End Program")
        num = int(input())
        if num == 1:
            input_string = input('Enter elements into the list separated by space: ')
            user_list = input_string.split()
            ll.insert_value(user_list)
            print("List is")
            ll.print()
            continue
        if num == 2:
            val = int(input("Enter value which you ant to add "))
            pos = int(input("enter position at which you want to add data"))
            ll.insert_at(pos, val)
            print("List is")
            ll.print()
        if num == 3:
            val = int(input("enter position from where you want to delete "))
            ll.remove_at(val)
            print("List is")
            ll.print()
        if num == 4:
            val = int(input("enter element which you want to search"))
            ll.search(val)
            print("List is")
            ll.print()
        if num == 5:
            break
        if num < 0 or num > 5:
            print("you entered wrong choice")
            continue






