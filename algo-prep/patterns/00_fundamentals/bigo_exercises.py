"""Big-O: reference answer key.

Analyzing the complexity of existing code is something LeetCode never tests,
and it's exactly what an interviewer asks you ("and the complexity?"). This
file keeps 7 annotated typical cases, to reread when needed.

Reminders: count the loops, a `y in list` is O(n), a sort is O(n log n).
"Space" = extra memory allocated, excluding the input array.
"""


def total_sum(nums: list[int]) -> int:
    total = 0
    for x in nums:
        total += x
    return total
# Time:  O(n)   a single pass
# Space: O(1)   a single variable, independent of n


def all_pairs(nums: list[int]) -> list[tuple[int, int]]:
    pairs: list[tuple[int, int]] = []
    for a in nums:
        for b in nums:
            pairs.append((a, b))
    return pairs
# Time:  O(n²)  loop inside a loop
# Space: O(n²)  the output list holds n x n pairs


def contains_zero(nums: list[int]) -> bool:
    for x in nums:
        if x == 0:
            return True
    return False
# Time:  O(n)   early exit possible, but the worst case walks everything
# Space: O(1)


def binary_search(sorted_nums: list[int], target: int) -> bool:
    lo, hi = 0, len(sorted_nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_nums[mid] == target:
            return True
        if sorted_nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False
# Time:  O(log n)  the [lo, hi] range is halved at each step
# Space: O(1)


def duplicates_slow(nums: list[int]) -> bool:
    for i, x in enumerate(nums):
        if x in nums[i + 1:]:
            return True
    return False
# Time:  O(n²)  the slice nums[i+1:] is walked again by `in`, inside a loop
# Space: O(n)   the slice rebuilds a list (up to n elements) at each step


def duplicates_fast(nums: list[int]) -> bool:
    seen: set[int] = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
# Time:  O(n)   one pass, set lookup in O(1)
# Space: O(n)   the set can hold up to n elements


def two_separate_loops(nums: list[int]) -> int:
    total = 0
    for x in nums:
        total += x
    maximum = nums[0]
    for x in nums:
        if x > maximum:
            maximum = x
    return total + maximum
# Time:  O(n)   two sequential loops: O(n) + O(n) = O(n), not O(n²)
# Space: O(1)
