# Queue Data Structure

## Introduction:

A queue is a fundamental linear data structure that follows the First-In, First-Out (FIFO) principle. In a queue, elements are added at the rear (enqueue operation) and removed from the front (dequeue operation). This ensures that the first element added is the first one to be removed, resembling a real-world queue or line.

## Real-Life Example:

Imagine a line at a ticket counter, where people wait to purchase tickets. The person who arrives first (at the front of the line) gets served first, and new arrivals join at the rear. This scenario mirrors the behavior of a queue data structure, making it a practical concept for modeling real-life situations.

## Usefulness of Queues:

Queues are useful in scenarios where tasks or entities need to be processed in a sequential order. Some common applications include:

- **Task Scheduling:** Managing tasks based on their arrival time, ensuring fairness in processing.
  
- **Print Job Queue:** Printing tasks are processed in the order they are submitted to the printer queue.

- **Breadth-First Search (BFS):** Queues are used in graph traversal algorithms like BFS, exploring nodes level by level.

- **Handling Requests:** In web servers, requests are often handled in the order they are received.

## Queue Representation:

A queue can be visualized as a line with two ends: the front and the rear.

Front  ----------------------------------------    Rear
---------------------------------------------------
| Element 1 | Element 2 | Element 3 | ... | Element N |
---------------------------------------------------

In this representation:

- `Front` indicates the front of the queue where removal occurs.
- `Rear` indicates the rear of the queue where elements are added.
- Elements are added at the rear and removed from the front, following the First-In, First-Out (FIFO) principle.

## Function/Method Descriptions:

Check the implementation in [src/queue.md](src/queue.md) for the details of the `Queue` class.

1. **`__init__` (Initialization):**
   - **Role:** Initializes a new instance of the `Queue` class with an empty list.
   - **Time Complexity:** O(1) - Constant time, as it involves creating an empty list.
   - **Space Complexity:** O(1) - Constant space, as it initializes an empty list.

2. **`is_empty`:**
   - **Role:** Checks whether the queue is empty.
   - **Time Complexity:** O(1) - Constant time, as it involves checking the length of the list.
   - **Space Complexity:** O(1) - Constant space, as it only performs a comparison.

3. **`size`:**
   - **Role:** Returns the number of elements in the queue.
   - **Time Complexity:** O(1) - Constant time, as it involves checking the length of the list.
   - **Space Complexity:** O(1) - Constant space, as it only performs a comparison.

4. **`add`:**
   - **Role:** Adds an element to the rear of the queue.
   - **Time Complexity:** O(1) - Constant time, as it involves appending an element to the end of the list.
   - **Space Complexity:** O(1) - Constant space, as it increases the size of the list by one.

5. **`remove`:**
   - **Role:** Removes and returns the element from the front of the queue.
   - **Time Complexity:** O(1) - Constant time, as it involves removing the first element from the list using `pop(0)`.
   - **Space Complexity:** O(1) - Constant space, as it decreases the size of the list by one.

6. **`peek`:**
   - **Role:** Retrieves the element at the front of the queue without removing it.
   - **Time Complexity:** O(1) - Constant time, as it involves accessing the first element of the list.
   - **Space Complexity:** O(1) - Constant space, as it doesn't modify the size of the list.

These methods collectively allow users to interact with the queue, performing essential operations such as checking its status, adding elements, removing elements, and peeking at the front element.
