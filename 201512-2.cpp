#include <iostream>
#include <utility>
using namespace std;
using gg = long long;

int main() {
	//输入矩阵
	int n, m, temp;
	cin >> n >> m;
	pair<int, int> A[n][m];
	int matrix[n][m];
	int i, j, k;
	for (i = 0; i < n; i++)
		for (j = 0; j < m ; j++) {
			cin >> temp;
			matrix[i][j] = temp;
		}

	//建立二维矩阵
	//pair.first 为行，pair.second 为列
	A[0][0].first = 0, A[0][0].second = 0;
	for (i = 1; i < n; i++) {
		A[i][0].first = 0;
		if (matrix[i - 1][0] == matrix[i][0])
			A[i][0].second =  A[i - 1][0].second + 1;
	}

	for (j = 1; j < m; j++) {
		A[0][j].second = 0;
		if (matrix[0][j - 1] == matrix[0][j])
			A[0][j].first =  A[0][j - 1].first + 1;
	}
	for (i = 1; i < n; i++)
		for (j = 1; j < m; j++) {
			if (matrix[i - 1][j] == matrix[i][j])
				A[i][j].second =  A[i - 1][j].second + 1;
			else
				A[i][j].second = 0;
			if (matrix[i][j - 1] == matrix[i][j])
				A[i][j].first =  A[i][j - 1].first + 1;
			else
				A[i][j].first = 0;
		}

	//消除
	for ( i = n - 1; i > -1; i--)
		for ( j = m - 1; j > -1; j--) {
			if (A[i][j].first > 1) {
				k = A[i][j].first + 1;
				while (k--) {
					A[i ][j - k].first = -1;
				}
			}
			if (A[i][j].second > 1) {
				k = A[i][j].second + 1;
				while (k--) {
					A[i - k][j].second = -1;
				}
			}
		}

	//遍历其中一个为-1就是要消除
	for (i = 0; i < n; i++) {
		for (j = 0; j < m ; j++) {
			if (A[i][j].first == -1 || A[i][j].second == -1)
				matrix[i][j] = 0;
			cout << matrix[i][j] << ' ';
		}
		cout << endl;
	}

	return 0;
}