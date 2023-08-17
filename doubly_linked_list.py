# Define the Node class for the doubly linked list
class Node:
  # Constructor initializes the node with a value and optional next and previous pointers
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node

  # Method to set the next node pointer
  def set_next_node(self, next_node):
    self.next_node = next_node

  # Method to get the next node pointer
  def get_next_node(self):
    return self.next_node

  # Method to set the previous node pointer
  def set_prev_node(self, prev_node):
    self.prev_node = prev_node

  # Method to get the previous node pointer
  def get_prev_node(self):
    return self.prev_node

  # Method to get the value of the node
  def get_value(self):
    return self.value

# Define the DoublyLinkedList class
class DoublyLinkedList:
  # Constructor initializes the linked list with optional head and tail pointers
  def __init__(self):
    self.head_node = None
    self.tail_node = None

  # Method to add a new node to the head of the list
  def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node

    # If there's an existing head, adjust pointers
    if current_head != None:
      current_head.set_prev_node(new_head)
      new_head.set_next_node(current_head)

    # Set the new node as the head
    self.head_node = new_head

    # If there's no tail, set the new node as the tail
    if self.tail_node == None:
      self.tail_node = new_head

  # Method to add a new node to the tail of the list
  def add_to_tail(self, new_value):
    new_tail = Node(new_value)
    current_tail = self.tail_node

    # If there's an existing tail, adjust pointers
    if current_tail != None:
      current_tail.set_next_node(new_tail)
      new_tail.set_prev_node(current_tail)

    # Set the new node as the tail
    self.tail_node = new_tail

    # If there's no head, set the new node as the head
    if self.head_node == None:
      self.head_node = new_tail

  # Method to remove the head node
  def remove_head(self):
    removed_head = self.head_node

    # If there's no head, return None
    if removed_head == None:
      return None

    # Move the head pointer to the next node
    self.head_node = removed_head.get_next_node()

    # If there's a new head, set its previous pointer to None
    if self.head_node != None:
      self.head_node.set_prev_node(None)

    # If the removed head was also the tail, remove the tail
    if removed_head == self.tail_node:
      self.remove_tail()

    # Return the value of the removed head
    return removed_head.get_value()

  # Method to remove the tail node
  def remove_tail(self):
    removed_tail = self.tail_node

    # If there's no tail, return None
    if removed_tail == None:
      return None

    # Move the tail pointer to the previous node
    self.tail_node = removed_tail.get_prev_node()

    # If there's a new tail, set its next pointer to None
    if self.tail_node != None:
      self.tail_node.set_next_node(None)

    # If the removed tail was also the head, remove the head
    if removed_tail == self.head_node:
      self.remove_head()

    # Return the value of the removed tail
    return removed_tail.get_value()

  # Method to remove a node by its value
  def remove_by_value(self, value_to_remove):
    node_to_remove = None
    current_node = self.head_node

    # Traverse the list to find the node with the given value
    while current_node != None:
      if current_node.get_value() == value_to_remove:
        node_to_remove = current_node
        break
      current_node = current_node.get_next_node()

    # If the node wasn't found, return None
    if node_to_remove == None:
      return None

    # If the node to remove is the head or tail, use the respective methods
    if node_to_remove == self.head_node:
      self.remove_head()
    elif node_to_remove == self.tail_node:
      self.remove_tail()
    else:
      # Otherwise, adjust the pointers of the adjacent nodes
      next_node = node_to_remove.get_next_node()
      prev_node = node_to_remove.get_prev_node()
      next_node.set_prev_node(prev_node)
      prev_node.set_next_node(next_node)

    # Return the removed node
    return node_to_remove

  # Method to convert the linked list to a string representation
  def stringify_list(self):
    string_list = ""
    current_node = self.head_node
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
