# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 22:27:56 2024

@author: Aicha
"""

class Queue:
  def __init__(self):
    self.items = []
    
  def is_empty(self):
    return len(self.items)== 0

  def size(self):
    return len(self.items)

  def add(self, item):
    self.items.append(item)
    
  def remove(self):
    if not self.is_empty():
      self.items = self.item.pop(0) 
      
  def peek(self):
    if not self.is_empty():
      return self.items[0]