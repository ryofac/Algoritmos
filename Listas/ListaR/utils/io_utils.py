## IO UTILS ATUALIZADA
import sys
sys.path.append('./utils')


from time import sleep
from os import system, get_terminal_size
import str_utils as str

def obter_tamanho_tela():
    return get_terminal_size().columns

# ====== ENTRADA ======

def obter_numero(label):
    # candidato = str.tirar_espaco(input(label))
    # if candidato == '': 
    #     print(candidato)
    #     return obter_numero(label= 'Digite novamente: ')
    # for numero in candidato:
    #     if not 57 >= ord(numero) >= 48:
    #         print('Digite um número!')
    #         return obter_numero(label)
    # return float(candidato)

    # => Usando Try-Except
    try:
        num = float(input(label))
    except:
            print('Digite um número!')
            return obter_numero(label)
    return num    
            

def obter_inteiro(label= 'Me diga um número inteiro:\n> ', tipo:str = None) -> int:
    num = obter_numero(label)
    
    if num != int(num):
        print('Digite um número inteiro!') 
        return obter_inteiro(label, tipo)
    
    if not tipo:
        return int(num)
    
    if tipo == '+':
        while not num > 0:
            print('Digite um número positivo!')
            num = obter_numero(label)
        return int(num)
    
    if tipo == '-':
        while not num <= 0:
            print('Digite um número negativo!')
            num = obter_numero(label)
        return int(num)
    

def obter_float(label ='Me diga um número: ', tipo:str = None) -> float:
    num = obter_numero(label)
    if not tipo:   
        return num
    if tipo == '+':
        while not num > 0:
            print('Digite um número positivo!')
            num = obter_numero(label)
        return num
    if tipo == '-':
        while not num <= 0:
            print('Digite um número negativo!')
            num = obter_numero(label)
        return num

         
def obter_numero_positivo(label:str) -> float:
    return obter_float(label, tipo='+')

def obter_numero_negativo(label:str) -> float:
    return obter_float(label, tipo= '-')

def obter_numero_max(label:str, max:int) -> float:
    numero = obter_float(label)
    if not numero < max:
        obter_numero_max(f'Respeite o intervalo máximo ({max}): ', max)
    return numero

def obter_numero_min(label:str, minimo:int):
    numero = obter_float(label)
    if not numero > minimo:
        obter_numero_min(f'Respeite o intervalo mínimo ({minimo}): ', minimo)
    return numero
    
    
def obter_numero_intervalo(label:str, max:float, min:float):
    numero = obter_float(label)
    if not min <= numero <= max:
        obter_numero_intervalo(f'Digite um número pertencente ao intervalo ({min}) -> ({max}): ', max, min)
    return numero
    

def obter_texto(label:str = 'Texto: ') -> str:
    texto = input(label)
    return texto

def obter_texto_min(label:str, tamanho_min:int) -> str:
    texto = obter_texto(label)
    if str.obter_tamanho(texto) < tamanho_min:
        return obter_texto_min(f'Respeite o tamanho mínimo({tamanho_min}): ', tamanho_min)
    return texto

def obter_texto_max(label:str, tamanho_max:int) -> str:
    texto = obter_texto(label)
    if str.obter_tamanho(texto) > tamanho_max:
        return obter_texto_max(f'Respeite o tamanho máximo({tamanho_max}): ', tamanho_max)
    return texto

def obter_char(label:str= 'Insira o caractere: ') -> str:
    return obter_texto_max(label, 1)

def obter_texto_min_max(label:str, tamanho_min:int, tamanho_max:int) -> str:
    texto = obter_texto(label)
    if not tamanho_min < texto < tamanho_max:
        return obter_texto_min_max(f'Respeite os intervalos! ({tamanho_min} -> {tamanho_max}) : ')
        

    

# ======= SAÍDA =======

# Imprime uma barra de loading na tela
def barra_loading(valor_atual:float, valor_final:float):
    
    while valor_atual < valor_final:
        porcentagem = (valor_atual / valor_final) * 100
        multiplicador = int(porcentagem // 10)
        total = ' ' * 10
        progresso = '#' * multiplicador
        quanto_falta = ' ' * (len(total) - len(progresso))
        return (f'[{progresso}{quanto_falta}] ({porcentagem:.2f}%)\r')


 # Escrever o texto lentamente (quando -speed, mais rápido)
def printslow(*palavras, speed = 0.04, inline = False):
    for elemento in palavras:
        for letra in elemento:
            print(letra, end='', flush=True)
            sleep(speed)
    if not inline:
        print('\n')
    
def title(txt, center = False):
    if not center:
        print('=' * (len(txt)))
        print(txt)
        print('=' * len(txt))
    else:
        print('=' * (len(txt) + 2))
        print(txt.center(len(txt) + 2))
        print('=' * (len(txt) + 2))

def centralize(txt):
    return txt.center(obter_tamanho_tela() - 2)

def printcenter(txt):
    print(centralize(txt))

def clear_screen():
    system('clear')

def enter_to_continue():
    input('<ENTER...>')
    clear_screen()

if __name__ == "__main__":
    title('io_utils')
    printslow('Olá, sou o módulo extra para as funções de entrada e saída do Python!')
    printslow('Eu não consigo rodar sozinho, para me testar, vá em algum módulo.py em que eu esteja presente!')

        


