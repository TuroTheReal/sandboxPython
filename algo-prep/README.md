# algo-prep

Algorithm training for SWE interviews (all kinds of roles, not only DevOps).
Goal: solid, durable foundations, ready to polish when an interview comes.

Working model: **LeetCode to solve, this repo + Claude to understand and
review.**

    LeetCode      = the gym. You solve, the judge validates (edge cases, timing).
    repo + Claude = the coach. We explain the pattern before, review your solution
                    after, and log it for spaced repetition.

So this repo does NOT contain solutions to run locally (the LeetCode judge
does it better). It contains course notes, problem lists and progress tracking.

## What's inside

- `CHEATSHEET.md`             Big-O + Python toolkit, your quick reference
- `PYTHON.md`                 common Python methods and idioms
- `RECOGNITION.md`            which pattern for which problem
- `PROBLEMS.md`               LeetCode problem pools per pattern (easy/medium/hard) + CodinGame
- `PROGRESS.md`               tracking + spaced repetition ("Solo?" = the truth)
- `patterns/*/README.md`      per pattern: the idea, the signals, the tools (the "concept")
- `patterns/00_fundamentals/` Big-O: lesson + complexity analysis exercise

## The loop per pattern (the method)

For each step of the roadmap, we run this cycle:

1. **CONCEPT (Claude)**  I explain the pattern: the idea, how to recognize it,
   a throwaway demo. Like we did for Big-O.
2. **PRACTICE (you)**    you pick from the pattern's pool (`PROBLEMS.md`),
   easy/medium/hard depending on your shape, and solve on LeetCode without
   the solution.
3. **REVIEW (Claude)**   you paste your code + its complexity, I give feedback
   (correctness, real complexity, cleanliness, Python idioms).
4. **ANCHORING**         we log it in `PROGRESS.md`, you redo it at D+2 and D+7.

Stuck more than ~15 min on a problem? Ask for a hint, not the solution.

## The loop IN the interview (6 steps, make it a ritual)

1. CLARIFY      rephrase, edge cases, input size, constraints
2. EXAMPLE      walk through a case by hand
3. BRUTE FORCE  the naive solution, stated with its complexity
4. OPTIMIZE     which data structure brings the complexity down?
5. CODE         cleanly, out loud
6. TEST         normal case + edge cases + final complexity

## Roadmap (NeetCode order, problems detailed in PROBLEMS.md)

Core (most interviews hit here):

- [x] 0. Fundamentals: Big-O + Python toolkit
- [ ] 1. Arrays & Hashing   (we are here)
- [ ] 2. Two Pointers
- [ ] 3. Sliding Window
- [ ] 4. Stack
- [ ] 5. Binary Search
- [ ] 6. Linked List
- [ ] 7. Trees (BFS/DFS)

Advanced (after the core):

- [ ] 8. Tries
- [ ] 9. Heap / Priority Queue
- [ ] 10. Backtracking
- [ ] 11. Graphs
- [ ] 12. Dynamic Programming (1-D then 2-D)
- [ ] 13. Intervals
- [ ] 14. Greedy

## Pace

~45 min/day. Consistency > intensity. Spaced repetition (D+2, D+7) anchors
more than volume.
