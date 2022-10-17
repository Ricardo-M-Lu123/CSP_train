#include "iostream"
using namespace std;

int main() {
	int N, a[1001] = {0}, sum = 0, n;
	cin >> N;
	int i = N;
	while (i--) {
		cin >> n;
		a[n] = a[n] + 1;
	}
	i = 1;
	while (i <=  1000) {
		if ( N - a[i] == sum * 2 )
			break;
		else {
			sum = sum + a[i];
			i++;
		}
	}
	if (i <= 1000 && a[i] != 0 )
		cout << i;
	else
		cout << -1;
	return 0;
}