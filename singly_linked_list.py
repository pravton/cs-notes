# Define the Node class for the singly linked list
class Node:
  # Constructor initializes the node with a value and an optional next pointer
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

  # Method to get the value of the node
  def get_value(self):
    return self.value

  # Method to get the next node pointer
  def get_next_node(self):
    return self.next_node

  # Method to set the next node pointer
  def set_next_node(self, next_node):
    self.next_node = next_node

# Define the LinkedList class
class LinkedList:
  # Constructor initializes the linked list with an optional head node
  def __init__(self, value=None):
    self.head_node = Node(value)

  # Method to get the head node
  def get_head_node(self):
    return self.head_node

  # Method to insert a new node at the beginning of the list
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node

  # Method to convert the linked list to a string representation
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list

  # Method to remove a node by its value
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    # If the head node is the one to be removed, adjust the head pointer
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      # Traverse the list to find and remove the node
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node
