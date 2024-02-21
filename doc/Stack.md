# Stack Data Structure

## Introduction:

A stack is a fundamental linear data structure that follows the Last-In, First-Out (LIFO) principle. In a stack, elements are added and removed from the same end, known as the top of the stack. This means that the last element added is the first one to be removed.

## Real-Life Example:

Think of a stack of plates in a cafeteria. New plates are added to the top, and when someone takes a plate, they take it from the top. This behavior mimics the characteristics of a stack data structure.

## Usefulness of Stacks:

Stacks are useful in various scenarios, including:

- **Function Call Management:** Stacks are used in programming languages to manage function calls and local variables.

- **Undo Mechanism:** Many applications use stacks to implement an undo feature.

- **Expression Evaluation:** In compiler design, stacks are used to evaluate expressions.

- **Backtracking Algorithms:** Stacks are employed in backtracking algorithms to store and manage the state.

## Stack Representation:

A stack can be visualized as a collection of elements with a single point of access, known as the top.

Top
-----------------
| Element 1     |
| Element 2     |
| Element 3     |
| ...           |
| Element N     |
-----------------

In this representation:

- `Top` indicates the position where elements are added and removed.
- Elements are added to and removed from the top, following the Last-In, First-Out (LIFO) principle.

## Function/Method Descriptions:

Check the implementation in [src/Stack.py](../src/Stack.py) for the details of the Stack class.

1. **`__init__` (Initialization):**
   - **Role:** Initializes a new instance of the `Stack` class with an empty list.
   - **Time Complexity:** O(1) - Constant time, as it involves creating an empty list.
   - **Space Complexity:** O(1) - Constant space, as it initializes an empty list.

2. **`is_empty`:**
   - **Role:** Checks whether the stack is empty.
   - **Time Complexity:** O(1) - Constant time, as it involves checking the length of the list.
   - **Space Complexity:** O(1) - Constant space, as it only performs a comparison.

3. **`add`:**
   - **Role:** Adds an element to the top of the stack.
   - **Time Complexity:** O(1) - Constant time, as it involves appending an element to the end of the list.
   - **Space Complexity:** O(1) - Constant space, as it increases the size of the list by one.

4. **`remove`:**
   - **Role:** Removes and returns the element from the top of the stack.
   - **Time Complexity:** O(1) - Constant time, as it involves removing the last element from the list using `pop()`.
   - **Space Complexity:** O(1) - Constant space, as it decreases the size of the list by one.

5. **`size`:**
   - **Role:** Returns the number of elements in the stack.
   - **Time Complexity:** O(1) - Constant time, as it involves checking the length of the list.
   - **Space Complexity:** O(1) - Constant space, as it only performs a comparison.

6. **`peek`:**
   - **Role:** Retrieves the element at the top of the stack without removing it.
   - **Time Complexity:** O(1) - Constant time, as it involves accessing the last element of the list.
   - **Space Complexity:** O(1) - Constant space, as it doesn't modify the size of the list.

These methods collectively enable users to interact with the stack, performing essential operations such as checking its status, adding elements, removing elements, and peeking at the top element.
