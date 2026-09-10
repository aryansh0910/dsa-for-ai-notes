# ============================================================
# LISTS AND THEIR OPERATIONS
# (CampusX DSA for AI — Module 02: Python's actual built-in
#  structure, contrasted against the "pure array" theory from
#  the previous two topics)
# ============================================================

# NOTE: Everything so far (contiguous memory, O(1) access, O(n)
# shifting) was taught using the IDEA of an array. Python doesn't
# actually give you a raw fixed-size array by default — it gives
# you a LIST, which is a more flexible, dynamic version built on
# top of that same array foundation. This topic bridges theory
# to what you actually type in Python every day.


# ============================================================
# STEP 1: WHAT MAKES A PYTHON LIST DIFFERENT FROM A "PURE" ARRAY
# ============================================================

# A true array (like in C) requires every element to be the SAME
# type and a FIXED size decided upfront. A Python list drops both
# restrictions:
#   - can hold MIXED types in the same list
#   - GROWS and SHRINKS automatically (dynamic array under the hood)
#
# Under the hood, Python doesn't store the actual values
# contiguously when types are mixed — it stores contiguous
# POINTERS/references to the objects, wherever those objects
# actually live in memory. This is WHY mixed-type lists are
# possible at all: the contiguous part is the list of addresses,
# not the values themselves.

mixed = [1, "hello", 3.14, [1, 2, 3]]   # perfectly valid — each slot
                                          # just holds a REFERENCE


# ============================================================
# STEP 2: ANALOGY — LOCKERS THAT HOLD ADDRESS SLIPS, NOT ITEMS
# ============================================================

# Recall the locker-row analogy from Arrays. A Python list is
# still a row of numbered lockers, contiguous and instantly
# accessible by index — but instead of each locker holding the
# ACTUAL item, each locker holds a SLIP OF PAPER with the address
# of where the real item is stored elsewhere. That's why a list
# can hold a string, a number, and another list all in a row —
# the lockers are uniform in what they store (an address), even
# though what those addresses POINT TO can differ wildly.


# ============================================================
# STEP 3: 1D LIST OPERATIONS — THE CORE TOOLKIT
# ============================================================

lst = [10, 20, 30, 40, 50]

# ACCESS -- O(1), same reasoning as arrays: direct address math
print(lst[2])            # 30

# APPEND -- O(1) amortized, adds to the end, no shifting
lst.append(60)            # [10, 20, 30, 40, 50, 60]

# INSERT -- O(n) worst case, shifts everything after the index
lst.insert(1, 99)         # [10, 99, 20, 30, 40, 50, 60]

# REMOVE (by VALUE, not index) -- O(n): must SEARCH for the value
# first (O(n)), THEN shift to close the gap (O(n)) -> still O(n)
# overall (constants dropped, as always)
lst.remove(99)             # removes the FIRST occurrence of 99

# POP -- O(1) if popping from the end (default), O(n) if popping
# a specific earlier index (shifting required to close the gap)
lst.pop()                  # removes and returns the LAST element
lst.pop(0)                 # removes index 0 -> O(n), shifts everything left

# SLICING -- O(k), where k is the size of the slice being copied
# (creates a NEW list, doesn't just "view" the original)
sub = lst[1:3]             # copies elements at index 1 and 2 into a new list

# EXTEND -- O(k), appends every element of another iterable
lst.extend([70, 80])        # adds elements one by one, k = len of the addition

# SORT -- O(n log n), uses Timsort internally (hybrid merge+insertion sort)
lst.sort()                  # sorts IN PLACE

# REVERSE -- O(n), must touch every element once
lst.reverse()

# COUNT -- O(n), must check every element to tally occurrences
lst.count(40)

# INDEX (find position of a value) -- O(n), linear search under the hood
lst.index(40)

# KEY INSIGHT: almost every "convenience" method on Python lists
# is really just the SAME array operations from the previous
# topic (shift-to-insert, shift-to-delete, linear-search),
# wrapped in a friendlier name. Knowing the underlying complexity
# stops you from accidentally writing O(n²) code by calling
# .remove() or .pop(0) inside a loop without realizing the cost.


# ============================================================
# STEP 4: 2D LISTS (LIST OF LISTS)
# ============================================================

# A 2D list in Python is literally a list WHERE EACH ELEMENT IS
# ITSELF ANOTHER LIST. Unlike a true 2D array in C (one
# contiguous block, row-major), Python's 2D list is a list of
# POINTERS to separate list objects, which may not sit next to
# each other in memory at all.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])        # O(1) -- access row (O(1)), then access
                             # element in that row (O(1)) -> still O(1)

