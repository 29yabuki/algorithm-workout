# <p align="center">Daily Routine</p>
This is a collection of algorithms that I code daily for two reasons:
1. To remember the fundamental coding concepts even if I were to go on a slump
2. To embed rudimentary algorithms used in the studies of data structures and algorithm

## Features
A working version of the following algorithms:

**A.** Search Algorithms
- Sequential Search
- Ordered Search
- Binary Search
</br>
**B.** Sorting Algorithms
- Bubble Sort
- Short Bubble Sort
- Selection Sort
- Insertion Sort
- Shell Sort
- Gap Insertion Sort
- Merge Sort
-  Quick Sort
</br>
**C.** Singly Linked List
A **singly linked list** is a type of linked list that is unidirectional, that is, it can be traversed in only one direction from head to the last node (tail).

The whole linked list file contains the following classes and functions:
- Node class
	- A **Node** in a linked list holds the data value and the pointer which points to the location of the next node in the linked list. As the node is a combination of multiple information, hence we will be defining a class for Node which will have a variable to store data and another variable to store the pointer.
- PythonicNode class
	- It has the same function as the Node class but done in a pythonic fashion by integrating @property, getter, and setter decorators.
- is_empty
	- It tests whether the list is empty or not.
- add
	- It adds a new item to the list.
	- It needs the item and returns nothing. Assume the item is not already in the list
- append
	- Adds a new item to the end of the list making it the last item in the collection. 
	- It needs the item and returns nothing. Assume the item is not already in the list
- insert
	- Adds a new item to the list at position pos.
	- It needs the item and returns nothing. 
	- Assume the item is not already in the list and there are enough existing items to have position pos.
- size
	- Returns the number of items in the list. 
	- It needs no parameters and returns an integer.
- search
	- Searches for the item in the list.
	- It needs the item and returns a boolean value.
- index 
	- Returns the position of item in the list. 
	- It needs the item and returns the index. Assume the item is in the list.
- remove
	- removes the item from the list. 
- pop
	- removes and returns the item at position pos. 
	- It needs the position and returns the item. Assume the item is in the list.
	- has a default pos value of -1 (to remove the item in the last position)
- \_\_repr\_\_
	-  prints a representation of the linked list in a list format
 
## Sources
A word of thanks to the following sources by establishing themselves as both direct and indirect references for my daily coding routine. Your work will never go unnoticed and is making an impact for aspiring developers such as myself.

https://runestone.academy/runestone/books/published/pythonds/index.html
https://codeburst.io/algorithms-i-searching-and-sorting-algorithms-56497dbaef20 
https://www.geeksforgeeks.org/data-structures/linked-list/ 
https://www.studytonight.com/data-structures/linear-linked-list 

## Contributions
If there are any comment or recommendations, always feel free to implement anything, submit pull requests, create issues, and discuss ideas with me.