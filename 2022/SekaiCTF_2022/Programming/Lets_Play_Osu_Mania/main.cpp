#include <bits/stdc++.h>

using namespace std;

const int MAXN = 1e4 + 7;

int n;

string a[MAXN];

int main()
{
    if (fopen("test.inp", "r"))
        freopen("test.inp", "r", stdin);

    cin >> n;
    getline(cin, a[0]);
    for (int i = 0; i < n; ++i)
        getline(cin, a[i]);

    for (int i = 0; i < n; ++i)
        for (int j = 0; j < 6; ++j)
            if (a[i][j] == '#')
            {
                if (i > 0 && a[i - 1][j] == '-') a[i - 1][j] = ' ';
                if (i < n - 1 && a[i + 1][j] == '-') a[i + 1][j] = ' ';
            }
    int ans = 0;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < 6; ++j)
            if (a[i][j] == '#')
            {
                int k = i;
                while (k < n)
                {
                    if (a[k][j] == '#') a[k][j] = ' ';
                    else break;
                    ++k;
                }
                ++ans;
            }   
            else ans += a[i][j] == '-';

    cout << ans;
    return 0;
}