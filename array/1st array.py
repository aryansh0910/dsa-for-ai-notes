# ============================================================
# ARRAYS
# (CampusX DSA for AI — Module 02: the first real data structure,
#  applying the time/space complexity vocabulary from Module 01
#  directly to real operations)
# ============================================================

# NOTE: Arrays are the foundation almost every other data
# structure (stacks, queues, hash tables, even trees/graphs
# under the hood) is built on top of. Understanding WHY arrays
# behave the way they do (fast access, slow insertion) is what
# makes every later "why use a linked list instead" or "why use
# a hash map instead" explanation make sense.


# ============================================================
# STEP 1: WHAT AN ARRAY ACTUALLY IS, PHYSICALLY
# ============================================================

# An array is a collection of elements stored in CONTIGUOUS
# memory locations — meaning each element sits right next to the
# previous one in memory, back to back, with no gaps. This
# physical fact is the SINGLE reason arrays behave the way they
# do — every property (fast access, slow insertion) traces back
# to "contiguous memory," not to some arbitrary rule.


# ============================================================
# STEP 2: ANALOGY — A ROW OF NUMBERED LOCKERS
# ============================================================

# Think of an array as a row of lockers in a hallway, all the
# same size, numbered 0, 1, 2, 3... If you know locker number 7's
# exact position, you can walk STRAIGHT to it — you don't need to
# check lockers 0 through 6 first. That's why array access is
# instant (O(1)): the "locker number" (index) plus knowing where
# locker 0 starts lets you calculate any locker's exact location
# directly, with simple math, not searching.

# But if you want to ADD a new locker in the middle of the row,
# every locker after it has to physically shift down to make
# room — there's no "gap" to slide into. That's why insertion in
# the middle is slow (O(n)): the shifting, not the insertion
# itself, is the expensive part.


# ============================================================
# STEP 3: WHY ACCESS IS O(1) — THE MATH BEHIND IT
# ============================================================

# Because memory is contiguous, the computer can calculate any
# element's memory address directly:
#
#     address of arr[i] = base_address + (i * size_of_each_element)
#
# This is a single arithmetic calculation — no searching, no
# stepping through elements one by one. Whether you're accessing
# index 0 or index 999,999, it takes the SAME amount of work.
# That's the definition of O(1): constant time, regardless of n.

arr = [10, 20, 30, 40, 50]
print(arr[3])   # O(1) — direct address calculation, not a search


# ============================================================
# STEP 4: WHY INSERTION/DELETION IN THE MIDDLE IS O(n)
# ============================================================

# Since there are no gaps between elements, inserting a new
# value at position i means every element from i onward has to
# shift one slot to the right FIRST, to physically make room.
# In the worst case (inserting at index 0), ALL n elements shift
# -> O(n).

def insert_at(arr, index, value):
    arr.append(None)                     # make room for one more slot
    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i - 1]               # shift each element right
    arr[index] = value
    return arr

print(insert_at([10, 20, 30, 40], 1, 99))  # [10, 99, 20, 30, 40]

# Deletion works the same way in reverse — everything after the
# deleted index shifts LEFT to close the gap, also O(n) worst case.

def delete_at(arr, index):
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]                # shift each element left
    arr.pop()                              # remove the now-duplicate last slot
    return arr

print(delete_at([10, 20, 30, 40], 1))      # [10, 30, 40]

# KEY INSIGHT: insertion/deletion at the END is different — no
# shifting needed, since nothing comes after it -> O(1)
# (this is exactly why arr.append() is fast, but arr.insert(0, x)
# is slow).


# ============================================================
# STEP 5: FIXED-SIZE vs DYNAMIC ARRAYS
# ============================================================

# STATIC arrays (like in C/Java by default) have a FIXED size
# decided at creation — you can't grow them, you'd have to create
# a brand new, bigger array and copy everything over.
#
# DYNAMIC arrays (Python lists, Java ArrayList, C++ vector) look
# like they grow freely, but under the hood they do EXACTLY that
# copy-and-resize operation automatically whenever they run out
# of room — usually by DOUBLING their capacity, so this resize
# doesn't happen on every single append, just occasionally.

# This is why appending is described as O(1) AMORTIZED, not
# strictly O(1) every single time: most appends are truly O(1)
# (there's spare room), but occasionally one append triggers an
# O(n) resize+copy. Averaged ("amortized") across many appends,
# the cost per append still works out to O(1).

arr = []
for i in range(5):
    arr.append(i)   # O(1) amortized — occasional resize happens invisibly


# ============================================================
# STEP 6: SEARCHING IN AN ARRAY
# ============================================================

# UNSORTED array: no shortcut exists — you must check elements
# one by one in the worst case -> O(n) linear search.

def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

# SORTED array: you can eliminate half the remaining elements
# each step instead of checking one by one -> O(log n) binary
# search (covered in Module 01, reused here since arrays are
# where it's actually implemented).

# KEY INSIGHT: this is a preview of a recurring theme — the SAME
# data structure can have wildly different performance depending
# on whether extra structure (sortedness) is imposed on it.


# ============================================================
# STEP 7: MULTI-DIMENSIONAL ARRAYS (BRIEF PREVIEW)
# ============================================================

# A 2D array is just an array of arrays — still contiguous
# memory in most languages (row-major order: entire row 0 stored
# first, then row 1, etc.), which is why accessing arr[i][j] is
# still effectively O(1) — same direct address math, just with
# two offsets instead of one.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])   # O(1) -> 6


# ============================================================
# CHEAT SHEET
# ============================================================

#  OPERATION                    TIME COMPLEXITY     WHY
#  ──────────────────────────────────────────────────────────
#  Access by index               O(1)                direct address math
#  Search (unsorted)             O(n)                 no shortcut, check each
#  Search (sorted, binary)       O(log n)             halves search space
#  Insert/delete at END          O(1) amortized        no shifting needed
#  Insert/delete at START/MID    O(n)                 shifting required
#  Append (dynamic array)        O(1) amortized        occasional resize+copy

#  SPACE COMPLEXITY: O(n) — proportional to number of elements
#  stored, contiguous block


# ============================================================
# KEY POINTS TO REMEMBER
# ============================================================

# 1.  Arrays store elements in CONTIGUOUS memory — this single
#     physical fact explains every property below
# 2.  Access is O(1) because the address of any index can be
#     CALCULATED directly, not searched for
# 3.  Insertion/deletion in the middle or start is O(n) because
#     of the shifting needed to preserve contiguity — no gaps
#     allowed
# 4.  Insertion/deletion at the END is O(1) (amortized for
#     dynamic arrays) — nothing needs to shift
# 5.  Dynamic arrays (Python lists) simulate "growing" by
#     resizing (usually doubling) and copying — this makes
#     append O(1) AMORTIZED, not strictly O(1) every time
# 6.  Searching is O(n) unsorted, O(log n) sorted — sortedness
#     is "extra structure" that unlocks a faster algorithm
# 7.  2D arrays are still contiguous under the hood (row-major
#     order), so element access stays O(1)


# ============================================================
# NEXT TOPIC: likely Array operations in depth / rotations /
# subarray problems, or moving on to Linked Lists — the natural
# contrast structure where insertion is O(1) but access becomes
# O(n), i.e. arrays' strengths and weaknesses flip
# ============================================================