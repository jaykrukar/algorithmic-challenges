# Algorithmic Challenges — C++17 + Differential Testing

[![Tests](https://github.com/jaykrukar/algorithmic-challenges/actions/workflows/tests.yml/badge.svg)](https://github.com/jaykrukar/algorithmic-challenges/actions/workflows/tests.yml)

Two newly authored **portfolio exercises** with optimized C++17 reference solutions, written problem statements, Python slow oracles, and deterministic randomized test generation.

> These problems were created as portfolio exercises. I **have not verified** that no equivalent problem exists online. No claims of contest placements, judging appointments, or prior publications.

## Challenges

| Challenge | Core algorithm | Time complexity |
|---|---|---|
| [Bounded Jump](problems/bounded-jump/PROBLEM.md) | Sliding-window DP + monotonic deque with lexicographic tie-break | `O(n)` |
| [Temporal Relays](problems/temporal-relays/PROBLEM.md) | Time-dependent earliest-arrival Dijkstra with periodic schedules | `O((n+m) log n)` |

## Verify

Requires Python 3.10+ and `g++`:

```bash
python scripts/stress.py --iterations 500 --seed 91
```

The script compiles references in a temporary directory, generates 500 reproducible random cases **for each problem**, compares each C++ result to an independent simpler Python oracle, and checks four deterministic edge cases. The script stops immediately and prints the seed/case if a mismatch occurs.

[Verified seeded test run](docs/stress_results.json).

## Why these tests matter

A reference solution passing examples is weak evidence of correctness. A slower independent oracle supports differential validation, especially around negative costs, tie-breaking, unreachable graphs, waiting times, and periodic schedules. Random testing is **not** a formal proof; problem statements explain why the efficient algorithms are correct.

## Next work

Add custom output checkers for multi-answer construction problems and property-based generators that systematically target incorrect heuristic implementations.

## Provenance

Initial code written with AI assistance and locally tested. Review and extend it before representing it as independently authored expertise. License: MIT.
