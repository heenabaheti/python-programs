"""
  queue is a Fifo structure. insertion will happen at rear end and
  deletion occurs from front end
  """


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueStructure:
   def __init__(self):
      self.head = None
      self.last = None

   def enqueue(self, data):
    # checking is the queue is empty if is empty then insertion will happen at head node
      if self.last is None:
         self.head = Node(data)
         self.last = self.head
      else:
         self.last.next = Node(data)
         self.last = self.last.next

   def dequeue(self):
    # if queue is empty then return none
      if self.head is None:
         return None
      else:
         val_returned = self.head.data
         self.head = self.head.next
         return val_returned

   def printing(self):           # printing elements of the queue
      if self.head is None:
         print("list is empty")
         return
      itr = self.head
      lstr = ' '
      while itr:
         lstr += str(itr.data) + '   '
         itr = itr.next
      print(lstr)

   def queue_size(self):
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
   qs = QueueStructure()
   while True:
      print('1. enqueue')
      print('2. dequeue')
      print('3. Size_of')
      print('4. quit')
      var = int(input('What operation would you like to perform ? '))
      if var == 1:
         value = input("Enter value to be insert in queue : ")
         qs.enqueue(value)
         print("Items in the Queue now: ")
         qs.printing()
      if var == 2:
         dequeued = qs.dequeue()
         if dequeued is None:
            print('The queue is empty.')
         else:
            print('The deleted element is : ', int(dequeued))
            qs.printing()
      if var == 3:
         qs.queue_size()
      if var == 4:
         break

if __name__ == "__main__":
   main()
