import sys
input = sys.stdin.readline
total = int(input())
wine= []
dp = [0] * total
for _ in range(total):
    wine.append(int(input()))
if total <= 2:
    print(sum(total))
else:
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    for i in range(2, total):
        dp[i] = max(dp[i-2]+wine[i], dp[i-3]+ wine[i-1]+wine[i],dp[i-1] ) # 한칸 차이로 안마신 경우, 마셨는데 1칸 차이로 마신 경우, 2칸 차이로 마신 경우
    print(max(dp))
