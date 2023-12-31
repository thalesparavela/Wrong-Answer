import sys

def calcular_combinacao_minima(elementos, valor_total):
    dp = [float('inf')] * (valor_total + 1)
    dp[0] = 0
    resto = 0
    
    if(valor_total>10*elementos[-1]):
        resto = valor_total//elementos[-1]
        valor_total= valor_total%(elementos[-1])

        if valor_total==0:
            return resto
        if (elementos[-1] == elementos[-2]+1):
            aux =elementos[-2]-valor_total
            valor_total = elementos[-1]*aux+valor_total
            resto = resto-aux
        else:
            resto = resto-10
            valor_total+=elementos[-1]*10
    for elemento in elementos:
        for i in range(elemento, valor_total + 1):
            dp[i] = min(dp[i], dp[i - elemento] + 1)
    return dp[valor_total]+resto
vetor = list(range(1, 1000000 + 1))
casos = int(sys.stdin.readline().strip())
##with open("saida", "w") as arquivo_saida:
for _ in range(casos):
    numpedra, tamanho = map(int, sys.stdin.readline().strip().split())
    pedras = list(map(int, sys.stdin.readline().strip().split()))
    pedras.sort()
    ##print(pedras)
    min_elementos = calcular_combinacao_minima(pedras, tamanho)
    print(min_elementos)
    ##print(min_elementos, file=arquivo_saida)
