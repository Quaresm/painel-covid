# Painel-Covid

O **Painel de Covid** é uma aplicação simples em Python projetada para ajudar e organizar hospitais ou pacientes que foram infectados pela COVID-19
---

## 📋 Como funciona?

1. **Pré-requisitos**:
   - Você precisará de um ambiente que suporte a execução de código Python. Você pode usar:
     - **VSCode** (Visual Studio Code) – Editor de código recomendado.
     - **Terminal do Windows** ou **Terminal do Linux**.
   
2. **Instalação**:
   - Certifique-se de ter o **Python 3.6 ou superior** instalado. Se não tiver, baixe e instale a versão mais recente [aqui](https://www.python.org/downloads/).
   
3. **Execução**:
   - Para rodar a aplicação, basta seguir os passos abaixo:
   
     1. **Clone o repositório**:
        ```bash
        git clone https://github.com/Quaresm/painel-covid
        ```
     2. **Acesse a pasta do projeto**:
        ```bash
        cd painel-covid
        ```
     3. **Execute o programa**:
        - No VSCode, você pode abrir o terminal integrado e digitar:
          ```bash
          python start.py
          ```
        - Ou, no terminal do Windows/Linux, basta navegar até a pasta onde o projeto foi clonado e rodar o comando acima.

4. **Cadastro de pacientes**:
   - Informe o número de pacientes a serem cadastrados (não tem mínimo nem máximo).
   - Para cada funcionário, insira:
     - **Nome** (apenas letras).
     - **Data de início dos sintomas**  no formato `DD/MM/AAAA`.
     - **Data de confirmação da COVID-19**  no formato `DD/MM/AAAA`.

5. **Validação**:
   - O nome deve conter **apenas letras**.
   - A data deve ser válida e seguir o formato `DD/MM/AAAA`.

---
