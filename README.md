# 📧 Sistema de Disparo Automático de E-mails com Python

Projeto simples para envio automático de e-mails com múltiplos destinatários e anexos, utilizando Python, SMTP SSL e MIME para formatação de mensagens HTML e anexos.

> Repositório: [https://github.com/Markosalves12/email_automatico](https://github.com/Markosalves12/email_automatico.git)

---

## ⚙️ Funcionalidades

- Envio de e-mails em formato HTML
- Envio para múltiplos destinatários
- Anexos múltiplos (PDF, imagens, etc)
- Autenticação segura via SMTP SSL (exemplo usando Gmail)
- Código modular para fácil personalização

---

## 🧰 Tecnologias Utilizadas

- Python 3.x
- Biblioteca padrão `smtplib`, `ssl`, `email`
- SMTP Gmail (requer senha de aplicativo para autenticação)

---

## 🔧 Configuração

1. Crie um arquivo `dados.py` na raiz do projeto com as seguintes variáveis:

```python
sender_email = "seu_email@gmail.com"
password = "sua_senha_de_aplicativo"
receiver_email = "destinatario1@example.com"
receiver_email2 = "destinatario2@example.com"
receiver_email3 = "destinatario3@example.com"
