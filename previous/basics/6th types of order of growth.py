'''
1. Constant: O(1) The time taken is independent of the input size. The graph is a perfectly flat line
Time |
     |----------------- (Flat)
     +-----------------
           Input (n)

EXAMPLE ==> INDEXING OF THE ARRRAY LIKE LIST[100] IT DOESNT MATTER IF THE ARRAY OR LIST IS 200 ELEMENTS OR 1000 ELEMENTS IT WIIL 
AWAYS TAKE THE SAME AMOUNT OF TIME EVERY TIME
2. Logarithmic: $O(\log n)$The time increases very slowly. As you double the input, the time only increases by a tiny amount.
Time |         _______ (Leveling off)
     |      /
     |    /
     +-----------------
           Input (n)
EXAMPLE ==> BINARY SEACH IS THE EXAMPLE OF IT
3. Linear: $O(n)$The time increases at the exact same rate as the input. A 45-degree straight line
Time |            /
     |         /
     |      /
     +-----------------
           Input (n)
EXAMPLE ==> LINEAR SEACHING  IN A ARRRAY FOR AN ELEMENT IF THE ARRAY IS 100 ELEMETNS IT WILL TAKE LESS TIME AND IF THE ARRAY IS 1000 
ELEMENTS IT WILL TAKE MORE TIME
4. Linearithmic: O(nlog n) Slightly steeper than a straight line. This is typical for efficient sorting          
Time |             /
     |           /
     |        / 
     |     /   (Slightly curved)
     +-----------------
           Input (n)
EXAMPLE MERGE SORT QUCIK SORT
5. Quadratic: $O(n^2)$The time increases exponentially relative to the input. If $n=10$, steps=100. If $n=100$, steps=10,000
Time |      |
     |      |  (Steep Curve)
     |     /
     |____/
     +-----------------
           Input (n)
EXAMPLE ==> FOR LOOPS ARE THE EXAMPLE OF IT
'''