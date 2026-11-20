#include <bits/stdc++.h>
using namespace std;
using int64 = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    if (!(cin >> n >> k)) return 0;
    vector<int64> a(n), dp(n);
    vector<int> jumps(n);
    for (auto& x : a) cin >> x;
    dp[0] = a[0];
    deque<int> candidates;
    candidates.push_back(0);
    for (int i = 1; i < n; ++i) {
        while (!candidates.empty() && candidates.front() < i - k)
            candidates.pop_front();
        int best = candidates.front();
        dp[i] = dp[best] + a[i];
        jumps[i] = jumps[best] + 1;
        pair<int64, int> current = {dp[i], jumps[i]};
        while (!candidates.empty() &&
               current <= make_pair(dp[candidates.back()], jumps[candidates.back()]))
            candidates.pop_back();
        candidates.push_back(i);
    }
    cout << dp[n-1] << " " << jumps[n-1] << "\n";
}
