#include "iostream"
using namespace std;

int main() {
	int N = 0;
	int sum = 0;
	cin >> N;
	while ( N > 0 ) {
		if (N >= 50) {
			N -= 50;
			sum += 7;
		} else if (N >= 30) {
			N -= 30;
			sum += 4;
		} else {
			sum = sum + N / 10;
			break;
		}
	}
	cout << sum;
	return 0;
}