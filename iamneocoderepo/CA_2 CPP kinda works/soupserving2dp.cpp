#include <iostream>
#include <vector>
using namespace std;

double soup_servings(int N) {
    if (N >= 5000)
        return 1.0;
    
    // Since serve(a, b) depends only on a and b,
    // we can reduce the size of the DP array to N / 25 + 1
    int size = N / 25 + 1;
    vector<vector<double>> dp(size, vector<double>(size, 0.0));
    
    // Base cases
    dp[0][0] = 0.5;
    for (int i = 1; i < size; ++i) {
        dp[0][i] = 1.0;
        dp[i][0] = 0.0;
    }
    
    // Fill DP table
    for (int a = 1; a < size; ++a) {
        for (int b = 1; b < size; ++b) {
            dp[a][b] = 0.25 * (dp[max(a - 4, 0)][b] +
                               dp[max(a - 3, 0)][max(b - 1, 0)] +
                               dp[max(a - 2, 0)][max(b - 2, 0)] +
                               dp[max(a - 1, 0)][max(b - 3, 0)]);
        }
    }
    
    return dp[N / 25][N / 25];
}

int main() {
    int n = 50;
    cout << soup_servings(n) << endl;  // Output: 0.625
    return 0;
}