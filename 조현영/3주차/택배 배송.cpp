#include <iostream>
#include <vector>
#include <queue>

using namespace std;

typedef pair<int, int> ci;
const int INF = 1e9;
int N, M; //헛간 수, 길의 수

vector<int> dijkstra(vector<vector<ci>> graph, int v, int s){
    vector<int> distance(v+1, INF);

    priority_queue<ci, vector<ci>, greater<>> pq; //오름차순
    pq.push({0, s}); //시작점으로부터의 거리, 정점
    distance[s] = 0;

    while(!pq.empty()){
        int node = pq.top().second;
        int weight = pq.top().first;
        pq.pop();
        if(weight > distance[node])
            continue;

        for(int i=0; i<graph[node].size(); i++){
            int next_node = graph[node][i].first;
            int next_weight = weight + graph[node][i].second;
            if(distance[next_node] > next_weight){
                distance[next_node] = next_weight;
                pq.push({next_weight, next_node});
            }
        }
    }

    return distance;

}

int main(){
    cin >> N >> M;

    vector<vector<ci>> graph(N+1, vector<ci>(0));
    for(int i=0; i<M; i++){
        int u, v, w;
        cin >> u >> v >> w;
        int min = INF;
        for(int j=0; j<graph[u].size(); j++){ //연결된 간선이 여러개인 헛간이라면 가중치 더 작은 길로
            if(graph[u][j].second == v){
                min = graph[u][j].first;
            }
        }
        if(w < min){
            graph[u].emplace_back(v, w);
            graph[v].emplace_back(u, w);
        }
    }

    vector<int> distance = dijkstra(graph, N, 1);
    cout << distance[N];
}

