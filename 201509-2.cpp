#include <bits/stdc++.h>
using namespace std;
using gg = long long;

int main() {
	int y, d, i;
	cin >> y >> d;
	int m[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	if ((y % 4 == 0) && (y % 100 != 0) || (y % 400 == 0)) {
		m[1] = 29;
	}
	for (i = 0; i < 12; i++) {
		if (d > m[i])
			d = d - m[i];
		else
			break;
	}
	cout << i + 1 << '\n' << d << endl;
	return 0;
}