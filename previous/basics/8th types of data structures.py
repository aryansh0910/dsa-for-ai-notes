''' there are two types of data structures : 1. linear and 2. non linear
A. Linear Data Structures
Data is arranged in a sequential manner. Each element (except the first and last) has a unique "before" and "after" neighbor.

Arrays: A collection of elements stored in contiguous memory. In ML, these are the foundation for Vectors and Matrices.

Linked Lists: Elements (nodes) are not stored together; each node "points" to the next one. Great for dynamic memory.

Stacks (LIFO): "Last In, First Out." Like a stack of plates. Used in backtracking algorithms.

Queues (FIFO): "First In, First Out." Like a line at a store. Used for task scheduling and data pipelines.



B. Non-Linear Data StructuresData is not in a sequence. Instead, it is arranged hierarchically or as a network.

Trees: A hierarchical structure with a "root" node and "children."24AI 
Use Case: Decision Trees and Random Forests use this structure to make predictions.

Graphs: A collection of nodes (vertices) connected by edges.
AI Use Case: Social Networks, Google Maps, and Neural Networks (which are essentially computation graphs).

Hash Tables (Dictionaries): Maps "keys" to "values."28 It provides near-instant (29$O(1)$) search time.30AI 
Use Case: Storing labels, metadata, or feature lookup'''