"""Compile both C++ references and compare with independent Python oracles."""
import argparse
from pathlib import Path
import random
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def compile_reference(name: str, workdir: Path) -> Path:
    src = ROOT / "problems" / name / "reference.cpp"
    binary = workdir / name
    subprocess.run(["g++", "-std=c++17", "-O2", "-Wall", "-Wextra", "-pedantic",
                    str(src), "-o", str(binary)], check=True, capture_output=True, text=True)
    return binary


def run(binary: Path, text: str) -> str:
    completed = subprocess.run([str(binary)], input=text, text=True, capture_output=True,
                               timeout=4, check=True)
    return completed.stdout.strip()


def oracle_jump(costs: list[int], k: int) -> tuple[int, int]:
    dp = [(costs[0], 0)]
    for i in range(1, len(costs)):
        best = min(dp[max(0, i-k):i])
        dp.append((best[0] + costs[i], best[1] + 1))
    return dp[-1]


def oracle_relays(n: int, edges: list[tuple[int,int,int,int,int]]) -> int:
    # Independent small-case Bellman-Ford-style dynamic relaxation, not Dijkstra.
    inf = 10**18
    dist = [inf] * n
    dist[0] = 0
    for _ in range(n):
        changed = False
        for u, v, offset, period, travel in edges:
            if dist[u] == inf:
                continue
            departure = max(dist[u], offset)
            if departure > offset:
                departure = offset + ((departure-offset+period-1)//period)*period
            arrival = departure + travel
            if arrival < dist[v]:
                dist[v] = arrival
                changed = True
        if not changed:
            break
    return -1 if dist[n-1] == inf else dist[n-1]


def stress(iterations: int, seed: int) -> dict[str, int]:
    rng = random.Random(seed)
    with tempfile.TemporaryDirectory() as temp:
        folder = Path(temp)
        jump_bin = compile_reference("bounded-jump", folder)
        relay_bin = compile_reference("temporal-relays", folder)
        for case in range(iterations):
            n = rng.randint(1, 35)
            k = rng.randint(1, n)
            costs = [rng.randint(-100, 100) for _ in range(n)]
            input_text = f"{n} {k}\n" + " ".join(map(str, costs)) + "\n"
            expected = oracle_jump(costs, k)
            actual = tuple(map(int, run(jump_bin, input_text).split()))
            assert actual == expected, f"bounded-jump case={case} seed={seed}, expected={expected}, actual={actual}"
            n = rng.randint(1, 12)
            m = rng.randint(0, 35)
            edges = []
            for _ in range(m):
                edges.append((rng.randrange(n), rng.randrange(n), rng.randint(0, 20),
                              rng.randint(1, 20), rng.randint(0, 20)))
            lines = [f"{n} {m}"] + [f"{u+1} {v+1} {o} {p} {t}" for u,v,o,p,t in edges]
            actual_relay = int(run(relay_bin, "\n".join(lines) + "\n"))
            expected_relay = oracle_relays(n, edges)
            assert actual_relay == expected_relay, (
                f"temporal-relays case={case} seed={seed} expected={expected_relay} actual={actual_relay}")
        assert run(jump_bin, "1 1\n-42\n") == "-42 0"
        assert run(jump_bin, "5 2\n2 100 -4 3 5\n") == "3 2"
        assert run(relay_bin, "3 3\n1 2 2 4 3\n2 3 6 5 1\n1 3 20 1 0\n") == "7"
        assert run(relay_bin, "2 0\n") == "-1"
    return {"bounded_jump_random_cases": iterations, "temporal_relays_random_cases": iterations,
            "deterministic_edge_cases": 4, "seed": seed}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--iterations", type=int, default=500)
    parser.add_argument("--seed", type=int, default=91)
    args = parser.parse_args()
    import json
    print(json.dumps(stress(args.iterations, args.seed), indent=2))


if __name__ == "__main__":
    main()
