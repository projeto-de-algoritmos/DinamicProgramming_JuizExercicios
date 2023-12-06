class Solution:
    def maxProfit(self, prices):
        mini = prices[0]  # Inicializa o preço mínimo como o primeiro elemento
        maxprofit = 0     # Inicializa o lucro máximo como 0
        n = len(prices)   # Obtém o número de dias para os quais os preços estão disponíveis

        # Itera pelos preços começando do segundo dia (índice 1)
        for i in range(1, n):
            # Calcula o lucro (diferença entre o preço atual e o preço mínimo visto até agora)
            cost = prices[i] - mini

            # Atualiza o lucro máximo se o lucro atual for maior
            maxprofit = max(cost, maxprofit)

            # Atualiza o preço mínimo visto até agora
            mini = min(mini, prices[i])

        # Retorna o lucro máximo alcançável
        return maxprofit

solution = Solution()

# Teste 1
prices1 = [7, 1, 5, 3, 6, 4]
result1 = solution.maxProfit(prices1)
print(f"Teste 1 - Preços: {prices1}, Lucro Máximo: {result1}")
# Saída esperada: 5

# Teste 2
prices2 = [7, 6, 4, 3, 1]
result2 = solution.maxProfit(prices2)
print(f"Teste 2 - Preços: {prices2}, Lucro Máximo: {result2}")
# Saída esperada: 0
