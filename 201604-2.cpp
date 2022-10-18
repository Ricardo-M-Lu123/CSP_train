#include <bits/stdc++.h>
using namespace std;

int sum(int A[][10], int B[][4], int k) {
	//遍历15遍，相加，出现2则退出
	int m, n;
	int i;

	for (i = 0; i < 18; i++) {
		for (m = i; m < i + 4; m++) {
			for (n = k; n < k + 4; n++)
				if (A[m][n] + B[m - i][n - k] > 1)
					return i - 1;
		}
	}
	return i - 1;
}

int main() {
	//输入
	int i, j, temp, k;
	int A[22][10], B[4][4];

	for (i = 3; i < 18; i++) {
		for (j = 0; j < 10; j++) {
			cin >> temp;
			A[i][j] = temp;
		}
	}

	for (i = 0; i < 4; i++) {
		for (j = 0; j < 10; j++) {
			A[i][j] = 0;
		}
	}
	for (i = 18; i < 22; i++) {
		for (j = 0; j < 10; j++) {
			A[i][j] = 1;
		}
	}


	for (i = 0; i < 4; i++) {
		for (j = 0; j < 4; j++) {
			cin >> temp;
			B[i][j] = temp;
		}
	}
	cin >> k;
	k = k - 1;
	int m, n;
	temp = sum(A, B, k);
	for (m = temp ; m < temp + 4; m++)
		for (n = k; n < k + 4; n++)
			A[m][n] += B[m - temp][n - k];

	for (i = 3; i < 18; i++) {
		for (j = 0; j < 10; j++)
			cout << A[i][j] << ' ';
		cout << endl;
	}
	return 0;
}