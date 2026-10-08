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
hidden tests on large inputs. Goal: understand, not speed. No timing except
the final mock. LC = LeetCode, CG = CodinGame (list and URLs in `PROBLEMS.md`).

One "Day" = one work session, not a calendar day. Reviews = redo from memory
(D+2 ~ 2 sessions later, D+7 ~ 5 sessions later). Load = new + review items.

| Day | Done | Theme | New | Reviews | Load |
|-----|------|-------|-----|---------|------|
| 1 | [x] | hashing review + accumulator | LC #217, #1 · CG The Descent, Temperatures | (D+7 of #217, #1) | 4 |
| 2 | [~] | two pointers | LC #167, #238, #125 (v1) done · left: CG Horse-racing Duals (started) | #344 (overdue) left | 5 (3 done) |
| 3 | [ ] | carry-over + stack | Carry-over first: CG Horse-racing Duals, LC #344 review. Then LC #20, #739 · CG MIME Type | #49, #347 (overdue) | 7 |
| 4 | [ ] | intervals 1 | LC #56, #57, #986 | D+2: The Descent, Temperatures, #238, #125 | 7 |
| 5 | [ ] | intervals 2 + binary search | LC #435, #1094, #704 | D+2: #20, #739 | 5 |
| 6 | [ ] | grid BFS/DFS | LC #200, #994 | D+2: #56, #57, #986 | 5 |
| 7 | [ ] | D+7 reviews + kata | kata `katas/availabilities/` | D+7: The Descent, Temperatures, #238, #125, #739 · D+2: #435, #1094, #704 | 9 (lighter if D+2 ones are SOLID) |
| 8 | [ ] | timed mock (1h, the only timed session) | 1 easy + CG Stock Exchange Losses + Python MCQ | D+7: #56, #986 · D+2: #200, #994 | 3 + 4 |

Day 4 and Day 7 are the heaviest: if short on time, keep the new problems and
the reviews of GUIDED/GIVEN items, skip reviews of items already SOLID.

Optional (only if ahead):

- LC #875 Koko Eating Bananas (binary search on the answer)
- CG Defibrillators (parsing), Shadows of the Knight 1 (2D binary search), There is no Spoon 1 (grid)
- Overdue reviews: #11, #121, #3, #383, #349, #219, #205

| Date       | Problem                   | Pattern        | Time  | Level  | D+2       | D+7       | Notes |
|------------|---------------------------|----------------|-------|--------|-----------|-----------|-------|
| 2026-08-11 | #242 Valid Anagram        | arrays_hashing | ~     | SOLID  | [x] 08-17 solo | [ ] 08-24 | `Counter==Counter`. Reviewed from memory on 08-17, one clean shot = ACQUIRED. |
| 2026-08-13 | #217 Contains Duplicate   | arrays_hashing | ~     | GUIDED | [x] 08-17 | [x] 10-08 | `set` + early exit. Solo on first try. Reviewed 08-17: structure from memory OK, syntax slips (`{}` vs `set()`, `.append` vs `.add`) fixed. Reviewed 10-08 [GUIDED]: Counter version (slip: iterating a dict gives keys only, needs `.items()`), then one-liner `len(set(nums)) != len(nums)` (first wrote `==`: inverted the question). Early-exit version redone from a hint (useless `enumerate`). Gap (partly known): space complexity, said he was less familiar with it (what it counts, worst vs best case); thought the one-liner was O(1) time. |
| 2026-08-13 | #1 Two Sum                | arrays_hashing | ~     | GUIDED | [x] 08-17 | [x] 10-08 | dict `{value: index}` + enumerate. Reviewed 08-17: structure recalled from memory (enumerate included!), one slip `seen[comp]` vs `seen[num]` fixed. O(n) space. Reviewed 10-08 [GUIDED]: started with a `set` (can't store the index), switched to dict after a hint. |
| 2026-08-13 | #49 Group Anagrams        | arrays_hashing | ~     | POLISH | [x] 08-18 | [ ] 08-25 | `defaultdict(list)` + `tuple(sorted(word))`. Reviewed 08-18: skeleton from memory, 3 slips (tuple, useless `if` guard, `list(values())`). defaultdict mechanism + dict `in` O(1) fully understood after questions. Redo for fluency. |
| 2026-08-14 | #347 Top K Frequent       | arrays_hashing | ~     | POLISH | [x] 08-18 | [ ] 08-25 | `Counter().most_common(k)`. Reviewed 08-18: comprehension from memory, nudge on `most_common(k)` (forgot it takes k). Footgun: reused `k` (parameter) as loop variable (works thanks to evaluation order, but bad habit). O(n log k). |
| 2026-08-14 | #238 Product Except Self  | arrays_hashing | ~     | GIVEN  | [ ] 08-16 **REDO SOLO** | [ ] 08-21 | Prefix/suffix. Given (stuck). Reviewed 10-08 [GIVEN]: remembered the idea (left pass then right pass) but could not code it. Bugs: `left = num` (replace instead of accumulate), `left += num` (sum instead of product), result included nums[i], `right = len(nums)` init. Help: table filled together, then left pass code given (write `result[i] = left` BEFORE `left *= num`). Right pass done ALONE from the mirror description (reverse `range`, `result[i] *= right`). Time O(n), Space O(1) excluding output. Still REDO SOLO. |
| 2026-08-17 | #125 Valid Palindrome     | two_pointers   | ~     | POLISH (not optimal) | [ ] 08-19 **REDO SOLO** | [ ] 08-24 | Skip structure given (fiddly). Mistakes: method parentheses, `elif` vs 3 `if`. Reviewed 10-08 [POLISH (not optimal)]: v1 alone = clean copy with `"".join(c.upper() for c in s if c.isalnum())` then two pointers on the copy. Help: asked for a way to drop non-alnum chars, `join` + `isalnum` idiom given. Time O(n), Space O(n), complexity given right alone. v2 (skip in place, O(1) space) NOT done yet: still REDO SOLO for v2. |
| 2026-08-17 | #167 Two Sum II           | two_pointers   | ~     | GUIDED | [x] 08-20 | [x] 10-08 | Two pointers on sorted input. Time O(n), Space O(1). Reviewed 08-20 SOLO from memory, with the idiomatic `while left<right` structure (better than the first draft) = ACQUIRED. Reviewed 10-08 [GUIDED (not optimal first)]: 1st try = Two Sum #1 hashmap (correct, 1-indexed handled alone, but O(n) space breaks the "constant extra space" constraint and ignores sorted input). Help: pointed to the constraint + hint "one pointer at each end, compare the sum". Then two pointers alone: Time O(n), Space O(1). Polish: compute the sum once per loop. |
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
| 2026-10-08 | CG Horse-racing Duals     | sorting        | ~     | GUIDED | [ ] | [ ] | IN PROGRESS (stopped, tired). 1st try skipped the plan: compared each horse to the previous one in INPUT order (input not sorted, so the closest pair can be missed: 5, 8, 6 gives 2 instead of 1) + `abs(prev) - abs(pi)` instead of `abs(pi - prev)`, condition and assignment in opposite directions (can go negative). Help: both bugs pointed out with counterexamples. Next: answer brute force complexity + what sorting changes, then store, sort, compare neighbors. |
