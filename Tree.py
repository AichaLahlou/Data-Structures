# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 22:28:41 2024

@author: Aicha
"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class Tree:
  def __init__(self):
    self.root = None

  def is_empty(self):
    return self.root is None

  def add(self, data):
      if self.is_empty():
          self.root = TreeNode(data)
      else:
          self._add_recursive(data, self.root)

  def _add_recursive(self, data, current_node):
    if data < current_node.data:
      if current_node.left is None:
        current_node.left = TreeNode(data)
      else:
        self._add_recursive(data, current_node.left)
    elif data > current_node.data:
      if current_node.right is None:
        current_node.right = TreeNode(data)
      else:
        self._add_recursive(data, current_node.right)

    def find_element(self, data):
        current = self.root
        while current is not None:
            if current.data == data:
                return True
            elif data < current.data:
                current = current.left
            elif data > current.data:
                current = current.right
        return False


    def delete(self, data):
      self.root = _delete(self.root, data)

    def _delete(self, root, data):
      if root is None: return root
      if data < root.data:
        root.left = self._delete(root.left, data)
      if data > root.data:
        root.right = self._delete(root.right_data)
      if data == root.data:
        if root.left is None:
          return root.right
        elif root.right is None:
          return root.left
        root.data = self.find_min(root.right)
        root.right = self._delete_node(root.right, root.data)
      return root

    def find_min(self, node):
      current = node
      while current.left is not None:
        current = current.left
      return current.data

    def in_order_traversal(self):
      result = []
      if self.root:
        result.extend(in_order_traversal(self.root.left))
        result.append(self.root.value)
        result.extend(in_order_traversal(self.root.right))
      return result

    def print_in_order(self, start = None):
      if start is None:
        start = self.root
      if start.left: self.print_in_order(start.left)
      print(start.value)
      if start.right: self.print_in_order(start.right)