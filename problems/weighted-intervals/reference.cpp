#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>

struct Interval {
    std::int64_t start;
    std::int64_t end;
    std::int64_t value;
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    if (!(std::cin >> n)) return 0;
    std::vector<Interval> intervals(n);
    for (auto& item : intervals) {
        std::cin >> item.start >> item.end >> item.value;
    }
    std::sort(intervals.begin(), intervals.end(), [](const auto& left, const auto& right) {
        if (left.end != right.end) return left.end < right.end;
        return left.start < right.start;
    });

    std::vector<std::int64_t> ends;
    ends.reserve(n);
    for (const auto& item : intervals) ends.push_back(item.end);
    std::vector<std::int64_t> best(n + 1, 0);
    for (int i = 0; i < n; ++i) {
        const auto prefix_end = std::upper_bound(ends.begin(), ends.begin() + i,
                                                 intervals[i].start);
        const auto compatible_count = static_cast<int>(prefix_end - ends.begin());
        const auto take = intervals[i].value + best[compatible_count];
        best[i + 1] = std::max(best[i], take);
    }
    std::cout << best[n] << '\n';
}
