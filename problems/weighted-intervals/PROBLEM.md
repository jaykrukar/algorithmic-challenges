# Weighted Intervals — algorithm exercise

You are given up to `n` optional work intervals. Each interval has a start time,
an end time, and a signed value. Two selected intervals may touch at an endpoint
but may not overlap. Choose a subset with maximum total value; selecting nothing
is allowed.

## Input

`n` (`0 <= n <= 200000`), followed by `n` lines of `start end value`.
Times satisfy `0 <= start < end <= 1,000,000,000`; values are signed integers
between `-1,000,000,000` and `1,000,000,000`.

## Output

One integer: the maximum total value of a non-overlapping subset.

## Example

```text
4
1 3 5
3 5 6
2 6 10
6 8 4
```

Output:

```text
15
```

The first, second, and fourth intervals produce value 15.

## Intended solution

Sort intervals by end time. For each interval `i`, binary search for the number
of earlier intervals whose end is at most its start. Dynamic programming chooses
between skipping `i` or adding its value to that compatible prefix's best value.
The empty schedule has value zero, so negative-value intervals can be skipped.

Complexity is `O(n log n)` time and `O(n)` memory. The exercise is not claimed to
be unique among published problem sets.
