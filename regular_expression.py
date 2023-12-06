class Solucao:
    def corresponde(self, s: str, p: str) -> bool:
        linhas = len(p) + 1
        colunas = len(s) + 1
        dp = [[False] * colunas for _ in range(linhas)]

        dp[0][0] = True

        for i in range(1, linhas):
            if p[i - 1] == '*':
                dp[i][0] = dp[i - 2][0]

        for i in range(1, linhas):
            for j in range(1, colunas):
                caractere_padrao = p[i - 1]
                caractere_string = s[j - 1]

                if caractere_padrao == caractere_string or caractere_padrao == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif caractere_padrao == '*':
                    caractere_anterior_padrao = p[i - 2]
                    dp[i][j] = dp[i - 2][j] or (caractere_anterior_padrao == caractere_string or caractere_anterior_padrao == '.') and dp[i][j - 1]
                else:
                    dp[i][j] = False

        return dp[linhas - 1][colunas - 1]

solution = Solucao()
print(solution.corresponde("aa", "a"))    # Output: False
print(solution.corresponde("aa", "a*"))   # Output: True
print(solution.corresponde("ab", ".*"))   # Output: True