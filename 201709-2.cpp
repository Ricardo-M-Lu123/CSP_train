#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

struct key {
	int num; //±àºÅ
	int start_time;
	int end_time;
};

bool cmp_start(key m1, key m2) {
	return m1.start_time < m2.start_time;
}

bool cmp_end(key m1, key m2) {
	if (m1.num != m2.num)
		return m1.end_time < m2.end_time;
	else
		return m1.num < m2.num;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0), cout.tie(0);

	int N, K;
	cin >> N >> K;
	vector<int> Key;
	int i = N;
	while ( i-- ) {
		Key.push_back( N - i);
	}
	vector<key> start, end;
	i = K;
	key temp;
	int w, s, c;
	while ( i-- ) {
		cin >> w >> s >> c;
		temp.num = w;
		temp.start_time = s;
		temp.end_time = s + c;
		start.push_back(temp);
		end.push_back(temp);
	}
	sort(start.begin(), start.end(), cmp_start);
	sort(end.begin(), end.end(), cmp_end);
	int m, n;
	for ( m = 0, n = 0; m < K && n < K;) {
		if (start[m].start_time < end[n].end_time) {
			vector<int>::iterator it = find(Key.begin(), Key.end(), start[m].num);
			*it = 0;
			m++;
		} else {
			vector<int>::iterator it = find(Key.begin(), Key.end(), 0);
			*it = end[n].num;
			n++;
		}
	}
	while ( n < K) {
		vector<int>::iterator it = find(Key.begin(), Key.end(), 0);
		*it = end[n].num;
		n++;
	}
	for ( vector<int>::iterator it = Key.begin() ; it != Key.end(); it++) {
		cout << *it << ' ';
	}
	return 0;
}