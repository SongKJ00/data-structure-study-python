class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

  def __init__(self, data, next=None):
    self.data = data
    self.next = next


def add(data):
  node = head
  while node.next:
    node = node.next
  node.next = Node(data)


def print_all():
  node = head
  while node.next:
    print(node.data)
    node = node.next
  print(node.data)


# insert
node1 = Node(1)
head = node1
for index in range(2, 10):
  add(index)
print_all()

# middle insert
node = head
node3 = Node(1.5)
search = True
while search:
  if node.data == 1:
    search = False
  else:
    node = node.next

node_next = node.next
node.next = node3
node3.next = node_next
print_all()