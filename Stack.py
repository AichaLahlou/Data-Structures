# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 22:27:12 2024

@author: Aicha
"""

class Stack:
  def __init__(self):
    self.items = []
    
  def is_empty(self):
    return len(self.items)==0

  def add(self, item):
    self.items.append(item)
    
  def remove(self):
    if not self.is_empty():        
      return self.items.pop()
  
  def size(self):
    return len(self.items)

  def peek(self):
    if not self.is_empty():
      return self.items[-1]