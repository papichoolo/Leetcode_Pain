#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool findPath(vector<vector<char>>& grid, int i, int j) {
    int n = grid.size();
    int m = grid[0].size();

    if (i < 0 || i >= n || j < 0 || j >= m || grid[i][j] == 'X')
        return false;

    if (i == n - 1 && j == m - 1)
        return true;

    grid[i][j] = 'X'; // Mark current cell as visited

    // Explore all four directions
    if (findPath(grid, i + 1, j) || findPath(grid, i - 1, j) || findPath(grid, i, j + 1) || findPath(grid, i, j - 1))
        return true;

    // If none of the directions lead to cheese, backtrack
    grid[i][j] = 'o'; // Mark current cell as unvisited
    return false;
}

void printGrid(const vector<vector<char>>& grid) {
    for (const auto& row : grid) {
        for (char cell : row) {
            if (cell == 'X')
                cout << "T ";
            else
                cout << "0 ";
        }
        cout << endl;
    }
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<char>> grid(n, vector<char>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> grid[i][j];
        }
    }

    if (findPath(grid, 0, 0)) {
        printGrid(grid);
    } else {
        cout << "NO PATH FOUND" << endl;
    }

    return 0;
}