#include <bits/stdc++.h>
using namespace std;
using gg = long long;

struct node {
	int num = 0; //出现次数
	int name; //字母序号
} A[1001];

bool cmp(node a, node b) {
	if (a.num == b.num)
		return a.name < b.name;
	else
		return a.num > b.num;
}

int main() {
	int N, x;
	cin >> N;
	while (N--) {
		cin >> x;
		A[x].name = x;
		A[x].num++;
	}
	sort(A, A + 1001, cmp);
	for (int i = 0; i < 1001; i++) {
		if (A[i].num) {
			cout << A[i].name << ' ' << A[i].num << endl;
		} else
			break;
	}
	return 0;
}