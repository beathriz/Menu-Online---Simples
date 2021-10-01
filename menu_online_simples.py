# Passo a passo menu online simples

print('Menu online\n\n'
      'Para começar escolha:')


print('1 - Entradas\n' 
      '2 - Prato Principal\n'
      '3 - Bebidas\n')

opcao = input('Digite a opção desejada 1, 2 ou 3: ')

if opcao == '1':
      print ('1.1 - Sopa de legumes\n''1.2 - Torradas com geleia\n''1.3 - Prato de frios\n')
elif opcao == '2':
      print ('2.1 - Picanha\n''2.2 - Contra Filé\n' '2.3 - Peixe e frutos do mar\n')
elif opcao == '3':
      print ('3.1 - Refrigerante\n''3.2 - Suco Laranja\n''3.3 - Cerveja\n')
else:
      print ('Por favor, digite uma opção válida.')