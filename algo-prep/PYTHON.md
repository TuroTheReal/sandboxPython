# PYTHON: common methods and idioms

Keep it open while you code. Fluency comes from TYPING these, not from
reading them. This cheat sheet unblocks you, it doesn't replace the reps.

## The rule that trips you up the most

A method call ALWAYS has parentheses.

    s.lower       -> the method itself (an object, always truthy), NOT the result
    s.lower()     -> the result             <- this is what you want

Same for `.values()`, `.most_common(k)`, `.isalnum()`, `.keys()`, `.items()`...
No `()` = no execution.

## Strings (str)

    s.lower() / s.upper()      lowercase / uppercase
    s.isalnum()                True if letter OR digit (bool)
    s.isdigit()                True if digits only
    s.strip()                  removes leading/trailing whitespace
    s.split(",")               splits into a list on the separator
    "-".join(items)            joins a list of str with a separator
    s[::-1]                    the string reversed

## Lists

    lst.append(x)              append at end
    sorted(lst)                new sorted list (O(n log n))
    lst[::-1]                  the list reversed
    [x for x in lst if cond]   comprehension: filter / transform
    [a for a, b in pairs]      tuple unpacking in a comprehension

## Dict / set

    d.get(key, default)        read without crashing (returns default if missing)
    d.values() / .keys() / .items()   iterate
    key in d                   membership test O(1)
    st.add(x)                  add to a set

## collections

    from collections import Counter, defaultdict
    Counter(iterable)          counts occurrences
    c.most_common(k)           the k most frequent -> [(elem, count), ...]
    defaultdict(list)          missing key -> []
    defaultdict(set)           missing key -> set()
    defaultdict(int)           missing key -> 0   (for counting)

## Numbers

    abs(x)                     distance to 0: abs(-3) == 3, abs(5) == 5
    max(a, b) / min(a, b)      larger / smaller of two values (also takes an iterable)
    float('inf')               a value bigger than any number (start of a min search)

## Conversions

    list(x)   set(x)   tuple(x)   str(x)   int(x)
    tuple(sorted(word))        hashable key from a sort (a "signature")
    "".join(sorted(word))      same, but as a string

## Loops / indices

    for i, x in enumerate(lst)         index + value at the same time
    range(start, stop_excl, step)      e.g. range(len(l)-1, -1, -1) = reverse traversal
    a // b                             INTEGER division (drops the remainder)
    a / b                              regular division (float result)
