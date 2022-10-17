#include "iostream"
#include <algorithm>
using namespace std;

int main() {
	int N, sum = 0;
	cin >> N;
	int A[1001] = {0};
	int i = N, temp;
	while (i--) {
		cin >> temp;
		A[abs(temp)] ++;
	}
	for (i = 0; i < 1000; i++) {
		sum = sum + A[i] / 2;
	}
	cout << sum;
	return 0;
}