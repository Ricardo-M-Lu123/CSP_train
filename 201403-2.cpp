/*
��������
������ĳͼ�β���ϵͳ��,�� N ������,ÿ�����ڶ���һ��������������ֱ�ƽ�еľ�������
	���ڵı߽��ϵĵ�Ҳ���ڸô��ڡ�����֮���в�ε�����,�ڶ���һ�������ص���������,ֻ����ʾλ�ڶ���Ĵ���������ݡ�
������������Ļ��һ�����ʱ��,���ѡ���˴��ڱ����λ�õ���㴰��,����������ھͻᱻ�Ƶ����д��ڵ����,��ʣ��Ĵ��ڵĲ��˳�򲻱䡣���������λ�ò������κδ���,��ϵͳ���������ε����
������������ϣ����дһ������ģ�������ڵĹ��̡�
�����ʽ
��������ĵ�һ��������������,�� N �� M��(1 �� N �� 10,1 �� M �� 10)
���������� N �а��մ����²㵽����˳����� N �����ڵ�λ�á�
	ÿ�а����ĸ��Ǹ����� x1, y1, x2, y2,��ʾ�ô��ڵ�һ�Զ�������ֱ�Ϊ (x1, y1) �� (x2, y2)����֤ x1 < x2,y1 2��
���������� M ��ÿ�а��������Ǹ����� x, y,��ʾһ������������ꡣ
������Ŀ���漰�������е�;��εĶ���� x, y ����ֱ𲻳��� 2559 �͡���1439��
�����ʽ
����������� M ��,ÿһ�б�ʾһ��������Ľ��������ô������ѡ����һ������,�����������ڵı��(���ڰ��������е�˳��� 1 ��ŵ� N);
	���û��,�����"IGNORED"(����˫����)��

	��������
3 4
0 0 4 4
1 1 5 5
2 2 6 6
1 1
0 0
4 4
0 5
	�������
	2
	1
	1
	IGNORED
*/
#include "iostream"
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int main() {
	int N, M, x1, x2, y1, y2, x, y;
	cin >> N >> M;
	vector<vector<int>> Figure;
	vector<int> temp;
	queue<int> result;
	int i = N;
	do {
		temp.clear();
		cin >> x1 >> y1 >> x2 >> y2;
		temp.push_back(x1);
		temp.push_back(y1);
		temp.push_back(x2);
		temp.push_back(y2);
		temp.push_back(N - i + 1);
		Figure.push_back(temp);
	} while (--i);

	int j = M;
	while (j--) {
		cin >> x >> y;
		i = N;
		while (i--) {
			temp = Figure[i];
			if ((x >= temp[0] && x <= temp[2]) && (y >= temp[1] && y <= temp[3])) {
				result.push(temp.back())  ;
				if (i != (N - 1))
					rotate(Figure.begin() + i, Figure.begin() + i + 1, Figure.end());
				break;
			}
		}
		if (i == -1)
			result.push(0)  ;
	}

	j = M;
	while (j--) {
		if (result.front()) {
			cout << result.front() << endl;
			result.pop();
		} else {
			cout << "IGNORED" << endl;
			result.pop();
		}

	}
	return 0;
}