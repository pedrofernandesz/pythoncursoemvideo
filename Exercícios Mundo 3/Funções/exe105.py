'''Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

OBS: Sem usar funções built-in comoi max(), min(), sum()

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.'''

def notas(*num, situation=False):
    """
    -> Analisa a nota de x alunos, joga em um dicionário e mostra a situação
    :param num: recebe vários números
    :param situation: caso True, adciona na lista a situação do aluno
    :return: dicionário com dados de menor nota, maior nota, média e situação 

    """
    import math
    dados = {}
    maior = menor = s = 0
    for i ,n in enumerate(num):
        s += n
        if i <= 1:
            maior = n
            menor = n
        else:
            if n > maior:
                maior = n
            elif n < menor:
                menor = n
        dados['maior'] = maior
        dados['menor'] = menor
        dados['media'] = math.trunc(s/len(num))
        if situation:
            if s/len(num) < 6:
                dados['sit'] = 'Reprovado'
            else:
                dados['sit'] = 'Aprovado'
    return dados

help(notas)