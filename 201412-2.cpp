#include "iostream"
#include "queue"
using namespace std;

int main() {
	int N;
	queue<int> result;
	cin >> N;
	int A[N][N];
	int i = N, j = N, x;
	for (i = 0; i < N; i++)
		for (j = 0; j < N; j++) {
			cin >> x;
			A[i][j] = x;
		}
	for (i = 0; i < N; i++) {
		if (i % 2) {
			for ( j = 0; j <= i ; j++) {
				result.push(A[j][i - j]);
			}
		} else {
			for ( j = 0; j <= i; j++ ) {
				result.push(A[i - j][j]);
			}
		}
	}
	for (i = N; i < 2 * N - 1; i++) {
		if (i % 2) {
			for ( j = i - N + 1; j < N ; j++) {
				result.push(A[j][i - j]);
			}
		} else {
			for ( j = i - N + 1; j < N; j++ ) {
				result.push(A[i - j][j]);
			}
		}
	}
	while (!result.empty()) {
		cout << result.front() << ' ';
		result.pop();
	}

	return 0;
}
