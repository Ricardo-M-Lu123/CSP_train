#include "iostream"
#include <algorithm>
using namespace std;

int main() {
	int N;
	cin >> N;
	int A[10001] = {0};
	int i = N, temp;
	while (i--) {
		cin >> temp;
		A[temp] ++;
	}
	cout << max_element(A, A + 10001) - A;
	return 0;
}