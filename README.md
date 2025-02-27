# Desafio - Target Sistemas

Este repositório contém a resolução de um conjunto de desafios em Python. Abaixo, você encontrará a descrição de cada exercício e a forma como ele foi implementado.

## 1) Cálculo do Valor da Variável SOMA

### Descrição:
O código executa uma operação de soma acumulada, onde uma variável `SOMA` recebe valores incrementados de 1 até um valor fixo `INDICE = 13`.

### Implementação:
- Utiliza um loop `while` para iterar enquanto `k < indice`.
- Em cada iteração, `k` é incrementado e somado à variável `soma`.
- Ao final, o valor de `soma` é impresso.

### Saída Esperada:
```
Valor de SOMA: 91
```

## 2) Verificação de um Número na Sequência de Fibonacci

### Descrição:
O programa recebe um número e verifica se ele pertence à sequência de Fibonacci.

### Implementação:
- A sequência começa em `0` e `1`.
- Um loop calcula os próximos números até atingir ou ultrapassar o número fornecido.
- Se o número estiver na sequência, retorna uma mensagem de confirmação.

### Exemplo de Entrada:
```
Digite um número para verificar se pertence à sequência de Fibonacci: 8
```

### Exemplo de Saída:
```
8 pertence à sequência de Fibonacci.
```

## 3) Processamento do Faturamento Diário

### Descrição:
O programa processa um conjunto de dados em formato JSON contendo o faturamento diário de uma distribuidora e retorna:
- O menor faturamento diário.
- O maior faturamento diário.
- O número de dias com faturamento superior à média mensal.

### Implementação:
- Os valores são lidos e armazenados ignorando dias sem faturamento (`valor = 0`).
- Calcula-se a média dos dias faturados.
- Retorna-se o menor e o maior faturamento e a contagem de dias acima da média.

### Exemplo de Saída:
```
Menor faturamento: 1000
Maior faturamento: 3000
Dias com faturamento acima da média: 2
```

## 4) Cálculo do Percentual de Representação do Faturamento por Estado

### Descrição:
Dado um faturamento mensal detalhado por estado, o programa calcula a porcentagem de contribuição de cada estado em relação ao total.

### Implementação:
- Soma-se o faturamento total.
- Calcula-se a porcentagem de cada estado em relação ao total.
- Exibe-se o resultado formatado.

### Exemplo de Saída:
```
Percentual de representação por estado:
SP: 37.53%
RJ: 20.31%
MG: 16.18%
ES: 15.04%
Outros: 10.97%
```

## 5) Inversão de uma String sem Funções Prontas

### Descrição:
O programa recebe uma string e a exibe de forma invertida sem utilizar funções nativas como `reverse()`.

### Implementação:
- Utiliza um loop `for` para iterar a string de trás para frente e armazenar os caracteres invertidos.
- Imprime a string resultante.

### Exemplo de Entrada:
```
Digite uma string para inverter: Python
```

### Exemplo de Saída:
```
nothyP
```

## Como Executar o Código

1. Certifique-se de ter o Python instalado.
2. Baixe o arquivo `desafio_python.py`.
3. Execute o script com:
   ```bash
   python desafio_python.py
   ```
4. Insira os valores conforme solicitado pelo programa.
