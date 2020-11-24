class PQueue:
  ROOT_IDX = 1
  MAX_SIZE = 100
  def __init__(self, comp):
    self.comp = comp
    self.arr = [None] * self.MAX_SIZE
    self.num_of_data = 0

  def get_parent_idx(self, idx):
    return idx // 2

  def get_left_child_idx(self, idx):
    return idx * 2

  def get_right_child_idx(self, idx):
    return idx * 2 + 1

  def has_child(self, idx):
    if self.num_of_data >= self.get_left_child_idx(idx):
      return True
    else:
      return False

  def get_high_priority_child_idx(self, idx):
    if not self.has_child(idx):
      return 0
    else:
      left_child_idx = self.get_left_child_idx(idx)
      right_child_idx = self.get_right_child_idx(idx)
      if left_child_idx == self.num_of_data:
        return left_child_idx
      else:
        if self.comp(self.arr[left_child_idx], self.arr[right_child_idx]) < 0:
          return left_child_idx
        else:
          return right_child_idx

  def enqueue(self, data):
    if self.is_full():
      print('Can not enqueue. queue is full')
      return

    idx = self.num_of_data + 1
    while idx != self.ROOT_IDX:
      parent_idx = self.get_parent_idx(idx)
      # if data priority is higher than parent node priority
      if self.comp(data, self.arr[parent_idx]) < 0:
        self.arr[idx] = self.arr[parent_idx]
        idx = parent_idx
      else:
        break

    self.arr[idx] = data
    self.num_of_data += 1

  def is_full(self):
    return self.num_of_data == self.MAX_SIZE

  def dequeue(self):
    if self.is_empty():
      print("Can not dequeue. queue is empty")
      return

    ret_node = self.arr[self.ROOT_IDX]
    last_node = self.arr[self.num_of_data]

    parent_idx = self.ROOT_IDX
    idx = self.get_high_priority_child_idx(parent_idx)

    while idx != 0:
      curr_node = self.arr[idx]
      # if last node priority is lower than current node
      if self.comp(last_node, curr_node) >= 0:
        self.arr[parent_idx] = curr_node
        parent_idx = idx
        idx = self.get_high_priority_child_idx(parent_idx)
      else:
        break

    self.arr[parent_idx] = last_node
    self.num_of_data -= 1
    return ret_node

  def is_empty(self):
    return self.num_of_data == 0


if __name__ == '__main__':
  heap_types = ['min heap', 'max heap']
  comp_funcs = [lambda x, y: x-y, lambda x, y: y-x]

  for heap_type, comp_func in zip(heap_types, comp_funcs):
    pq = PQueue(comp_func)
    input_list = [1, 3, 7, 4, 9, 12, 13, 15, 8]
    for val in input_list:
      pq.enqueue(val)

    print('heap type : ' + heap_type)
    for _ in range(0, pq.num_of_data):
      print(pq.dequeue())
    print()