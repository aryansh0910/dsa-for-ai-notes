# ============================================================
# ARRAY OPERATIONS
# (CampusX DSA for AI — Module 02: the practical toolkit built
#  on top of the array fundamentals from the previous topic —
#  traversal, insertion, deletion, and searching, formalized)
# ============================================================

# NOTE: The previous topic explained WHY arrays behave the way
# they do (contiguous memory -> fast access, slow shifting).
# This topic turns that theory into the actual reusable
# OPERATIONS you'll call on arrays constantly — think of it as
# moving from "understanding the locker hallway" to "here's your
# toolkit for actually using it."


# ============================================================
# STEP 1: TRAVERSAL — VISITING EVERY ELEMENT
# ============================================================

# The simplest operation: visit each element exactly once. Since
# array access is O(1) per element, visiting all n elements is
# O(n) overall — you can't do better than this, since you must
# at minimum LOOK at every element to guarantee you've seen all
# of them.

def traverse(arr):
    for i in range(len(arr)):
        print(arr[i])   # O(1) per access -> O(n) total

# KEY INSIGHT: traversal is the BASELINE every other array
# operation gets compared against. Anything faster than O(n)
# means you're skipping elements (like binary search exploiting
# sortedness); anything slower means you're doing EXTRA work per
# element (like nested loops).


# ============================================================
# STEP 2: INSERTION — THREE DISTINCT CASES, THREE DIFFERENT COSTS
# ============================================================

# Insertion isn't ONE operation with ONE complexity — WHERE you
# insert changes everything, because it changes how much
# shifting is needed (recall: no gaps allowed in contiguous
# memory).

# CASE A: Insert at the END
def insert_at_end(arr, value):
    arr.append(value)     # O(1) amortized — nothing to shift
    return arr

# CASE B: Insert at the BEGINNING
def insert_at_beginning(arr, value):
    arr.append(None)                          # make room
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]                    # shift EVERY element right
    arr[0] = value
    return arr                                 # O(n) — worst possible case,
                                                # since ALL elements shift

# CASE C: Insert at an ARBITRARY middle index
def insert_at_index(arr, index, value):
    arr.append(None)
    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i - 1]
    arr[index] = value
    return arr                                 # O(n) worst case, O(1) best
                                                # case (if index is near the end)

# KEY INSIGHT: "insertion is O(n)" is a WORST-CASE statement
# specifically about inserting near the FRONT. Insertion near
# the END is essentially free. This is exactly the best/worst
# case distinction from Module 01, now applied concretely.


# ============================================================
# STEP 3: DELETION — MIRRORS INSERTION, SAME LOGIC IN REVERSE
# ============================================================

# CASE A: Delete from the END
def delete_from_end(arr):
    arr.pop()          # O(1) — nothing needs to shift
    return arr

# CASE B: Delete from the BEGINNING or MIDDLE
def delete_at_index(arr, index):
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]    # shift everything AFTER index one step left
    arr.pop()                   # remove the now-duplicate last element
    return arr                  # O(n) worst case — shifting to CLOSE the gap

# KEY INSIGHT: insertion shifts elements RIGHT to make a gap;
# deletion shifts elements LEFT to close one. Same mechanism,
# opposite direction, same O(n) worst-case reasoning.


# ============================================================
# STEP 4: SEARCHING — REVISITED WITH OPERATION FRAMING
# ============================================================

# LINEAR SEARCH — works on any array, no assumptions required:
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i        # found -> return index
    return -1                # not found -> checked everything, O(n) worst case

# BINARY SEARCH — requires a SORTED array, trades that
# requirement for massive speed:
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1     # target must be in the right half
        else:
            high = mid - 1    # target must be in the left half
    return -1                  # O(log n)

# KEY INSIGHT: this is the "operation" version of a big theme —
# an operation's complexity isn't fixed to the DATA STRUCTURE
# alone, it depends on what PROPERTY (like sortedness) you can
# exploit about the specific data inside it.


# ============================================================
# STEP 5: UPDATE (a.k.a. "SET") — THE OPERATION EVERYONE FORGETS
# ============================================================

# Updating an existing element at a known index is just a direct
# write to a calculated address — same O(1) reasoning as access,
# since no shifting is involved (you're not changing array size).

def update_at(arr, index, value):
    arr[index] = value    # O(1) — direct address write
    return arr

# KEY INSIGHT: update is O(1) precisely BECAUSE it doesn't change
# the array's length — the moment size changes (insert/delete),
# shifting becomes necessary and complexity jumps to O(n).


# ============================================================
# STEP 6: PUTTING IT TOGETHER — A DECISION LENS
# ============================================================

# When choosing HOW to modify an array, the real question isn't
# "is this array good or bad" — it's "does my use case mostly
# need END operations (cheap) or FRONT/MIDDLE operations
# (expensive)?" This is the first concrete motivation for why
# later data structures (linked lists, deques) exist: they trade
# array's O(1) access for O(1) front insertion, because some
# problems need that trade-off instead.


# ============================================================
# CHEAT SHEET
# ============================================================

#  OPERATION                        BEST CASE   WORST CASE   WHY
#  ────────────────────────────────────────────────────────────────
#  Traversal                         O(n)        O(n)         must visit each element
#  Access by index                   O(1)        O(1)         direct address math
#  Update at known index              O(1)        O(1)         no shifting needed
#  Insert at end                     O(1)*       O(1)*        *amortized, occasional resize
#  Insert at beginning/middle        O(1)        O(n)          shifting to make a gap
#  Delete from end                    O(1)        O(1)         no shifting needed
#  Delete from beginning/middle      O(1)        O(n)          shifting to close the gap
#  Linear search                      O(1)        O(n)         no shortcut on unsorted data
#  Binary search (sorted only)       O(1)        O(log n)      halves search space each step


# ============================================================
# KEY POINTS TO REMEMBER
# ============================================================

# 1.  Traversal is the O(n) BASELINE — nothing meaningful can
#     visit fewer elements and still guarantee correctness
# 2.  Insertion/deletion complexity depends ENTIRELY on WHERE —
#     end operations are cheap (O(1)), front/middle are
#     expensive (O(n)) due to shifting
# 3.  Update (overwriting an existing index) is O(1) because
#     array LENGTH doesn't change — no shifting triggered
# 4.  Search complexity depends on whether you can exploit
#     sortedness (O(log n)) or not (O(n)) — same data structure,
#     different guarantees based on data properties
# 5.  "Best case" and "worst case" aren't abstract — for arrays
#     they map directly onto POSITION (near the end = cheap,
#     near the start = expensive)
# 6.  This full toolkit (traverse, insert, delete, search,
#     update) is the same five-operation lens you'll apply to
#     EVERY future data structure — the comparisons only make
#     sense once you know arrays' baseline numbers


# ============================================================
# NEXT TOPIC: likely Array-based problems/patterns (rotation,
# reversal, two-pointer technique) or a transition to Linked
# Lists — where insertion at the front finally becomes O(1),
# directly solving arrays' weakest point at the cost of O(n)
# access
# ============================================================