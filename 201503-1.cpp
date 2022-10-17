#include "iostream"
using namespace std;

int main() {
	int n, m;
	cin >> n >> m;
	int i, j;
	int A[n][m], B[m][n];
	for (i = 0; i < n; i ++)
		for (j = 0; j < m; j++) {
			cin >> A[i][j];
		}

	for (i = 0; i < m; i++) {
		for (j = 0; j < n; j ++) {
			B[i][j] = A[j][m - i - 1];
			cout << B[i][j] << " ";
		}
		cout << endl;
	}
	return 0;
}