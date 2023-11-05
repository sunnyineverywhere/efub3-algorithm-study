#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main(){

    ios::sync_with_stdio();
    cin.tie(0);

    int n;
    cin >> n;

    vector<vector<int>> tree(n+1, vector<int>(0));
    vector<int> result(n+1, 0);

    for(int i=0; i<n-1; i++){
        int u, v;
        cin >> u >> v;

        tree[u].push_back(v);
        tree[v].push_back(u);
    }

    queue<int> q;
    q.push(1);

    while(!q.empty()){

        int cur = q.front();
        q.pop();
        for(int i=0; i<tree[cur].size(); i++){
            int node = tree[cur][i];
            if(result[node] == 0){
                q.push(node);
                result[node] = cur;
            }
        }
    }

    for(int i=2; i<=n; i++){
        cout << result[i] << '\n';
    }

}