def count_permutations(s):
    MOD = 10**9 + 7
    n = len(s)
    
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        temp = [0] * (n + 1)
        for j in range(1, i + 1):
            if s[i - 1] == 'D':
                for k in range(j, i + 1):
                    temp[k] = (temp[k] + dp[j - 1]) % MOD
            else:
                for k in range(0, j):
                    temp[k] = (temp[k] + dp[j - 1]) % MOD
        dp = temp
    
    result = sum(dp) % MOD
    return result

# Exemplos de uso:
print(count_permutations("DID"))  # Saída esperada: 5
print(count_permutations("D"))    # Saída esperada: 1
