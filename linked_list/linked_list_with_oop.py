class Node:
  def __init__(self, data, next=None):
    self.data = data
    self.next = next


class NodeManager:
  def __init__(self, data):
    self.head = Node(data)

  def add(self, data):
    if self.head is None:
      self.head = Node(data)

    else:
      node = self.head
      while node.next:
        node = node.next
      node.next = Node(data)

  def delete(self, data):
    if self.head is None:
      print('no data')
      return

    if self.head.data == data:
      temp = self.head
      self.head = self.head.next
      del temp
    else:
      node = self.head
      while node.next:
        if node.next.data == data:
          temp = node.next
          node.next = node.next.next
          del temp
        else:
          node = node.next

  def desc(self):
    node = self.head
    while node:
      print(node.data)
      node = node.next


node_manager = NodeManager(0)
node_manager.desc()
print(node_manager.head, end='\n\n')

node_manager.delete(0)
print(node_manager.head, end='\n\n')

print('add 1 to 9')
for data in range(1, 10):
  node_manager.add(data)
node_manager.desc()

print('delete 4')
node_manager.delete(4)
node_manager.desc()

print('delete 9')
node_manager.delete(9)
node_manager.desc()
