"""
ENVIO DE EMAIL COM EMISSO SENDO GMAIL
import smtplib
from email.message import EmailMessage
from login import username, password, rec

email = username
pss = password


def send_email(key):
    # Cria um e-mail
    msg = EmailMessage()
    msg['Subject'] = 'Chave'
    msg['From'] = email
    msg['To'] = rec
    msg.set_content(key)

    # Envia o e-mail, passando provedor e porta
    with smtplib.SMTP_SSL('smtp.outlook.com', 465) as smtp:
        smtp.login(email, pss)
        smtp.send_message(msg)


send_email("Teste de envio")
print("Finalizado")

"""
import smtplib
from email.message import EmailMessage
from login import username, password, rec

email = username
pss = password


def send_email(key):
    # Cria um e-mail
    msg = EmailMessage()
    msg['Subject'] = 'Chave'
    msg['From'] = email
    msg['To'] = rec
    msg.set_content(key)

    # Envia o e-mail, passando provedor e porta
    with smtplib.SMTP_SSL('smtp.outlook.com', 465) as smtp:
        smtp.login(email, pss)
        smtp.send_message(msg)


send_email("Teste de envio")
print("Finalizado")