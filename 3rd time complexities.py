# ============================================================
# SPACE AND TIME COMPLEXITY
# (CampusX DSA for AI — Module 01: foundational analysis tools
#  used to evaluate EVERY algorithm from here on)
# ============================================================

# NOTE: This video doesn't teach a data structure — it teaches
# the LANGUAGE you'll use to talk about every data structure and
# algorithm for the rest of the course. Skipping this makes
# every later "why is this approach better" explanation
# meaningless, since "better" only has meaning in terms of
# time/space complexity.


# ============================================================
# STEP 1: WHY THIS MATTERS BEFORE ANYTHING ELSE
# ============================================================

# Two pieces of code can produce the EXACT same output and still
# be wildly different in quality — one might finish instantly on
# a million rows, the other might take hours. "Correct" isn't
# enough in real systems (or interviews) — you need to reason
# about HOW WELL a solution scales as input size grows. Time and
# space complexity give you a precise, hardware-independent
# vocabulary for that comparison, instead of vague "this feels
# slow" judgments.


# ============================================================
# STEP 2: ANALOGY — MOVING BOXES, NOT STOPWATCHES
# ============================================================

# Imagine judging two movers not by a stopwatch (which depends
# on their mood, the weather, traffic that day) but by asking:
# "as the number of boxes DOUBLES, does their work roughly
# double too? Or does it quadruple? Or stay the same?" That
# growth PATTERN is what complexity analysis measures — not the
# actual seconds/minutes, which depend on machine speed, so
# they're an unreliable and shifting target.


# ============================================================
# STEP 3: TIME COMPLEXITY — MEASURING GROWTH, NOT SECONDS
# ============================================================

# Time complexity asks: as input size n grows, how does the
# NUMBER OF BASIC OPERATIONS grow? Not wall-clock time (that
# varies by CPU, language, load) — operation COUNT, expressed
# using Big-O notation, which captures the DOMINANT growth term
# and ignores constants/lower-order terms because those become
# irrelevant at large n.

# WORKED EXAMPLES:

def print_once(arr):
    # runs ONE operation regardless of arr's size -> O(1)
    print(arr[0])

def print_all(arr):
    # one operation PER element -> grows linearly with n -> O(n)
    for item in arr:
        print(item)

def print_pairs(arr):
    # inner loop runs n times for EACH of the n outer iterations
    # -> n * n operations -> O(n^2)
    for i in arr:
        for j in arr:
            print(i, j)

def binary_search(arr, target):
    # each step HALVES the remaining search space instead of
    # scanning one-by-one -> O(log n)
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# ============================================================
# STEP 4: WHY WE DROP CONSTANTS AND LOWER-ORDER TERMS
# ============================================================

# If an algorithm does exactly "3n + 5" operations, we still
# call it O(n), NOT O(3n + 5). Reasoning: as n grows toward
# infinity, that "+5" becomes negligible, and the "3" is just a
# hardware/implementation-dependent constant — it doesn't change
# the GROWTH SHAPE. Two O(n) algorithms might have very
# different real-world constants (one could be 10x slower than
# another), but they scale the SAME WAY — which is what Big-O is
# built to describe, not raw speed.


# ============================================================
# STEP 5: BEST, AVERAGE, AND WORST CASE
# ============================================================

# The SAME algorithm can have different complexities depending
# on the input it's given:
#   - BEST CASE: the most favorable input (e.g. searching for
#     the FIRST element in a linear search -> O(1))
#   - WORST CASE: the least favorable input (e.g. searching for
#     an element that ISN'T there at all -> O(n)) — this is
#     what Big-O notation conventionally refers to unless stated
#     otherwise, since it's the guaranteed upper bound
#   - AVERAGE CASE: expected performance across typical/random
#     inputs — harder to compute, less commonly asked about, but
#     matters more for real-world tuning

# Interview convention: unless told otherwise, "what's the time
# complexity" means WORST CASE.


# ============================================================
# STEP 6: SPACE COMPLEXITY — MEMORY GROWTH, SAME LOGIC APPLIED
# ============================================================

# Same growth-pattern thinking, but for MEMORY instead of
# operation count. Two components matter:
#   - INPUT SPACE: memory the input itself already occupies
#     (usually excluded from analysis — it's a given, not
#     something your algorithm controls)
#   - AUXILIARY SPACE: EXTRA memory your algorithm allocates
#     beyond the input (new arrays, recursion call stack frames,
#     hash maps, etc.) — this is what "space complexity" usually
#     refers to in interviews

def sum_array(arr):
    # no extra data structure grows with n -> O(1) auxiliary space
    total = 0
    for num in arr:
        total += num
    return total

def duplicate_array(arr):
    # creates a NEW array of the same size as input -> O(n)
    # auxiliary space
    return [x for x in arr]

def factorial(n):
    # RECURSION uses the call stack as memory — n nested calls
    # sit on the stack simultaneously before any of them return
    # -> O(n) auxiliary space, even though there's no explicit
    # array being created
    if n == 0:
        return 1
    return n * factorial(n - 1)

# KEY INSIGHT: recursion's space cost is easy to miss because
# there's no visible data structure — the cost is HIDDEN in the
# call stack, one frame per unreturned call.


# ============================================================
# STEP 7: THE TIME-SPACE TRADE-OFF
# ============================================================

# Very often you can trade one for the other: using EXTRA space
# (e.g. a hash map to store seen values) can bring time
# complexity DOWN (e.g. O(n^2) -> O(n) for a "find duplicates"
# problem), at the cost of extra memory. Recognizing when this
# trade-off is worth making is a recurring theme across nearly
# every DSA topic that follows (especially Hashing, Module 10).


# ============================================================
# CHEAT SHEET
# ============================================================

#  BIG-O          NAME              EXAMPLE
#  ──────────────────────────────────────────────────────────
#  O(1)            Constant          array index access, print_once
#  O(log n)        Logarithmic       binary_search
#  O(n)            Linear            print_all, sum_array
#  O(n log n)      Linearithmic      efficient sorting (merge/quick sort)
#  O(n^2)          Quadratic         print_pairs, nested loops over same array
#  O(2^n)          Exponential       naive recursive Fibonacci
#  O(n!)           Factorial         brute-force permutations

#  GROWTH ORDER (fastest to slowest):
#  O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n) < O(n!)


# ============================================================
# KEY POINTS TO REMEMBER
# ============================================================

# 1.  Complexity measures GROWTH PATTERN as input size increases
#     — not actual runtime in seconds, which depends on hardware
# 2.  Constants and lower-order terms get dropped in Big-O — only
#     the DOMINANT term matters as n grows large
# 3.  "Time complexity" without qualification conventionally
#     means WORST CASE, unless best/average case is specified
# 4.  Space complexity usually refers to AUXILIARY space (extra
#     memory beyond the input), not the input's own size
# 5.  Recursion has a HIDDEN space cost — every unreturned call
#     sits on the call stack, so n recursive calls means O(n)
#     auxiliary space even with no visible data structure
# 6.  Time and space can often be traded against each other —
#     using more memory can reduce time complexity, and this
#     trade-off decision recurs throughout the whole course


# ============================================================
# NEXT TOPIC: likely Arrays (Module 02) — first real data
# structure, applying this complexity vocabulary immediately to
# real operations (access, insert, delete, search)
# ============================================================