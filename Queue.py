class Node:
     def __init__(self, value):
          self.value = value
          self.next_node = None

class Queue:
     def __init__(self):
          self.head = None

     # inserting elements in queue
     def insert(self, value):
          self.node = Node(value)
          if self.head == None:
               self.head = self.node
          else:
               self.current_node = self.head
               while self.current_node.next_node is not None:
                    self.current_node = self.current_node.next_node
               self.current_node.next_node = self.node

     # printing whole queue
     def show_ele(self):
          self.current_node = self.head
          while self.current_node is not None:
               print(self.current_node.value, end = ",")
               self.current_node = self.current_node.next_node

     # deleting first element
     def delete_first(self):
          self.first_ele = self.head.value
          self.head = self.head.next_node
          self.size -= 1
          return self.first_ele, "is deleted"

     def list_size(self):
          self.size = 0
          self.current_node = self.head
          while self.current_node is not None:
               self.size += 1
               self.current_node = self.current_node.next_node
          return "size: ",self.size

queue1 = Queue()

queue1.insert(1)
queue1.insert(2)
queue1.insert(3)
queue1.insert(4)
queue1.insert(5)

queue1.show_ele()

print(queue1.list_size())

print(queue1.delete_first())
queue1.show_ele()
print(queue1.list_size())