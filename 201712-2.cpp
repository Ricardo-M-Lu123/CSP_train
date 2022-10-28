#include <iostream>
#include <vector>
#include <numeric>
#include <utility>
using namespace std;

struct people {
	int num;
	int call;
};

int main() {
	int n, k;
	cin >> n >> k;
	vector<people> V;
	int num = 0;
	people temp;
	for (num = 0; num < n; num++) {
		temp.num = num + 1;
		temp.call = num + 1;
		V.push_back(temp);
	}
	int start = 1, last_size, call;
	while (V.size() > 1) {
		last_size = V.size();
		for (vector<people>:: iterator it = V.begin(); it != V.end(); ) {
			if ( (*it).call % 10 == k || (*it).call % k == 0) {
				V.erase(it);
			}
			else it++;
			if (V.size() == 1)
				break;
		}
		call = 0;
		start = start + last_size;
		for (vector<people>:: iterator it = V.begin(); it != V.end(); it ++) {
			(*it).call = start + call;
			call++;
		}

	}
	cout << (*V.begin()).num;
	return 0;
}