#include <iostream>
#include <vector>
#include <set>

using namespace std;

vector<char> vec;
int N = 16;
    set<strings> corrects;

void checkandadd(){
    //
}

void backtrack(int i){
    if(i >= 16) return;
    vec[i] = '(';
    checkandadd(vec, i+1);
    vec[i] = ')';
    checkandadd(vec, i+1);
}

int main(){
    vec = vector<char>(N, '(');
    backtrack(0);
    cout << corrects.size() << endl;
}
