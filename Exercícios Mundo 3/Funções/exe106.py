c = ('\033[m',
     '\033[0;30;41m')

def pyHelp(msg):
    help(msg)

def titulo(msg,cor=0):
    tam = len(msg)
    print(c[cor],end='')
    print('-'*tam)
    print(msg)
    print('-'*tam)
    print(c[0],end='')

while True:
    
    titulo('SISTEMA DE AJUDA',1)
    comando = input('Função ou Biblioteca: ')
    if comando.upper() == 'FIM':
        break
    else:
        pyHelp(comando)