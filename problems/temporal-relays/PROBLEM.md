# Temporal Relays — algorithm exercise

A directed network has `n` nodes and `m` scheduled relay links. For a directed link `(u, v, offset, period, travel)`, departures occur at `offset`, `offset+period`, `offset+2*period`, ... Each departure reaches `v` exactly `travel` time units later. You can wait at any node, and initially stand at node 1 at time 0.

Find the earliest time you can reach node `n`, or output `-1` if unreachable.

## Input

`n m`, with `1 <= n <= 200000`, `0 <= m <= 300000`.

For each edge: `u v offset period travel`, where nodes are in `[1,n]`, `0 <= offset <= 1e9`, `1 <= period <= 1e9`, `0 <= travel <= 1e9`.

## Output

The earliest arrival time as an integer, or `-1`.

## Example

```text
3 3
1 2 2 4 3
2 3 6 5 1
1 3 20 1 0
```

Output: `7` (depart 1->2 at time 2, arrive 5; depart 2->3 at 6, arrive 7).

## Intended solution

Dijkstra on arrival times. For arrival `t` at `u`, the earliest available departure is `offset` if `t <= offset`, otherwise `offset + ceil((t-offset)/period)*period`. The edge relaxation time is departure + travel. Because departing later cannot yield an earlier arrival along the same edge, FIFO monotonicity holds; waiting is allowed. Thus earliest-arrival labels can be settled with Dijkstra.

Complexity: `O((n+m) log n)` time and `O(n+m)` memory. Use 64-bit arithmetic.

**Portfolio note:** Newly authored exercise, not a claim of uniqueness among all published online judges.
