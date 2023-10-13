#include <string>
#include <vector>
#include <algorithm>
#include <climits> // 자료형의 최댓값을 이용함

using namespace std;

long long min(long long a, long long b){
    return a >=b ? b : a;
}

long long solution(int n, vector<int> times) {
    long long answer = LLONG_MAX; //long long형의 최댓값
    sort(times.begin(), times.end()); // 최댓값을 구하기 위해 자료형 정렬
    long long start = 1;
    long long end = (long long)n * (long long)times[times.size()-1];

    while(start <= end){
        long long mid = (start+end)/2;
        long long temp = 0;

        for(int i=0; i<times.size(); i++){
            temp += mid/times[i];
        }

        if(temp >= n){
            answer = min(answer, mid);
            end = mid-1;
        }
        else{
            start = mid+1;
        }
    }
    return answer;
}