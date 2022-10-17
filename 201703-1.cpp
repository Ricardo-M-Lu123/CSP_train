#include "iostream"
using namespace std;

int main() {
	int n, k, i, a;
	int sum = 0, temp = 0;
	cin >> n >> k;
	i = n;
	while (i--) {
		cin >> a;
		temp = temp + a;
		if (temp < k) {}
		else {
			sum = sum + 1;
			temp = 0;
		}
	}
	if (temp)
		sum = sum + 1;
	cout << sum;

	return 0;
}