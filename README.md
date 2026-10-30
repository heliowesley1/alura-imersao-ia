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

## Desafio 02 - Calculadora: Adicionar nova funcionalidade

Atualização da calculadora com a inclusão da operação de **Potenciação / Exponenciação (`^`)**, demonstrando a evolução contínua do projeto:

* **Nova Função Modular (`potenciar`):** Implementada para calcular exponenciações (`x ** y`) de forma isolada e reutilizável.
* **Tratamento de Exceções Avançado (`try / except`):**
  * Proteção contra `ZeroDivisionError` em potências com base zero e expoente negativo ($0^{-n}$).
  * Proteção contra `OverflowError` para números excessivamente grandes fora do limite do sistema.
  * Suporte a expoentes decimais/fracionários (cálculo de raízes, como $9^{0.5} = 3.0$) e detecção de números complexos.
* **Menu Atualizado:** Inclusão da opção `5. Potenciação (^)` e ampliação do filtro de validação de entrada para o intervalo de `0` a `5`.

---

## Como Executar

```bash
python calculadora.py
