#include "iostream"
#include <algorithm>
using namespace std;

int main() {
	string N;
	cin >> N;
	int A[10], flag = -1, sum = 0, i = 0;
	A[0] = N[0] - '0';
	A[1] = N[2] - '0';
	A[2] = N[3] - '0';
	A[3] = N[4] - '0';
	A[4] = N[6] - '0';
	A[5] = N[7] - '0';
	A[6] = N[8] - '0';
	A[7] = N[9] - '0';
	A[8] = N[10] - '0';
	A[9] = N[12] - '0';
	for (i = 0; i < 9; i++) {
		sum = sum + A[i] * (i + 1);
	}
	flag = sum % 11;
	if (flag == 10) {
		flag = 'X' - '0';
	}
	if ( A[9] == flag)
		cout << "Right";
	else {
		N[12] = flag + '0';
		cout << N;
	}
	return 0;
}