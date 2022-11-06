#include <iostream>
#include <vector>
using namespace std;
using gg = long long;
using namespace std;

int main(int argc, char *argv[]) {
	gg n,N;
	cin >> n >> N;//输入个数，和范围
	gg r = N / (n+1);
	gg i = n;
	// 初始化
	gg Ai = 0, fi = 0, gi = 0, num = 0;
	gg sum = 0;
	gg last_gi = 0;
	gg last_num = 0;
	while(i--){
		cin >> Ai;
		fi = n - i;
		gi = Ai / r;
		num = Ai % r;
		gg sum_0 = 0;
		for(gg i = last_gi; i <= gi; i++){
			int j = 0, end = r;
			if( i == last_gi) j = last_num;
			if( i == gi) end = num;
			for(; j < end; j++)
				sum_0 = sum_0 + abs( i- fi + 1 );
		}
		last_gi = gi; last_num = num;
		sum = sum + sum_0;
	}
	Ai = N-1; fi = n; gi = (N-1) / r; num = (N-1) % r;
	gg sum_0 = 0;
	for(gg i = last_gi; i <= gi; i++){
		int j = 0, end = r;
		if( i == last_gi) j = last_num;
		if( i == gi) end = num;
		for(; j < end; j++)
			sum_0 = sum_0 + abs( i- fi);
	}
	sum_0 = sum_0 + gi - fi;
	sum = sum + sum_0;
	cout << sum;
	return  0;
}
