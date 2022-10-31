#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
struct buy_time{
  int start;
  int end;
  friend bool operator < (buy_time t1, buy_time t2){
    return t2.start < t1.start;
  }
};

int main(int argc, char *argv[]) {
  int n,a,b;
  cin >> n;
  int i = n;
  queue<buy_time> time1;
  queue<buy_time> time2;
  buy_time temp;
  while(i--){
    cin >> temp.start >> temp.end;
    time1.push(temp);
  }
  i = n;
  while(i--){
    cin >> temp.start >> temp.end;
    time2.push(temp);
  }
  int num = 0;
  while(!time1.empty() && !time2.empty()){
    if(time1.front().end > time2.front().start && time1.front().start <= time2.front().start){
      if(time1.front().end <= time2.front().end){
        num = num + time1.front().end - time2.front().start;
        time1.pop();
      }
      else{
        num = num + time2.front().end - time2.front().start;
        time2.pop();
      }
    }
    else if(time2.front().end > time1.front().start && time2.front().start <= time1.front().start){
      if(time2.front().end <= time1.front().end){
        num = num + time2.front().end - time1.front().start;
        time2.pop();
      }
      else{
        num = num + time1.front().end - time1.front().start;
        time1.pop();
      }
    }
    else{
      if(time1.front().end < time2.front().end)
        time1.pop();
      else time2.pop();
    }
  }
  cout << num;
  return 0;
}