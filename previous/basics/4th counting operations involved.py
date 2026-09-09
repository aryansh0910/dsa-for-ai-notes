'''
operations is defined as the things done in your code like assigning variables i.e x=10 performing calculations like 10*3 one 
operation involved 
EXAMPLE CODE

def sum_list(data):
    total = 0               # 1 operation (Assignment)
    for x in data:          # Runs 'n' times (where n is length of list)
        total = total + x   # 2 operations (Addition + Assignment)
    return total            # 1 operation (Return)

Summary Rule of Thumb:Sequential steps? Add them: O(a + b).Nested steps? Multiply them: 
O(a times b).Split the data in half? It’s likely Logarithmic: $O(\log n)$
'''
''' there are 3 cases known in a operations/program ==> best case,worst case,average case
Example: Searching for a name in a list of 1,000 people.
Best Case: The name is the very first one O(1)
Worst Case: The name is at the very end or not there at all O(n)


mostly a program focuses on the worst case so that even in the worst situtaions our program doesnt fail
'''