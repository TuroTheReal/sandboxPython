# PROGRESS

Spaced repetition: redo each problem at D+2 and D+7.
Claude keeps this file up to date, Arthur codes. Levels are strictly factual.

"Level" = level on the LATEST attempt (first try or review). Each dated
review in Notes carries its own level in brackets.

| Level  | Meaning |
|--------|---------|
| SOLID  | Alone, first try, nothing to fix. Acquired. |
| POLISH | Alone and close: approach right, small slips (syntax, edge case) fixed once pointed out. |
| GUIDED | Needed questions or hints to find the approach or fix the logic. |
| GAP    | A basic was missing (language feature or concept): had to learn it to finish. Named in Notes as "Gap: ..." with its kind: "unknown" (never knew it) or "not recalled" (knew it, did not think of it / misused it). |
| GIVEN  | Solution or key structure given. Redo solo. |

Qualifiers added after the level when relevant: "(not optimal)" = correct but
worse complexity than expected; "(stuck)" = blocked before asking.
Notes always say where Claude helped: "Help: ...".

## Sprint: CodinGame-style screening test

Typical format: 2 questions, one easy, one hard where brute force fails the
hidden tests on large inputs.
LC = LeetCode, CG = CodinGame (list and URLs in `PROBLEMS.md`).

- [ ] hashing (review)  : LC #217, #1 from memory · CG The Descent, Temperatures
- [ ] two pointers      : LC #167, #238, #125 solo · CG Horse-racing Duals
- [ ] stack             : LC #20, #739 · CG MIME Type
- [ ] intervals         : LC #56, #57, #986
- [ ] intervals         : LC #435, #1094 · CG Defibrillators
- [ ] binary search     : LC #704, #875 · CG Shadows of the Knight 1
- [ ] grid BFS/DFS      : LC #200, #994 · CG There is no Spoon 1
- [ ] D+7 reviews (#56, #986, #739, #875) + kata `katas/availabilities/`
- [ ] 1h timed mock     : 1 easy + CG Stock Exchange Losses + Python MCQ

| Date       | Problem                   | Pattern        | Time  | Level  | D+2       | D+7       | Notes |
|------------|---------------------------|----------------|-------|--------|-----------|-----------|-------|
| 2026-08-11 | #242 Valid Anagram        | arrays_hashing | ~     | SOLID  | [x] 08-17 solo | [ ] 08-24 | `Counter==Counter`. Reviewed from memory on 08-17, one clean shot = ACQUIRED. |
| 2026-08-13 | #217 Contains Duplicate   | arrays_hashing | ~     | GUIDED | [x] 08-17 | [x] 10-08 | `set` + early exit. Solo on first try. Reviewed 08-17: structure from memory OK, syntax slips (`{}` vs `set()`, `.append` vs `.add`) fixed. Reviewed 10-08 [GUIDED]: Counter version (slip: iterating a dict gives keys only, needs `.items()`), then one-liner `len(set(nums)) != len(nums)` (first wrote `==`: inverted the question). Early-exit version redone from a hint (useless `enumerate`). Gap (partly known): space complexity, said he was less familiar with it (what it counts, worst vs best case); thought the one-liner was O(1) time. |
| 2026-08-13 | #1 Two Sum                | arrays_hashing | ~     | GUIDED | [x] 08-17 | [x] 10-08 | dict `{value: index}` + enumerate. Reviewed 08-17: structure recalled from memory (enumerate included!), one slip `seen[comp]` vs `seen[num]` fixed. O(n) space. Reviewed 10-08 [GUIDED]: started with a `set` (can't store the index), switched to dict after a hint. |
| 2026-08-13 | #49 Group Anagrams        | arrays_hashing | ~     | POLISH | [x] 08-18 | [ ] 08-25 | `defaultdict(list)` + `tuple(sorted(word))`. Reviewed 08-18: skeleton from memory, 3 slips (tuple, useless `if` guard, `list(values())`). defaultdict mechanism + dict `in` O(1) fully understood after questions. Redo for fluency. |
| 2026-08-14 | #347 Top K Frequent       | arrays_hashing | ~     | POLISH | [x] 08-18 | [ ] 08-25 | `Counter().most_common(k)`. Reviewed 08-18: comprehension from memory, nudge on `most_common(k)` (forgot it takes k). Footgun: reused `k` (parameter) as loop variable (works thanks to evaluation order, but bad habit). O(n log k). |
| 2026-08-14 | #238 Product Except Self  | arrays_hashing | ~     | GIVEN  | [ ] 08-16 **REDO SOLO** | [ ] 08-21 | Prefix/suffix. Given (stuck). |
| 2026-08-17 | #125 Valid Palindrome     | two_pointers   | ~     | GIVEN  | [ ] 08-19 **REDO SOLO** | [ ] 08-24 | Skip structure given (fiddly). Mistakes: method parentheses, `elif` vs 3 `if`. |
| 2026-08-17 | #167 Two Sum II           | two_pointers   | ~     | SOLID  | [x] 08-20 | [ ] 08-27 | Two pointers on sorted input. Time O(n), Space O(1). Reviewed 08-20 SOLO from memory, with the idiomatic `while left<right` structure (better than the first draft) = ACQUIRED. |
| 2026-08-20 | #11 Container Most Water  | two_pointers   | ~     | GUIDED | [ ] 08-22 | [ ] 08-27 | Two pointers: move the shorter wall, area = width × min(heights). Guided on the accumulator pattern (`max_area` outside the loop) + 2 fixes (`h * w`, compare heights not positions); structure assembled by him. Time O(n), Space O(1). |
| 2026-08-24 | #121 Best Time Buy/Sell   | sliding_window | ~     | GUIDED | [ ] 08-26 | [ ] 08-31 | Single-pass accumulator (min_price + max_profit). DERIVED the O(n²)→O(n) optimization himself through Socratic questions (started from "double loop"). 2 fixes: `float('inf')` (not `Max_int`), profit `price - min` not the reverse. |
| 2026-08-24 | #3 Longest Substring      | sliding_window | ~     | GUIDED | [ ] 08-26 | [ ] 08-31 | Sliding window. First O(n²) (list window), then OPTIMIZED to O(n) (set + left pointer + accumulator), guided but assembled by him. Fixed the illegal `longest[left]` on a set → `s[left]`. Saw amortized analysis (while inside for stays O(n) because left never moves back). Time O(n), Space O(n). |
| 2026-08-25 | #383 Ransom Note          | arrays_hashing | ~     | GUIDED | [ ] 08-27 | [ ] 09-01 | Counter + "enough of each letter" (>= per letter, NOT == like #242). Recognized the Counter reflex alone and ruled out `in`. Fluency fixes: `.items()` (2nd time), `>` vs `!=`. Consolidation. |
| 2026-08-25 | #349 Intersection Arrays  | arrays_hashing | ~     | POLISH | [ ] 08-27 | [ ] 09-01 | `list(set(a) & set(b))` in one line, almost solo. Closure on `&`: used well here (intersection = common items), where he had misused it on #242 (which needed `Counter ==`). Learned `&`/`\|`/`-` on sets. |
| 2026-08-26 | #219 Contains Duplicate II | arrays_hashing | ~     | POLISH | [ ] 08-28 | [ ] 09-02 | dict `{value: last position}` (Two Sum reflex) + check `i - seen[num] <= k`. Recognized the pattern alone, 2 fixes (distance direction, unconditional update outside `else`). Time O(n), Space O(n). |
| 2026-09-01 | #205 Isomorphic Strings   | arrays_hashing | ~     | GUIDED | [ ] 09-03 | [ ] 09-08 | dict as a MAPPING + `set used` for the bijection (both directions). Fiddlier than "easy" (bad difficulty pick), Rule 2 given. BUT spotted the repeated-letters bug alone (an else catching one case too many). Lesson: branch on "seen vs new", not on consistency. |
| 2026-09-01 | #344 Reverse String       | two_pointers   | ~     | POLISH | [ ] 09-03 | [ ] 09-08 | Converging two pointers + swap (by hand with a `keep` temp, valid; Python idiom `a,b=b,a` shown). First did `s.reverse()` (shortcut) then the manual version to drill the pattern. Time O(n), Space O(1). |
| 2026-10-08 | CG The Descent            | accumulator    | ~     | GUIDED | [ ] 10-12 | [ ] 10-15 | First CodinGame: understood the game loop (one `input()` = one line, one `print` per turn). 1st try: sorted then printed the height (lost the index). Asked how the input loop works. Fixed with a 2-variable accumulator (after hint) (max height + index), reset each turn. Time O(n), Space O(1) per turn. Init at 0 works since heights >= 0, `-1` / `float('-inf')` is the safer reflex. |
| 2026-10-08 | CG Temperatures           | accumulator    | ~     | GUIDED | [ ] 10-12 | [ ] 10-15 | Gap (unknown): `abs()`, said he did not know it when asked which built-in gives the distance to 0. Help: `abs()` given; bugs pointed out (sign flag never reset, stored the distance not the temperature, `input is none`, `*= -1` corruption, double output when n = 0, `print` indented inside the `for`); skeleton given for the n = 0 branch. Alone: tie-break `max(closest, t)` on equal distance (clean), `float('inf')` init, complexity right incl. the `split()` trap (Time O(n), Space O(n)). |
