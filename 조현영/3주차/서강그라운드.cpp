#include <iostream>
#include <vector>

using namespace std;

const int INF = 1e9;
int N, M, R;

void floyd(vector<vector<int>> &graph){
    for(int i=1; i<=N; i++){
        for(int j=1; j<=N; j++){
            for(int k=1; k<=N; k++){
                if(graph[j][i] + graph[i][k] < graph[j][k])
                    graph[j][k] = graph[j][i] + graph[i][k];
            }
        }
    }
}

int main() {

    cin >> N >> M >> R; //지역 개수, 예은이 수색 범위, 길의 개수
    vector<int> item(N+1, 0);
    for(int i=1; i<=N; i++){
        cin >> item[i];
    }

    vector<vector<int>> graph(N+1, vector<int>(N+1, INF));
    for(int i=1; i<N+1; i++){
        graph[i][i] = 0;
    }

    for(int i=0; i<R; i++){
        int u, v, w;
        cin >> u >> v >> w;
        graph[u][v] = w;
        graph[v][u] = w;
    }

    floyd(graph);

    int max = 0;
    for(int i=1; i<=N; i++){
        int sum = 0;
        for(int j=1; j<=N; j++){
            if(graph[i][j] <= M){
                sum += item[j];
            }
        }
        if(sum > max)
            max = sum;
    }

    cout << max;
}