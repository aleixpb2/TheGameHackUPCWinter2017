#include <iostream>
#include <vector>

using namespace std;

int main(){
    int N, M;
    int sum = 0;

    // Input
    while(cin >> N){
        cin >> M;
        vector<pair<int,int>> water;
        string instr;
        cin >> instr;
        vector<vector<char>> board(N, vector<char> (M));
        for(int i = 0; i < N; ++i)
            for(int j = 0; j < M; ++j){
                cin >> board[i][j];
                if(board[i][j] == '.')
                    water.push_back(make_pair(i,j));
            }

        // Algorithm
        for(int i = 0; i < water.size(); ++i){ // for each water spot
            int posX, posY;
            posX = water[i].first;
            posY = water[i].second;
            bool correct = true;
            for(int k = 0; k < instr.size() && correct; ++k){ // for each instr
                if(instr[k] == 'N')
                    --posX;
                else if(instr[k] == 'S')
                    ++posX;
                else if(instr[k] == 'E')
                    ++posY;
                else if(instr[k] == 'W')
                    --posY;
                if(board[posX][posY] == 'X')
                    correct = false;
                else if(k == (instr.size() - 1)) ++sum; // valid
            }
        }
    }
    cout << sum << endl;
}
