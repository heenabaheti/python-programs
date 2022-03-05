"""
  deque is a combination from stack & queue structure. insertion will happen at rear and front end,
  deletion occurs from front and rear end
  """


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class DeQueueStructure:
   def __init__(self):
      self.head = None
      self.last = None

   def insert_value(self, data_list):
      self.head = None
      for data in data_list:
         self.add_at_last(data)

   def add_at_front(self, data):
    # checking is the queue is empty if is empty then insertion will happen at head node
      if self.head is None:
         self.head = Node(data)
         self.last = self.head
      else:
         self.head.next = self.head
        # print(self.head.next.data)
         self.head = Node(data)

   def add_at_last(self, data):
    # checking is the queue is empty if is empty then insertion will happen at head node
    if self.last is None:
       self.head = Node(data)
       self.last = self.head
    else:
       self.last.next = Node(data)
       self.last = self.last.next

   def del_at_front(self):
    # if queue is empty then return none
      if self.head is None:
         return None
      else:
         val_returned = self.head.data
         self.head = self.head.next
         return val_returned

   def del_at_last(self):
    # if queue is empty then return none
      if self.head is None:
         return None
      else:
         val_returned = self.last.data
         self.last = self.last.next
         return val_returned

   def printing_deq(self):           # printing elements of the queue
      if self.head is None:
         print("list is empty")
         return
      itr = self.head
      lstr = ' '
      while itr:
         lstr += str(itr.data) + '   '
         itr = itr.next
      print(lstr)

   def deq_size(self):
      count = 0
      if self.head is None:
         print("list is empty")
         return
      itr = self.head
      while itr:
         itr = itr.next
         count += 1
      print("no of elements are", count)


def main():
   qs = DeQueueStructure()
   while True:
      print('1. Create Queue')
      print('2. add at beginning')
      print('3. add at last')
      print('4. delete from front')
      print('5. delete from last')
      print('6. Size_of')
      print('7. quit')
      var = int(input('What operation would you like to perform ? '))
      if var == 1:
         input_string = input('Enter elements into the queue separated by space: ')
         user_list = input_string.split()
         qs.insert_value(user_list)
         print("List is")
         qs.printing_deq()
      if var == 2:
         value = input("Enter value to be insert in queue : ")
         qs.add_at_front(value)
         print("Items in the Queue now: ")
         qs.printing_deq()
      if var == 3:
         value = input("Enter value to be insert in queue : ")
         qs.add_at_last(value)
         print("Items in the Queue now: ")
         qs.printing_deq()
      if var == 4:
         dequeued = qs.del_at_front()
         if dequeued is None:
            print('The queue is empty.')
         else:
            print('The deleted element is : ', int(dequeued))
            qs.printing_deq()
      if var == 5:
         dequeued = qs.del_at_last()
         if dequeued is None:
            print('The queue is empty.')
         else:
            print('The deleted element is : ', int(dequeued))
            qs.printing_deq()
      if var == 6:
         qs.deq_size()
      if var == 7:
         break

if __name__ == "__main__":
   main()