# TRAVERSING a 2D list needs a NESTED loop -- O(rows * cols)
for row in matrix:
    for val in row:
        print(val, end=" ")

# COMMON PITFALL -- creating a 2D list with * duplicates
# REFERENCES to the SAME inner list, not independent copies:
wrong = [[0] * 3] * 3        # DANGER: all 3 rows point to the SAME list object
wrong[0][0] = 99
print(wrong)                  # [[99, 0, 0], [99, 0, 0], [99, 0, 0]] -- BUG!

# CORRECT way -- list comprehension creates a genuinely NEW list
# for each row:
right = [[0] * 3 for _ in range(3)]
right[0][0] = 99
print(right)                  # [[99, 0, 0], [0, 0, 0], [0, 0, 0]] -- correct

# KEY INSIGHT: this bug exists BECAUSE of Step 1's "lockers hold
# address slips" model — [[0]*3] * 3 creates ONE inner list, then
# copies its ADDRESS three times, not three separate lists.


# ============================================================
# STEP 5: LIST COMPREHENSIONS -- SAME COMPLEXITY, CLEANER SYNTAX
# ============================================================

# A list comprehension is NOT a magic speedup -- it's the SAME
# O(n) loop under the hood, just written more compactly and
# (slightly) faster in practice due to internal optimizations.

squares = [x**2 for x in range(10)]         # O(n)
evens = [x for x in range(20) if x % 2 == 0] # still O(n), filtering
                                              # doesn't change growth rate


# ============================================================
# STEP 6: ARRAYS vs LISTS -- THE FORMAL COMPARISON
# ============================================================

# ARRAYS (conceptual/C-style):
#   - fixed size, single type, TRUE contiguous memory for values
#   - faster in practice due to no reference indirection, no
#     per-element type-checking overhead
#
# PYTHON LISTS:
#   - dynamic size, mixed types, contiguous memory of REFERENCES
#     (not values)
#   - more flexible, but each access involves one extra hop
#     (locker -> address slip -> actual object)
#   - use `array` module or NumPy arrays if you need TRUE
#     fixed-type contiguous storage for performance
#     (this is WHY NumPy exists and matters heavily for AI/ML --
#     it restores true contiguous same-type storage for speed)


# ============================================================
# CHEAT SHEET
# ============================================================

#  OPERATION                     TIME COMPLEXITY    NOTES
#  ────────────────────────────────────────────────────────────
#  Access by index                 O(1)               direct address math
#  append()                        O(1) amortized      end operation
#  insert(i, val)                  O(n)               shifting required
#  pop() [from end]                O(1)               no shifting
#  pop(i) [specific index]         O(n)               shifting to close gap
#  remove(val)                     O(n)               search + shift
#  index(val)                      O(n)               linear search
#  count(val)                      O(n)               must check every element
#  slicing [a:b]                   O(k)               k = size of slice, creates new list
#  extend()                        O(k)               k = size of added iterable
#  sort()                          O(n log n)         Timsort
#  reverse()                       O(n)               touches every element
#  2D access matrix[i][j]          O(1)               two O(1) hops
#  2D traversal                    O(rows * cols)     nested loop


# ============================================================
# KEY POINTS TO REMEMBER
# ============================================================

# 1.  Python lists are dynamic arrays of REFERENCES, not raw
#     values -- this is why mixed types are allowed, and it adds
#     one layer of indirection compared to a true array
# 2.  Most list "convenience methods" are just the SAME shift-
#     based insert/delete/search operations from Arrays, wrapped
#     in friendlier syntax -- their complexity doesn't change
# 3.  `[[0]*n] * n` creates n references to ONE shared inner
#     list -- always use a list comprehension for genuinely
#     independent 2D rows
# 4.  List comprehensions have the SAME complexity as an
#     equivalent loop -- they're syntactic sugar, not an
#     algorithmic speedup
# 5.  2D list access is O(1) (two chained O(1) lookups), but
#     traversal is O(rows * cols) -- don't confuse the two
# 6.  For true fixed-type, memory-efficient contiguous storage
#     (the kind AI/ML workloads actually need for performance),
#     NumPy arrays exist specifically to restore what plain
#     Python lists give up for flexibility


# ============================================================
# NEXT TOPIC: likely Complexity Analysis (applied specifically
# to list operations, per the course outline) or Arrays vs
# Lists as its own dedicated comparison topic, followed by
# classic list-based practice problems (largest element, remove
# duplicates, reverse a list)
# ============================================================