//
// Created by LG on 2023-10-12.
//
#include <iostream>
#include <vector>
#include <queue>

using namespace  std;

typedef pair<int, int> ci;
const int INF = 1e9;
int N, K;

int main(){

    cin >> N >> K;

    vector<int> distance(100001, INF);

    distance[N] = 0;
    priority_queue<ci, vector<ci>, greater<>> pq;
    pq.push({0, N}); //weight, 정점
    while(!pq.empty()){
        int weight = pq.top().first;
        int node = pq.top().second;
        pq.pop();

        if(node == K)
            break;

        if(weight > distance[node])
            continue;

        int next_node;
        if(node * 2 < 100001){
            next_node = node*2;
            if(distance[next_node] > distance[node]){
                distance[next_node] = distance[node];
                pq.push({distance[next_node], next_node});
            }
        }

        if(node > 0){
            next_node = node - 1;
            if(distance[next_node] > distance[node] + 1){
                distance[next_node] = distance[node] + 1;
                pq.push({distance[next_node], next_node});
            }
        }

        if(node < 100000){
            next_node = node + 1;
            if(distance[next_node] > distance[node] + 1){
                distance[next_node] = distance[node] + 1;
                pq.push({distance[next_node], next_node});
            }
        }

    }

    cout << distance[K];

}
