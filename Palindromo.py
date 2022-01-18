'''igual, aux = 0, 0
texto = input('Ingrese la palabra que desea evaluar: ')

for cont in reversed(range(0, len(texto))):
  if texto[cont].lower() == texto[aux].lower():
    igual += 1
  aux += 1
if len(texto) == igual:
  print("El texto ES Palindromo")
else:
  print("El texto ingresado NO es Palindromo")'''


palabra = input('Ingrese una palabra: ')

alreves=palabra[::-1]

if alreves == palabra:
    print(palabra, 'ES un Palindromo')
else:
    print(palabra, 'NO es un Palindromo')