#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    int cnt = n / 3;
    int bt = 0, bm = 0;
    for (int i = 0; i < n; ++i) {
        if (s[i] == 'T') {
            if (cnt > 0) {
                cnt--;
                bt++;
            } else {
                
                if (bm == 0) {
                    cout << "NO\n";
                    return;
                }
                bm--;
            }
        } else {
            if (bt == 0) {
                cout << "NO\n";
                return;
            }
            bt--;
            bm++;
        }
    }
    cout << "YES\n";
}
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}