# 🤖 Bot Automático de Preenchimento de Formulários (Google Forms)

Este projeto é um **bot em Python** que automatiza o preenchimento de um formulário do **Google Forms** usando dados armazenados em um arquivo CSV.

---

## 🚀 Tecnologias usadas
- [Python 3](https://www.python.org/)
- [Selenium](https://www.selenium.dev/)
- [Pandas](https://pandas.pydata.org/)
- [Webdriver-Manager](https://pypi.org/project/webdriver-manager/)

---

## 📂 Estrutura do Projeto
form-bot/
│── bot.py # código principal
│── data.csv # base de dados
│── requirements.txt # bibliotecas necessárias
│── README.md # documentação do projeto


---

## 🔧 Como rodar o projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/form-bot.git
   cd form-bot

2. Instale as dependências:
  pip install -r requirements.txt
3. Adicione seus dados em data.csv.
4. Execute o bot:
python bot.py

🎯 Exemplo de data.csv
nome,cpf,email,telefone
Fernando,12345678900,fernando@email.com,11999999999
Ana,98765432100,ana@email.com,11988888888
Carlos,11122233344,carlos@email.com,11777777777

✨ Funcionalidades

Preenche automaticamente Nome, CPF, Email e Telefone no Google Forms.
Lê os dados de um arquivo CSV.
Submete o formulário para cada linha do CSV.
Permite fácil customização para outros formulários.

📌 Próximos passos

  Gerar dados de teste com a biblioteca Faker
  Executar em headless mode (sem abrir o navegador)
  Adicionar logs de execução
  Criar pipeline de CI/CD com GitHub Actions

Autor:
Projeto desenvolvido por Fernando Ferreira Alves
