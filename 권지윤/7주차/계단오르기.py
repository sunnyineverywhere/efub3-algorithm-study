# 언제 안밟냐 (밟히거나 안밟히거나)
total = int(input())
stair = []
for i in range(total):
    stair.append(int(input()))
dp = [0] * total
if len(stair) <= 2:
    print(sum(stair))
else:
    dp[0] = stair[0]
    dp[1] = stair[0] + stair[1]
    for i in range(2,total):
        dp[i] = max(dp[i-2]+ stair[i] , dp[i-3]+stair[i-1] + stair[i])
    print(dp[-1])


