# 1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0; 
# Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
# Imprimir(SOMA); 
# Ao final do processamento, qual será o valor da variável SOMA? 
indice = 13
soma = 0
k = 0

while k < indice:
    k += 1
    soma += k

print(f"Valor de SOMA: {soma}")  # Saída esperada: 91

# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência. 
# 
# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código; 
def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
if is_fibonacci(num):
    print(f"{num} pertence à sequência de Fibonacci.")
else:
    print(f"{num} não pertence à sequência de Fibonacci.")

# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne: 
# • O menor valor de faturamento ocorrido em um dia do mês; 
# • O maior valor de faturamento ocorrido em um dia do mês; 
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal. 
# 
# IMPORTANTE: 
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal; 
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média; 
import json

def processar_faturamento(json_data):
    faturamento = json.loads(json_data)
    valores = [dia["valor"] for dia in faturamento if dia["valor"] > 0]
    
    menor = min(valores)
    maior = max(valores)
    media = sum(valores) / len(valores)
    dias_acima_media = sum(1 for v in valores if v > media)
    
    return menor, maior, dias_acima_media

json_faturamento = '[{"dia": 1, "valor": 1000}, {"dia": 2, "valor": 2000}, {"dia": 3, "valor": 0}, {"dia": 4, "valor": 3000}]'  # Exemplo JSON
menor, maior, dias_acima_media = processar_faturamento(json_faturamento)
print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")

# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado: 
# •	SP – R$67.836,43 
# •	RJ – R$36.678,66 
# •	MG – R$29.229,88 
# •	ES – R$27.165,48 
# •	Outros – R$19.849,53 
# 
# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora. 
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(faturamento_estados.values())
percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento_estados.items()}

print("Percentual de representação por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")

# 5) Escreva um programa que inverta os caracteres de um string. 
# 
# IMPORTANTE: 
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código; 
# b) Evite usar funções prontas, como, por exemplo, reverse; 
def inverter_string(s):
    invertida = ""
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

string = input("Digite uma string para inverter: ")
print(f"String invertida: {inverter_string(string)}")
