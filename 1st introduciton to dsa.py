# ============================================================
# DSA FOR AI — COURSE INTRODUCTION
# (CampusX: orientation lecture — no code, sets up the roadmap
#  for everything that follows)
# ============================================================

# NOTE: This video doesn't teach a DSA concept itself — its job
# is to answer three questions before you commit 57+ hours:
# WHY does DSA matter for an AI/ML career, WHAT does the course
# actually cover, and HOW is it structured so you can navigate it.


# ============================================================
# STEP 1: WHY DSA — EVEN FOR AN AI/ML TRACK
# ============================================================

# Your instinct might be "I'm going into ML, not SDE — why do I
# need DSA?" The course's answer: DSA isn't competing with your
# ML skills, it's the GATE in front of them. Most product-based
# companies (and plenty of AI-specific roles) still run DSA
# rounds before anyone even looks at your model portfolio or
# Kaggle rank. Skip DSA prep and you can be the strongest ML
# candidate in the pool and still get filtered out in round 1.

# Beyond interviews, DSA also directly feeds INTO ML work:
#   - efficient data preprocessing at scale needs the same
#     complexity thinking as any DSA problem
#   - understanding WHY certain ML algorithms are fast/slow
#     (e.g. tree-based models, nearest-neighbor search) requires
#     the same underlying structures (trees, graphs, hashing)
#   - competitive programming instincts (pattern recognition,
#     breaking a problem into known sub-patterns) transfer
#     directly into "how do I approach this ML system design
#     question"


# ============================================================
# STEP 2: ANALOGY — DSA AS THE ENGINE, ML AS THE DRIVING
# ============================================================

# Think of ML/AI skills as knowing HOW to drive well — reading
# the road, picking the right line. DSA is the ENGINE under the
# hood. You can be a great driver, but if the engine can't
# handle the load, you're not finishing the race. Companies test
# the engine first (DSA rounds) because a broken engine makes
# driving skill irrelevant — you never even get to show it.


# ============================================================
# STEP 3: WHAT THE COURSE COVERS — THE ROADMAP
# ============================================================

# The course is NOT a flat numbered video list — it's organized
# into 13 modules, structured so each one builds on the last:
#   01. Intro to DSA & Python Basics (complexity analysis, Big-O)
#   02. Arrays & Lists
#   03. Strings
#   04. Linked Lists
#   05. Stacks
#   06. Queues
#   07. Searching
#   08. Sorting
#   09. Recursion
#   10. Hashing
#   11. Patterns & Problem Solving (sliding window, two pointers,
#       prefix sums, fast/slow pointer, binary search pattern,
#       greedy basics — these are PATTERNS that get reused across
#       many problems, not a new data structure)
#   12. Trees
#   13. Graphs

# Design principle: linear data structures first (arrays through
# hashing), THEN the reusable problem-solving patterns, THEN the
# non-linear structures (trees, graphs) that need those patterns
# as prerequisites. Nothing later in the course depends on
# something taught after it.


# ============================================================
# STEP 4: HOW TO USE THE COURSE — THE INTENDED WORKFLOW
# ============================================================

# Beginner-friendly but INTERVIEW-ORIENTED — meaning every
# module pairs concept + clean Python implementation + a curated
# problem set, rather than just theory. The stated goal by the
# end: break down a new problem, pick the right approach, and
# write clean, efficient, interview-ready code — while also
# having the CS foundation that later ML/system-design topics
# assume you already have.


# ============================================================
# CHEAT SHEET
# ============================================================

#  MODULE #    TOPIC                          BUILDS TOWARD
#  ──────────────────────────────────────────────────────────
#  01           Python + Big-O basics          everything below
#  02-04        Arrays, Strings, Linked Lists  core linear structures
#  05-06        Stacks, Queues                 more linear structures
#  07-08        Searching, Sorting             algorithmic thinking
#  09           Recursion                      needed for trees/graphs
#  10           Hashing                        optimized lookups
#  11           Patterns                       reusable across all of the above
#  12-13        Trees, Graphs                  non-linear structures, hardest tier


# ============================================================
# KEY POINTS TO REMEMBER
# ============================================================

# 1.  DSA isn't a detour from your AI/ML goal — it's the
#     screening gate most AI/ML hiring pipelines still put in
#     front of the ML-specific evaluation
# 2.  The course is module-based (13 modules), not a flat video
#     list — order matters, each module assumes the ones before
#     it are done
# 3.  Linear structures -> patterns -> non-linear structures is
#     the deliberate sequencing, not arbitrary
# 4.  Every module pairs concept + Python implementation +
#     curated problems — theory alone isn't the point, writing
#     clean interview-ready code is
# 5.  Module 11 (Patterns) is the hinge point — it's where
#     isolated data-structure knowledge turns into a reusable
#     problem-solving toolkit you'll keep applying in 12-13 and
#     beyond


# ============================================================
# NEXT TOPIC: Module 01 — Introduction to DSA & Python Basics
# (complexity analysis / Big-O, most likely first real content)
# ============================================================