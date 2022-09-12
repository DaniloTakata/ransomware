"""
ENVIO DE EMAIL QUANDO O EMISSOR FOR OUTLOOK, UTILIZA O OUTLOOK DA MÁQUINA
import win32com.client as win32
from login import *

destino = rec


def send_email(key):
    # Integra o outlook com a aplicação
    outlook = win32.Dispatch('outlook.application')

    # Cria um e-mail
    email = outlook.CreateItem(0)

    # Configurações do e-mail
    email.To = rec
    email.Subject = 'Chave'
    email.HTMLBody = f'<p>{key}</p>'
    email.Send()


send_email('Teste de envio')
print("Enviou")

"""

import win32com.client as win32
from login import *

destino = rec


def send_email(key):
    # Integra o outlook com a aplicação
    outlook = win32.Dispatch('outlook.application')

    # Cria um e-mail
    email = outlook.CreateItem(0)

    # Configurações do e-mail
    email.To = rec
    email.Subject = 'Chave'
    email.HTMLBody = f'<p>{key}</p>'
    email.Send()
