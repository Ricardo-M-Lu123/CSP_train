#include "iostream"
#include <algorithm>
using namespace std;

int main() {
	int N, sum = 0;
	cin >> N;
	int A[N];
	int i = N;
	while (i--) {
		cin >> A[N - i - 1];
	}
	i = 0;
	sort(A, A + N);
	for (i = 0; i < N - 1; i++) {
		if (A[i + 1] - A[i] == 1)
			sum++;
	}
	cout << sum;
	return 0;
}