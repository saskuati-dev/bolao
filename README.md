# Bolão Web App

Sistema web para criação e participação em bolões de eventos esportivos, culturais ou personalizados. O objetivo é permitir que usuários criem bolões, compartilhem links de participação e registrem palpites de forma simples e segura.
🚀 Status do Projeto

    Em desenvolvimento:
    Estruturação do backend com Flask e MongoDB, definição dos modelos de dados, rotas principais e autenticação básica.

⚙️ Tecnologias Utilizadas

    Python (Flask)
    MongoDB (NoSQL)
    Docker (ambiente de desenvolvimento)
    Pytest (testes automatizados)
    Docker Compose (orquestração de containers)
    python-dotenv (variáveis de ambiente)

📝 Funcionalidades (Fase Atual)

    Cadastro e autenticação de usuários
    Criação de bolões com rounds e concorrentes definidos pelo criador

📁 Estrutura Inicial do Projeto

bolao/  
│  
├── app.py  
├── models.py  
├── routes/  
│   ├── auth.py  
│   ├── bolao.py  
│   └── palpites.py  
├── tests/  
│   └── test_bolao.py  
├── requirements.txt  
├── Dockerfile  
├── docker-compose.yml  
└── .env.example  

🛠️ Como rodar o projeto

    Clone o repositório
    Configure o arquivo .env com suas variáveis de ambiente
    Suba os containers com Docker Compose:

    docker-compose up --build  

    Acesse a aplicação em http://localhost:5000

📌 Próximos Passos
    
    Geração de link único para participação no bolão
    Participação de convidados via link
    Registro de palpites por rodada
    Estrutura flexível para diferentes tipos de bolão (ex: futebol, Oscar, etc.)
    Implementar interface web (frontend)
    Adicionar testes automatizados para novas rotas
    Integração com serviços de e-mail para recuperação de senha
    Deploy em ambiente cloud (AWS)

👨‍💻 Contribuição

Sinta-se à vontade para abrir issues, sugerir melhorias ou enviar pull requests!
