# RECOGNITION: which pattern for which problem

The interview reflex: read the statement, spot a SIGNAL, deduce the tool.
This table is your reading grid. With reps, it moves into your head and you
won't need to reread it.

## Signals → reflex

| In the statement you see...                                   | Reflex / tool |
|---------------------------------------------------------------|---------------|
| "seen before?", "duplicate", "all distinct", "unique"         | **set** (`in` O(1), `.add`) |
| "how many times", "frequency", "anagram"                      | **Counter** |
| "the K most frequent", "top K"                                | **Counter.most_common(k)** |
| "find back by value" (its index, its position, a link)        | **dict** `{value: info}` (Two Sum style) |
| "group by a common key / signature"                           | **defaultdict(list)** |
| "SORTED array" + "a pair / two numbers that..."               | converging **two pointers** (left/right) |
| "CONTIGUOUS subarray / substring" (longest / shortest)        | **sliding window** (window + left/right) |
| "the max / min / best ALONG the traversal"                    | **accumulator** (var outside + `max`/`min` inside) |
| "common / union / difference" between two collections        | **set operations** (`&`, `\|`, `-`) |
| "by positions / reversed / every 2 steps"                     | **range(start, stop, step)** |

## The golden reflex (90% of optimizations)

Replace a **search** with a **hashmap**:

- `x in list` (O(n))  →  `x in set/dict` (O(1))
- "I traverse again to find something"  →  I **remember** it in a set/dict along the way.

If you're stuck on "how do I optimize", ask yourself:
> "What am I searching for again in a loop, and could I remember it
> once to find it back in O(1)?"

## The approach when you read a new problem

1. What is the **structure** of the input? (sorted array? string? pairs?)
2. What am I **looking for**? (a duplicate? a pair? the longest? a count?)
3. These two answers → a signal from the table → a tool.
4. **Brute force first** (state its complexity), **then optimize** with the right tool.
