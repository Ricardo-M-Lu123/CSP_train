#include <iostream>
#include <vector>
const int num = 20;
using namespace std;
int main(int argc, char *argv[]) {
	int N,temp;
	vector<int> A;
	cin >> N;
	int i = N;
	while(i--){
		A.push_back(5);
	}
	i = N;
	int j;
	while(i--){
		cin >> temp;
		for(j = 0; j < num; j++){
			if(temp <= A[j]){
				for(int k = 1; k <= temp; k++){
					cout << j * 5 + k + 5 - A[j] <<' ';
				}
				cout << endl;
				A[j] = A[j] - temp;
				break;
			}
		}
		if(j >= num){
			for(j = 0; j < num; j++){
				if(A[j]){
					for(int k = 1; k <= temp && k  <= A[j]; k++){
						cout << j * 5 + k + 5 - A[j] <<' ';
					}
					if(temp < A[j])
						A[j] = A[j] - temp;
					else A[j] = 0;
					temp = temp - A[j];
				}
			}
			cout << endl;
		}
	}
	return 0;
}