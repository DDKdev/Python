import time
import os.path

def geraLog(text, nome_arquivo):
    if os.path.isfile('log.txt') is False:
        print('Criando arquivo')
    arquivo= open(nome_arquivo,'a')
    now= time.localtime()
    now_formatado = time.strftime('%d/%m/%y as %H:%M:%S', now)
    now_formatado2 = time.strftime('%x as %X')
    arquivo.write(f'{now_formatado} --> {text}\n')
    arquivo.write(f'{now_formatado2} --> {text}\n')
    arquivo.close()

geraLog('Usuário conectou no sistema', 'log.txt')