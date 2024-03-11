# Meus dados de envio
# email que envia e email que recebe
from dados import sender_email, password, receiver_email, receiver_email2, receiver_email3


"""
sender_email = email que vai fazer os envios -- email@gmail.com
receiver_email = email que vai receber o disparo
password = senha de aplicativo sem os espaços
"""



# script html para teste de envio
from html import html

# bibliotecxas que criam o servidor smtp e estabelece protocolo ssl
import smtplib, ssl

# imports usados
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


# ciração do email
mensagem = MIMEMultipart()

# assunto
mensagem['Subject'] = "text"
# email que envia
mensagem['From'] = sender_email
# lista de emails que recebem
mensagem['To'] = ','.join([receiver_email, receiver_email2, receiver_email3])
# corpo do email
mensagem['Body'] = html

# email
mensagem.attach(MIMEText(mensagem['Body'], 'html'))

###### inserção de anexos
anexo = 'CALENDÁRIO ACADÊMICO 2023.1 EAD - WYDEN.pdf'
with open(anexo, 'rb') as insercao:
    parte = MIMEBase(_maintype='Application', _subtype='pdf')
    parte.set_payload(insercao.read())

encoders.encode_base64(parte)

parte.add_header(
    "Content-Disposition",
    f"attachment; filename=calendario.pdf",
)
mensagem.attach(parte)


anexo = 'result-0.png'
with open(anexo, 'rb') as insercao:
    parte = MIMEBase(_maintype='Image', _subtype='png')
    parte.set_payload(insercao.read())

encoders.encode_base64(parte)

parte.add_header(
    "Content-Disposition",
    f"attachment; filename=logo.png",
)
mensagem.attach(parte)


anexo = 'CALENDÁRIO ACADÊMICO 2023.1 EAD - WYDEN.pdf'
with open(anexo, 'rb') as insercao:
    parte = MIMEBase(_maintype='Application', _subtype='pdf')
    parte.set_payload(insercao.read())

encoders.encode_base64(parte)

parte.add_header(
    "Content-Disposition",
    f"attachment; filename=calendario2.pdf",
)
mensagem.attach(parte)

# criação do gerenciador de contexto ssl
contexto = ssl.create_default_context()

# criação do servidor smtp
with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465, context=contexto) as servidor:
    # login no servidor
    servidor.login(sender_email, password=password)
    # envio do email
    servidor.sendmail(
        sender_email, [receiver_email, receiver_email2, receiver_email3], mensagem.as_string()
    )

