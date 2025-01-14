def newman_conway(n):
    if n < 1:
        return []

    memo = [0, 1, 1]
    count = 3
    while count <= n:
        memo.append(memo[memo[count - 1]] + memo[count - memo[count - 1]])
        count += 1

    return memo[1:n+1]