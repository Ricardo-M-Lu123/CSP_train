#include "iostream"
using namespace std;

int main() {
	int n, m, temp = 0, A;
	cin >> n >> m;
	int a[n + 1] = {0}, b[n + 1] = {0}, c[n] = {0};
	c[0] = 1;
	int i = n;
	while (i--) {
		cin >> A;
		a[n - i] = A;
		c[n - i] = c[n - i - 1] * a[n - i];
	}
	i = n;
	int j = m;
	do {
		temp = j / c[i - 1];
		if (temp) {
			b[i] = temp;
			j = j - b[i] * c[i - 1];
		}
	} while (--i > 1);
	b[1] = j;
	i = n;
	while (i--) {
		cout << b[n - i] << ' ';
	}
	return 0;
}