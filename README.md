# Calculadora Básica em Python

Calculadora interativa via terminal que executa as quatro operações matemáticas básicas, com foco em boas práticas de programação e tratamento de erros.

---

## Principais Componentes

* **Funções Modulares:** Funções separadas para soma, subtração, multiplicação e divisão (com proteção contra divisão por zero).
* **Menu Contínuo (`while True`):** Mantém a aplicação rodando até que o usuário digite `0`.
* **Tratamento de Exceções (`try / except`):** Impede que o programa trave caso o usuário digite letras em vez de números.

---

## Como Funciona

### 1. Entrada de Dados e Operação
* O menu exibe as opções e captura a escolha via `input()`.
* O programa valida a escolha usando `if/elif/else`. Se for válida, solicita dois números e os converte com `float()`.

### 2. Lógica dos Cálculos e Resultados
* A aplicação direciona os números informados para a função matemática correspondente à opção escolhida.
* O resultado é processado e exibido formatado no terminal usando *f-strings* (ex: `10 + 5 = 15`).

---

## Comportamento em Diferentes Operações

* **Números Decimais:** Suporta casas decimais (ex: `5.5 * 2 = 11.0`).
* **Divisão por Zero:** Exibe uma mensagem amigável sem interromper a execução.
* **Entradas Inválidas:** Letras ou opções fora do menu (0 a 4) são interceptadas com mensagens de aviso.

---

## Como Executar

```bash
python calculadora.py