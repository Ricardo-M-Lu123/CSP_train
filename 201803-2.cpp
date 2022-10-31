#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct ball {
	int num;//编号
	int Pos;//位置
	int flag;//方向 1为→，-1为←
};

bool cmp1(ball b1, ball b2) {
	return b1.Pos < b2.Pos;
}

bool cmp2(ball b1, ball b2) {
	return b1.num < b2.num;
}

int main() {
	int n, L, t, a; //数量，长度，秒数
	cin >> n >> L >> t;
	vector<ball> Ball;
	ball temp;
	int num = 1;
	temp.Pos = 0;
	temp.flag = 0;
	temp.num = 0;
	Ball.push_back(temp);
	while (n--) {
		cin >> a;
		temp.Pos = a;
		temp.flag = 1;
		temp.num = num++;
		Ball.push_back(temp);
	}
	temp.Pos = L;
	temp.flag = 0;
	temp.num = num;
	Ball.push_back(temp);
	sort(Ball.begin(), Ball.end(), cmp1);

	for (int num = 0; num < t; num++) {
		for (vector<ball>::iterator it = Ball.begin(); it != Ball.end(); it++) {
				if ((*it).Pos + (*it).flag == (*(it + 1)).Pos + (*(it + 1)).flag) {
					(*it).Pos = (*it).Pos + (*it).flag;
					(*(it + 1)).Pos = (*(it + 1)).Pos + (*(it + 1)).flag;
					(*it).flag = (*it).flag * -1;
					(*(it + 1)).flag = (*(it + 1)).flag * -1;
					it++;
				} 
				else if((*it).flag > 0) (*it).Pos++;
				else if((*it).flag < 0) (*it).Pos--;
		}
	}
	sort(Ball.begin(), Ball.end(), cmp2);
	for (vector<ball>::iterator it = Ball.begin() + 1; it != Ball.end() - 1; it++) {
		cout << (*it).Pos << ' ';
	}
	return 0;
}