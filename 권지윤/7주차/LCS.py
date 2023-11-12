target_word = input()
word = input()
dp = [[0 for _ in range(len(target_word)+1)] for _ in range(len(word)+1)]
for i in range(len(word)):
    for j in range(len(target_word)):
        if word[i] == target_word[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(max(max(dp)))
