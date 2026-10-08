# Kata: availabilities (free slots in a calendar)

Classic appointment-booking kata. No solution here: write
`availabilities.py` and `test_availabilities.py` in this folder.

    make test FILE=katas/availabilities/test_availabilities.py

## Statement

Write a function that, given a start date, returns the free slots of a
calendar over the next **7 days** (start date included).

The calendar holds two kinds of events:

- **opening**: an opening range on a given day. It can be **recurring
  weekly** (same weekday, same hours).
- **appointment**: an already booked appointment, which blocks that range.

Slots last **30 minutes**. A slot is free if it lies entirely within an
opening and overlaps no appointment.

Output: a list of 7 items, one per day, each with the date and the list of
start times of the free slots (`"9:30"`, not `"09:30"`).

## Reference example (your first test)

Events:

| kind        | start            | end              | weekly recurring |
|-------------|------------------|------------------|------------------|
| opening     | 2014-08-04 09:30 | 2014-08-04 12:30 | yes (Monday)     |
| appointment | 2014-08-11 10:30 | 2014-08-11 11:30 | no               |

Called with start date `2014-08-10` (a Sunday). Expected:

| index | date       | free slots                            |
|-------|------------|---------------------------------------|
| 0     | 2014-08-10 | `[]`                                  |
| 1     | 2014-08-11 | `["9:30", "10:00", "11:30", "12:00"]` |
| 2     | 2014-08-12 | `[]`                                  |
| 6     | 2014-08-16 | (last item)                           |

And the list has exactly 7 items.

## Constraints

- The data model is yours (dataclass, dict, tuples): justify your choice.
- Add tests for the edge cases (finding them is part of the exercise).
- Be pragmatic about performance: state the complexity.
