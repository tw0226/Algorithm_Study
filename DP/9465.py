T = int(input())

for i in range(T):
    n = int(input())
    dp = [0 for j in range(n+1)]
    for j in range(n+1):
       dp[j] = [0 for x in range(2)]

    sticker = [0 for x in range(2)]
    for j in range(2):
        sticker[j] = [0]+list(map(int, input().split()))
    if n>=1:
        dp[1][0] =sticker[0][1]
        dp[1][1] =sticker[1][1]
    if n>=2:
        dp[2][0] = sticker[1][1] + sticker[0][2]
        dp[2][1] = sticker[0][1] + sticker[1][2]

    for j in range(3, n+1):
        dp[j][0] = max(dp[j-1][1] + sticker[0][j], dp[j-2][0] + sticker[0][j], dp[j-2][1] + sticker[0][j])
        dp[j][1] = max(dp[j-1][0] + sticker[1][j], dp[j-2][0] + sticker[1][j], dp[j-2][1] + sticker[1][j])
        # print(dp)
    print(max(dp[n]))
