#Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Distância em metros '))
print(f'''{metros}m corresponde a
{metros/1000}km
{metros/100}hm
{metros/10}dam
{metros * 10:.1f}dm
{metros*100:.1f}cm
{metros*1000:.1f}mm''')