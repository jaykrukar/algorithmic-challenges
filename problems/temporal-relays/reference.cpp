#include <bits/stdc++.h>
using namespace std;
using int64 = long long;
struct Edge {int to; int64 offset, period, travel;};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<vector<Edge>> adj(n);
    for (int i = 0; i < m; ++i) {
        int u, v;
        int64 o, p, tr;
        cin >> u >> v >> o >> p >> tr;
        adj[u-1].push_back({v-1, o, p, tr});
    }
    const int64 INF = (1LL << 62);
    vector<int64> dist(n, INF);
    priority_queue<pair<int64,int>, vector<pair<int64,int>>, greater<pair<int64,int>>> pq;
    dist[0] = 0;
    pq.push({0, 0});
    while (!pq.empty()) {
        auto [now, u] = pq.top(); pq.pop();
        if (now != dist[u]) continue;
        if (u == n - 1) break;
        for (auto e : adj[u]) {
            int64 departure = e.offset;
            if (now > departure) {
                int64 diff = now - e.offset;
                departure += ((diff + e.period - 1) / e.period) * e.period;
            }
            int64 arrive = departure + e.travel;
            if (arrive < dist[e.to]) {
                dist[e.to] = arrive;
                pq.push({arrive, e.to});
            }
        }
    }
    cout << (dist[n-1] == INF ? -1 : dist[n-1]) << "\n";
}
