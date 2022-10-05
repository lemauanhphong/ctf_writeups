#include <bits/stdc++.h>

using namespace std;

const int MAXN = 2e4 + 7;

int R, N, L, W, M, a[MAXN], par[MAXN];
pair <pair <int, int>, int> b[MAXN];

int root(int u)
{
    return par[u] < 0 ? u : par[u] = root(par[u]);
}

void join(int u, int v)
{
    if ((u = root(u)) == (v = root(v))) return;
    if (par[u] > par[v]) swap(u, v);
    par[u] += par[v];
    par[v] = u;
}

int main()
{
    if (fopen("test.inp", "r"))
        freopen("test.inp", "r", stdin);

    cin >> R >> N;
    for (int i = 1; i <= N; ++i) cin >> a[i];

    cin >> L >> W >> M;
    for (int i = 1; i <= M; ++i)
        cin >> b[i].first.first >> b[i].first.second >> b[i].second;

    for (int i = 1; i <= M + 2; ++i) par[i] = - 1;

    vector <pair <double, pair <int, int> > > edge;
    for (int i = 1; i <= M; ++i)
    {
        for (int j = i + 1; j <= M; ++j)
        {
            double d = (b[j].first.first - b[i].first.first) * (b[j].first.first - b[i].first.first);
            d += (b[j].first.second - b[i].first.second) * (b[j].first.second - b[i].first.second);
            d = sqrt(d) - b[i].second - b[j].second;
            edge.push_back({d, {i, j}});
        }

        edge.push_back({b[i].first.second - b[i].second, {i, M + 1}});
        edge.push_back({W - b[i].first.second - b[i].second, {i, M + 2}});
    }
    edge.push_back({W, {M + 1, M + 2}});

    double ma = - 1;
    sort(edge.begin(), edge.end());
    for (int i = 0; i < edge.size(); ++i)
    {
        join(edge[i].second.first, edge[i].second.second);
        if (root(M + 1) == root(M + 2)) 
        {
            ma = edge[i].first / 2;
            break;
        }
    }
    if (ma == - 1) ma = W / 2.0;

    if (R >= ma) return cout << - 1, 0;

    int ans = 0;
    sort(a + 1, a + N + 1);
    for (int i = 1; i <= N; ++i)
        if (R + a[i] < ma) ++ans, R += a[i];
        else break;
    cout << ans;
    return 0;  
}