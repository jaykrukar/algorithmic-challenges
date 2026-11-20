# Bounded Jump — algorithm exercise

Given `n` positions in a line, each with an integer landing cost `a[i]`, start on position 1 and finish on position `n`. You must jump forward between 1 and `k` positions each time. You pay the cost of every position visited, including starting and ending positions.

Compute the minimum total cost. Among routes of minimum cost, minimize the number of jumps.

## Input

`n k` on the first line, with `1 <= n <= 200000`, `1 <= k <= n`.

Second line: `n` signed integers, each between `-1000000` and `1000000`.

## Output

Two integers: minimum total cost and, among optimal-cost routes, minimum jumps.

## Example

Input:
```text
5 2
2 100 -4 3 5
```

Output:
```text
3 2
```

One optimal route visits positions 1, 3, 5, costing 2 + (-4) + 5 = 3, with two jumps.

## Constraints and expected complexity

Target `O(n)` time using a monotonic deque of candidate predecessor states `(minimum_cost, jump_count)`. The deque maintains indices whose values are increasing lexicographically and expires out-of-window indices.

## Correctness outline

Each valid route to `i` ends at some `j` satisfying `max(0,i-k) <= j < i`. The best candidate minimizes the pair `(cost[j], jumps[j])`, since `a[i]` and one extra jump are constant across choices. A monotonic deque returns that minimum. Popping dominated candidates is safe because a newer index with no worse value remains in the window at least as long. Each index enters/exits the deque at most once.

**Portfolio note:** This exercise was written for this starter; uniqueness relative to all online judges has not been established. It should not be submitted as a guaranteed-original contest problem.
