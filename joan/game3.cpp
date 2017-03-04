#include <iostream>
#include <string>
#include <set>
using namespace std;

int count = 0;

void calculate(const string& s) {
    ++count;
    calculate("()" + s);
    calculate("(" + s + ")");
}

int main() {
    calculate("");
    cout << count << endl;
}