'''
The Order of Growth describes how the complexity of an algorithm increases as the size of the input (n) increases. 
It allows us to ignore the tiny details (like whether a loop has 2 or 3 instructions) and focus on the big picture 

THIS IS KNOWN AS THE BIG O notation i.e O()

to find the order of growth we have to do like drop the constants from the equation of the operations like 
5n+1 i.e 5 operations are in a loop and will execute N times means the no. of times the loop runs and 1 operations is ourside the 
loop so plus 1 for it


so while the the order complexity we always remove the constants like 5 and 1 and only care about the N in the relation
ANSWER ==>  so the result for it is O(n)


in case of nested loops like n^2 + 5n + 2 we only worry about the n with the highest complexity i.e n^2
ANSWER ==>  so the result for it is O(n^2)


log(n)+n
ANSWER O(n) as the n grows much faster than the log(n)

3^n + n^3
ANSWER O(3^n) as we always take n very high so it 3^N is very much bigger then N^3

HEIRCHAY

1 < \log n < n < n \log n < n^2 < n^3 < 2^n < n!


MEANS THE CODE'S TIME INC AS WE INC THE INPUT SIZE I.E THE N WITH THE INC IN ORDER SO WE GENERALLLY PREFER THE THINGS WITH LESS
ORDER LIKE THE CONSTANT AND THE LOG N'''
