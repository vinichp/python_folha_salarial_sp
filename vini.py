import csv

arquivo = open('remuneracao.txt')

#pessoas = csv.DictReader(arquivo)
valorMaior = int(0)
nomeMaior = ''
profMaior = ''
linha = arquivo.readline()
for linha in arquivo:
	valor = linha.split(';')
	valorFormatado = int(valor[10].split()[0].replace(',', ''))
	#print(valorFormatado)
	if(valorFormatado > valorMaior):
		#print('eh maior')
		valorMaior = valorFormatado
		nomeMaior = valor[0]
		profMaior = valor[1]
		
print(valor[0])
print(valor[1])
print(valor[10])
print("Maior salario liquido = " , valorMaior)
print(nomeMaior)
print(profMaior)
#print(pessoas)
#for pessoa in pessoas:
#for key in pessoas:
#    print(key, ' : ')
#print(pessoa["REDUTOR SALARIAL"])
#    print("Nome:", pessoa["nome"], " - Idade:", pessoa["idade"], " - Email:", pessoa["email"])