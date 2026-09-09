'''ORDER OF GROWTH ===>
1. CONSTANT
def check_first_element(my_list):
    # This takes the same amount of time whether the list 
    # has 10 items or 10 million items.
    if my_list[0] == 0:        # 1 operation
        return True            # 1 operation
    return False               # 1 operation
    
EXPLANATION => HERE THERE ARE THREE OPERATIONS SO O(1+1+1) SO O(3) MEANS IT'S A CONSTANT GROWTH.MEANS EVEN IF THE SIZE OF MY_LIST
BECOMES 100 OR 1000 THE TYM COMPLEXITY REMAINS SAME

2.LOGRATHMIC TIME log n
Structure: A loop where the input size is divided or cut in half during every iteration.
def binary_search_logic(n):
    steps = 0
    while n > 1:
        n = n // 2   # <--- The "Divide by 2" makes it Logarithmic
        steps += 1
    return steps
EXPLANATION => EVERY TYM THE N GETS DIVIDED BY TWO SO THAT IT MAKES A LOGRATHMIC GRAPH.MEANS IF THE N INCREASES 2 TIMES THE TYM WILL
BE INCREASES BY ONE AND IF THE N INCREASES BY 4 THE TYM COMPLEXITY INC BY 2 I.E IN A LOGRATHMIC WAY

3.LINER TIME n
Structure: A single for-loop that visits every element once
def linear_search(my_list):
    for item in my_list:       # Runs 'n' times
        if item == "Target":   # 1 operation
            return True
    return False
    
4.LINEARTHMIC TIME n log n
Structure: Usually seen in efficient sorting or when you have a linear loop that calls a logarithmic function inside it.
def sort_example(my_list):
    # Most modern sorting algorithms (like Python's .sort()) 
    # use this order of growth.
    my_list.sort() 
    return my_list
explanation => the n inc accordingly with the given formula
5. QUADRATIC N^2
Structure: Nested for-loops (a loop inside a loop) where both loops iterate over the input n
def print_all_pairs(my_list):
    for x in my_list:          # Outer loop (n times)
        for y in my_list:      # Inner loop (n times)
            print(x, y)        # Happens n * n times
EXPLANATION ==> means if u inc the n by two times the time complexity will be increased by 4 tym i.e the sqaure of it
'''
