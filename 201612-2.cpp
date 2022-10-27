//方法1
#include <bits/stdc++.h>
using namespace std;

int main() {
	double T, S;
	cin >> T;

	if (T < 3500)
		S = T;
	else if (T < 4955)
		S = (T - 3500 * 0.03) / 0.97;

	else  if (T < 7655)
		S =  (T + 45 - 5000 * 0.1) / 0.9;

	else if (T < 11255)
		S =  (T + 45 + 300 - 8000 * 0.2) / 0.8;

	else if (T < 30755)
		S =  (T + 45 + 300 + 900 - 12500 * 0.25) / 0.75;

	else if (T < 44755)
		S =  (T + 45 + 300 + 900 + 6500 - 38500 * 0.3) / 0.7;

	else if (T < 61005)
		S =  (T + 45 + 300 + 900 + 6500 + 6000 - 58500 * 0.35) / 0.65;

	else
		S =  (T + 45 + 300 + 900 + 6500 + 6000 + 8750 - 83500 * 0.45) / 0.55;
	cout << S;
	return 0;
}

//方法2
//#include <bits/stdc++.h>
//using namespace std;
//
//int main() {
//	double T, S, A;
//	cin >> T;
//	double m[7] = {0, 1500, 4500, 9000, 35000, 55000, 80000};
//	double n[7] = {0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45};
//	double x[6];
//	for (int i = 0; i < 6; i++ ) {
//		x[i] = (m[i + 1] - m[i]) * (1 - n[i]);
//	}
//	A = T - 3500;
//	if (A < 0)
//		S = T;
//	else {
//		int i;
//		for (i = 0; i < 6; i++) {
//			A = A - x[i];
//			if (A < 0)
//				break;
//		}
//		if (i < 6) {
//			S = m[i] + (A + x[i]) / (1 - n[i]) + 3500;
//		} else {
//			A = A / 0.55;
//			S = A + m[i] + 3500;
//		}
//	}
//	cout << S;
//	return 0;
//}