# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 22:30:03 2024

@author: Aicha
"""

class Heap:

  def __init__(self):
    self.heap = []

  def is_empty(self):
    return len(self.heap)== 0

  def parent(self, i):
    return (i - 2 )//2
  def left_child(self, i):
    return (i*2)+1
  def right_child(self, i):
    return(i*2) + 2

  def has_left_child(self, i):
    return self.left_child(self, i)< len(self.heap)
  def has_right_child(self, i):
    return self.right_child(self, i)< len(self.heap)

  def peek(self):
    if not self.is_empty(): return self.heap[0]
    
  def swap(self, i, j):
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

  def heapify_up(self, i):
      while i> 0 and self.heap[i] < self.heap[self.parent(i)]:
          self.swap(i, self.parent(i))
          i = self.parent(i)

  def insert(self, value):
    self.heap.append(value)
    self.heapify_up(len(self.heap)- 1)

  def heapify_down(self):
      index = 0
      heap_size = len(self.heap)

      while self.has_left_child(index):
        left_child_index = self.left_child(index)
        right_child_index = self.right_child(index)
        smallest = index

        if left_child_index < heap_size and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index

        if right_child_index < heap_size and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index
        
        if smallest != index:
            self.swap(smallest, index)
            index = smallest
        else:
            break

  def remove_peak(self):
    if self.is_empty(): return
    if len(self.heap)== 1: self.heap.pop()
    self.heap[0] = self.heap.pop()
    self.heapify_down()