''' array is a linear data structure which is used to store multiple items of same type in continours memory location


1. How Arrays Work in Memory
Contiguous Storage: Because all elements are next to each other, the computer can find any element instantly using a simple math 
formula:{Address} = {Base Address} + {Index} X{Size of one element})


MAJOR DISADVATANGES ==>
FIXED SIZE I.E IN C++ OR JAVA THE SIZE OF THE ARRAY HAS TO FIXED BEFORE HAND 
HOMOGENOUS I.E ONLY ONE DATA TYPE CAN BE STORED IN IT


TO SOLVE THIS HOMOGENOUS PROBLEM WE USE THE RFFERENTIAL ARRAY WHICH STORES THE LOCATION OF THE ELEMEMENTS IN A ARRAY RATHER THAN
THEIR ACTUAL VALUE LIKE STRING OR INT DUE TO WHICH THE ADRESS IS ALWAYS IN THE INTEGER FORM SO STORING THE MEMORY LOCATION FOR EACH
ELEMENT

REFFERENTIAL ARRAY ==>
It stores references (memory addresses or pointers) that point to where the actual data is located elsewhere
in the computer's memory.'

How it works (The Analogy)
NORMAL(COMPACT) Array (Standard): Imagine a row of lockers where each locker contains a physical book. To read a book, you just open the locker.

Referential Array: Imagine a row of lockers where each locker contains a small piece of paper with an address written on it 
(e.g., "Go to Room 402"). To read the "book," you must first open the locker, read the address, and then walk to that room.

Python list (Referential) and a NumPy array (Compact).

THE REFFERENTIAL ARRAY IS SLOWER THAN THE NORMAL ONE AND IT STORES EXTRA MEMORRY AS WELL

TO SOLVE THE OTHER PROBLEM I.E THE FIXED MEMORY LOCATION WE USE THE DYNAMIC ARRAY WHICH IS SAME AS THE NORMAL ARRAY IT CAN JUST GROW 
AND SHRINK IN SIZE AT THE RUNTIME

DYNAMIC ARRAY ==>A Dynamic Array is a resizable data structure that behaves like a standard array but can automatically grow or
shrink in size at runtime
PROBLEM WITH NORMAL ARRAY==>A standard (static) array has a fixed size. If you declare an array of size 10 and try to add an 11th item,
the computer will throw an error because the adjacent memory might already be taken by another variable

2. How Dynamic Arrays Solve This (The "Resizing" Mechanism)
A dynamic array uses a clever strategy to pretend it has infinite space:
Initial Capacity: It starts with a small, fixed-size array (e.g., space for 4 items).
Tracking: It keeps track of how many items are currently inside (Length) and how much total space it has (Capacity).
The Trigger: When you try to add an element but Length == Capacity, the array is full.

Resizing:
It allocates a new, larger block of memory (usually double the old size).
It copies all existing elements from the old array to the new one.
It deletes the old, smaller array.
It adds your new element into the now-available space


PYTHON LIST IS ALSO AN EXAMPLE OF THE DYNAMIC AS WELL AS REFFERENTIAL ARRAY
'''
