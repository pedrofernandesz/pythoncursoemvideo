#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

tempc = float(input('Temperatura em c°: '))
tempf = 9 * tempc /5 + 32
print(f'{tempc}°C equivale ao mesmo que {tempf}°F')