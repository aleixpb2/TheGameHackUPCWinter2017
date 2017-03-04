#include <iostream>
#include <vector>
using namespace std;

typedef vector<char> VC;
typedef vector<VC> VVC;

struct Pos {
    int x;
    int y;

    void operator+=(const Pos& other) {
        x += other.x;
        y += other.y;
    }
};

bool validPosition(const VVC& M, const vector<Pos>& VP, Pos p) {
    for (const Pos& pAux : VP) {
        p += pAux;
        //cout << p.x << " " << p.y << " " << M[p.x][p.y] << endl;
        if (M[p.x][p.y] == 'X') return false;
    }
    return true;
}

int numberValid(const VVC& M, const vector<Pos>& VP, int n, int m) {
    int total = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (M[i][j] == 'X') continue;
            //cout << n << " " << m << " " << i << " " << j << endl;
            if (validPosition(M, VP, {i, j})) {
                ++total;
                //cout << "hit " << total << endl;
            }
        }
    }
    return total;
}

int main() {
    int n, m;
    int total = 0;
    while(cin >> n >> m) {

        vector<Pos> VP;
        string s;
        cin >> s;
        for (const char& c : s) {
            if (c == 'N') VP.push_back({-1, 0});
            else if (c == 'S') VP.push_back({1, 0});
            else if (c == 'W') VP.push_back({0, -1});
            else VP.push_back({0, 1});
        }

        VVC M(n, VC(m));
        for (VC& F : M) for (char& c : F) cin >> c;
        total += numberValid(M, VP, n, m);
    }
    cout << total << endl;
}