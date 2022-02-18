class Node:
     def __init__(self, value):
          self.value = value
          self.next_node = None

class Linked_list:
     def __init__(self):
          self.head = None

     def insert(self, value):
          self.node = Node(value)
          if self.head == None:
               self.head = self.node
          else:
               self.current_node = self.head
               while self.current_node.next_node is not None:
                    self.current_node = self.current_node.next_node
               self.current_node.next_node = self.node

     def show_ele(self):
          self.current_node = self.head
          while self.current_node is not None:
               print(self.current_node.value, end=',')
               self.current_node = self.current_node.next_node

     def search_ele(self, value):
          self.current_node = self.head
          while self.current_node is not None:
               if value == self.current_node.value:
                    return True
               else:
                    self.current_node = self.current_node.next_node
          return False

     def delete_ele(self, value):
          if self.head.value == value:
               self.head = self.head.next_node
               self.size -= 1
               return value, "is deleted."
          else:
               self.current_node = self.head
               while self.current_node.next_node is not None:
                    if self.current_node.next_node.value == value:
                         self.current_node.next_node = self.current_node.next_node.next_node
                         self.size -= 1
                         return value, "is deleted."
                    else:
                         self.current_node = self.current_node.next_node
               if self.current_node.value == value:
                    self.current_node = None
                    self.size -= 1
                    return value, "is deletedd."
               else:
                    return value, "does not exist."

     def list_size(self):
          self.size = 0
          self.current_node = self.head
          while self.current_node is not None:
               self.size += 1
               self.current_node = self.current_node.next_node
          return "size: ",self.size

list1 = Linked_list()
list1.insert(1)
list1.insert(2)
list1.insert(3)
list1.insert(4)
list1.insert(5)

list1.show_ele()
print(list1.list_size())

print(list1.delete_ele(4))
list1.show_ele()
print(list1.list_size())

print(list1.delete_ele(2))
list1.show_ele()
print(list1.list_size())