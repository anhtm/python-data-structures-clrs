class Node:
  def __init__(self, key = None):
    self.key = key
    self.next = None

class DoublyNode(Node):
  def __init__(self, key = None):
    Node.__init__(self)
    self.prev = None
    self.key = key