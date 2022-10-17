#include "iostream"
using namespace std;

int main() {
	int score = 0, t = 0, num;
	while (1) {
		cin >> num;
		if (num == 0)
			break;
		else if (num == 1) {
			t = 0;
			score = score + t + 1;
		} else if (num == 2) {
			score  = score + t + 2;
			t = t + 2;
		}
	}
	cout << score ;
	return 0;
}