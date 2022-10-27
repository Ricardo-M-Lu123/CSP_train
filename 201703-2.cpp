#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int find(int p , vector<int> N){
	vector<int>::iterator it = find(N.begin(), N.end(), p);
	if (it != N.end())
		return distance(begin(N),it);
	return -1;
}
int main(int argc, char *argv[]) {
	int m,n,p,q;
	cin >> n;
	vector<int> N;
	int i = n;
	while(i--){
		N.push_back(n - i);
	}
	cin >> m;
	int j = m, temp , Pos , flag;
	while(j--){
		cin >> p >> q ;
		Pos = find(p , N);
		temp = N[Pos];
		flag = q / abs(q); //只能为 + - 1；
		for( i = 0; i < flag * q; i++){
			N[ Pos + i * flag ] = N[ Pos + ( i + 1 ) *flag ] ;
		}
		N[ Pos + i * flag ] = temp;
	}
	for( vector<int>::iterator it = N.begin() ; it != N.end() ; it++ )
		cout << *it << ' ';
}