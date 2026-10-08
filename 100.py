# introducao input & output(Entrada e saida)
# 1. imprimir ola mundo 
print('ola mundo')
# 2 pedir nome e mostra mensagem de boas vindas
nome = input('Digite seu nome completo: ')
print('Ola seja bem vindo',nome)
# 3 pedir idade e dizer quantos anos tem
idade = int(input('Digite sua idade: '))
print('Voce tem',idade,'anos de idade')
# 4 soma de dois numero e mostra diferencia entre ambos o produto e a divisao deci,al
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite o segundo numero: '))
soma = (n1 + n2)
print('A soma e',soma)
# 5 pedir dois numero e mostra a diferencia entre ambos
diferencia = (n1 - n2)
print('Esta e a diferencia entre ambos',diferencia)
# 6 pedir dois numeros e mostrar o produto
produto = (n1 * n2)
print('Este e o produto',produto)
# 7 pedir dois numeros e mostra a divisao decimal
divisao = (n1 / n2)
print('O resultado decimal e',divisao)
# 8 pedir ano de nascimento e dizer o ano actual do usuario
ano_nascimento = int(input('Digite sua data de nascimento: '))
ano_actual = 2026
idade = ano_actual - ano_nascimento
print('Este ano voce tem',idade,'anos de idade')
# 9 Pedir comprimento e largura de um retangulo e calcular a area
comprimento = float(input('Digite o comprimento da area retangular: '))
largura = float(input('Digite a largura da area retangular: '))
area_retangular = comprimento * largura / 2
print(f"a area_retangular e : {area_retangular}")
# 10 pedir raio de um circulo e calcular a area
raio = float(input('Digite o raio do circulo: '))
area = 3.14 * raio**2
print('a area do circulo e',area)
# Variaveis e tipos de dados
# 11 criar uma variavel com o meu nome e emprimir
meu_nome = 'Marcos jose pedro'
print('Meu nome e',meu_nome)
# 12 cria variavel com idade e imprimir
minha_idade = 27
print('minha idade e',minha_idade)
# 13 converter uma string em numero inteiro
texto = '123'
numero = int(texto)
print(numero)
print(type(texto))
# 14 converter um numero inteiro em uma string
numero = 456 
Texto = numero
print(Texto)
print(type(Texto))
# 15 converter um numero em float e fazer uma operacao
n0 = 789
number = float(n0)
resultado = number + n0
print(number)
print(type(number))
print('O resultado e ',resultado)
# 16 criar duas variaveis e somar elas
b1 = int(input('Digite um numero: '))
b2 = int(input('Digite outro numero: '))
soma = b1 + b2
print('o resultado da soma e',soma)
# 17 criar duas variavel e subtrair elas
t1 = int(input('Digite um numero: '))
t2 = int(input('Digite o segundo numero: '))
subtracao = t1 - t2
print('A subtracao e',subtracao)
# 18 criar duas variaveis e multiplicalas
a1 = int(input('Digite um numero: '))
a2 = int(input('Digite o segundo numero: '))
multiplicacao = a1 * a2
print('a multiplicacao dos dois numero e',multiplicacao)
# 19 criar duas variaveis e dividilas
d1 = int(input('Digite o primeiro numero: '))
d2 = int(input('Digite o segundo numero: '))
divisao = d1 / d2
print('A divisao dos dois numero e',divisao)
# 20 Mostrar tipos de variaveis usando a funcao type(tipo)
print(type(multiplicacao))
print(type(a1))
# condicionais##
# 21 pedir um numero e dizer se ele e negativo ou positivo
m1 = int(input('Digite um numero: '))
if m1 > 0:
    print('O numero e positivo',m1)
else:
    print('o numero e negativo',m1)
# 22 pedir um numero e dizer se e par ou impar
m2 = int(input('Digite um numero: '))
if m2 % 2 == 0:
    print('o numero e par',m2)
else:
    print('O numero e impar',m2)
# 23 pedir um numero e dizer se e maior que 10
num1 = int(input('Digite um numero: '))
if num1 > 10:
    print('O numero e maior que 10',num1)
else:
    print('O numero e menor que 10',num1)
# 24 pedir dois numeros e dizer qual e o maior
y1 = int(input('Digite um numero: '))
y2 = int(input('Digite outro numero: '))
if y1 > y2:
    print('Este e o maior numero',y1)
    print('Este e o menor numero',y2)
else:
    print('Este e o maior numero',y2)
    print('Este e o menor numero',y1)
# 25 Pedir numero e dizer se e multiplo de 3
k1 = int(input('Digite um numero: '))
if k1 % 3 == 0:
    print('O numero',k1,'e multiplo de 3')
else:
    print('O numero',k1,'nao e multiplo de 3')
# 26 pedir um numero e dizer se esta entre os numeros 10 e 20
t1 = int(input('Digite um numero: '))
if t1 > 20:
    print('O numero nao esta entre 10 e 20',t1)
else:
    print('O numero esta entre 10 e 20',t1)
# 27 pedir uma letra e dizer se e vogal ou consoante
letra = input('Digite uma letra: ')
mini = letra.lower()
vogais = 'a,e,i,o,u'
if mini in vogais:
    print('E uma vogal',letra)
else:
    print('E uma consoante',letra)
# 28 pedir duas nota e dizer se a media e maior que 7
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
soma = nota1 + nota2
media = soma /2
if media >= 7:
    print('Aprovado',media)
else:
    print('Reprovado',media)
#29 pedir idade e dizer se e maior ou menor de idade
idade = int(input('Digite sua idade: '))
if idade >= 18:
    print('Este e maior de idade',idade)
else:
    print('Este e menor de idade',idade)
# 30 pedir senha e dizer se esta correta
senha = int(input('Digite a senha: '))
senha_fixa = 1234
if senha == senha_fixa:
    print('senha correta')
else:
    print('Senha incorreta')
# lacos de repeticao(for)
# 31 imprimir numeros de 1 a 10
numero = int(input('Digite um numero: '))  
for numero in range(numero,11):
    print(numero)
# 32 imprimir numeros pares de 2 a 20
comeco = 2
fim = 21
passo = 2

for i in range(comeco, fim, passo):
    print(i)
# 33 imprimir numeros impares de 1 a 19
for variavel in range(1, 20, 2):
     print(variavel)
# 34 imprimir os quadrados de 1 a 10
for numero in range(0,11):
    print(numero **2)

# 35 somar os numeros de 1 a 100
n = int(input('digite um numero: '))
for i in range(0,101):
    print(n,'+',i, '=',i+n)

# 36 somar apenas numeros pares de 1 a 50
soma = int(input('Digite um numero: '))

for numero in range(1, 51):
    if numero % 2 == 0:
        soma = soma + numero

print(soma)
# 37 pedir cinco numeros e mostrar a soma
soma = 0
for i in range(5):
    recebe = int(input('Digite um numero: '))
    soma = recebe + soma
print(soma)
# 38 pedir cinco numeros e mostrar os positivos
for i in range(5):
    positivo = int(input('Digite um numero: '))
    if positivo > 0:
        print(f'O numero e positivo,{positivo}')
# 39 pedir cinco numeros e mostrar os impares
for i in range(5):
    impar = int(input('digite um numero: '))
    if impar % 2 != 0:
        print(f'O numero e impar, {impar}')
# 40 Mostrar a tabuada dos 5
tabuada = int(input('Digite um numero: '))
for i in range(1,11):
    resultado = tabuada 
    print(f"{tabuada} x {i} = {resultado}")
# outra versao ou maneira de resolucao
n = 5
for i in range(0,11):
    print(n,'*',i,'=',n*i)
# 41 imprimir numeros de 1 a 10 usando Loop while
cont = 1
while cont <= 10:
        print(cont)
        cont = cont +1
# 42 some os numeros de 1 a 50 usando while
cont = 1
soma = 0

while cont <= 50:
    soma = soma + cont
    print(f"{soma - cont} + {cont} = {soma}")
    cont = cont + 1
print(f"A soma dos numeros de 1 a 50 e: {soma}")

# 43 Pedir numeros ate Digitar 0.
while True:
    n = int(input('Digite um numero: '))
    if n == 0:
        break
# 44 Pedir numero ate digitar 1 e somar
soma = 0
while True:
    m = int(input('Digite um numero: '))  
    if m ==1:
        break
    soma = soma + m
print(f'O resultado da soma e {soma}')
# 45 Pedir senha ate acertar
while True:
    senha = int(input('Digite a sua senha: '))
    if senha != 1234:
        print('Senha incorrreta tente novamente!s')
    else:
        print(f'login feito com sucesso.')  
        break

# 46 Mostra numeros pares de 2 a 20 usando while
cont = 2
while cont <= 20:
    print(cont)
    cont = cont + 2       
# 47 Pedir 5 numeros e calcular a media
soma = 0
for _ in range(5):
    numero = int(input('Digite um numero: '))
    soma += numero
media = soma / 5
print(f'A media dos numeros e: {media}')
# 48 mostrar tabuada de um numero
n = int(input('Digite um numero: '))
for i in range(1,   11):
    resultado = n * i
    print(f"{n} x {i} = {resultado}")
# 49 conte regressivamente de 10 a 1
for i in range(10, 0, -1):
    print(i)    
# 50 pedir um numero e mostrar os seus divisores
n = int(input('Digite um numero: '))        
print(f'Os divisores de {n} sao:')
for i in range(1, n + 1):
    if n % i == 0:
        print(i)  

# 51 cria uma lista com 5 nomes
nome = ['Marcos', 'Maria', 'Joao', 'Ana', 'Carlos']
print(nome)
# 52 cria uma lista de 1 a 5
numeros = [1, 2, 3, 4, 5]
print(numeros)
# 53 adicione um item na lista
numeros.append(6)
print(numeros)  
# 54 Remover um item da lista
numeros.remove(6)
print(numeros)
# 55 mostrar o primeiro item da lista
print(nome[0])
# 56 mostrar o ultimo item da lista de produtos
print(nome[-1])
# 57 mostrar todos os item com loop for
for nome in nome:
    print(nome)
# 58 verificar se um item esta na lista
nomes = ['Marcos', 'Maria', 'Joao', 'Ana', 'Carlos']
nome = input('Digite seu nome: ').strip().capitalize()
if nome in nomes:
    print('Este nome faz parte da minha lista') 
else:
    print('Este nome nao faz parte da minha lista ')
# 59 Contar quanto item existe na minha lista
print(len(nomes))
# 60 somar numeros da lista
print(sum(numeros))
# 61 pedir uma palavra e mostra em maiscula
palavra = 'marcos'
print(palavra.upper())
# 62 pedir uma palavra e mostra em minuscula
maiscula = 'Marcos'
print(maiscula.lower())
# 63 pedir uma frase e contar as letras
frase = 'Eu gosto de programar'
print(len(frase))
# 64 contar palavras de uma frase
print(len(frase.split()))
# 65 verificar se a frase comeca com a letra A
primeira_letra = frase [0]
if primeira_letra.upper() == 'A':
    print('sim comeca com A')
else:
    print('nao comeca com a letra A')
# 66 vereficar se a frase termina com a letra O
ultima_letra = frase [-1]
if ultima_letra.upper() == 'O':
    print('A ultima letra termina com a letra O')
else:
    print('A ultima letra nao termina com a letra O')
# 67 Substituir uma palavra em uma frase
antiga = 'vamos joga a bola'
nova_frase =antiga.replace('bola','apanhada' )
print(f' Antiga frase e: {antiga}',f' A frase substituida  e: {nova_frase}')
# 68 inverter uma string ou um texto
texto = 'Peterson'
print(texto[::-1])# este metodo de contagem regressiva chama se slicing oa fatiamento
# 69 Mostra letras uma por uma  
for letra in texto:
    print(letra)
# 70 remover espacos extras
remover = antiga
print(remover.replace(' ',''))
# 71 cria funcao que soma dois numeros
def somar_dois_numeros():
    n1 = 12
    n2 = 21

    return n1+n2 
print(somar_dois_numeros())
# 72 criar uma funcao que multiplica dois numeros
def multiplicar_dois_numeros():
    number1 = 2
    number2 = 5
    return number1*number2
print(multiplicar_dois_numeros())
# 73 funcao para calcular a media
def calcular_media():
    d1 = 5
    d2 = 7
    media = d1 + d2 / 2
    return media
print(calcular_media())
# 74 funcao verificar se e par
def par_ou_impar(n):
    if n % 2 == 0:
        return 'par'
    else:
        return 'impar'
par = (par_ou_impar(2))
# 75. Função que imprime Olá várias vezes.
def saudacao(vezes):
    for i in range(vezes):
        print('Jesus caminho verdade e vida eterna ')
    
saudacao(2)
# 76 funcao que retorna o maior numero
def maior_numero():
    numero = 1,2,3,4,5
    return max(numero),min(numero)
print(maior_numero())
# 77 funcao que retorna o menor numero  
def menor_numero():
    numero = 1,2,3,4,5
    return min(numero)
print(menor_numero())    
# 78 Função que converte Celsius para Fahrenheit.
def converter(celsius):
     fahrenheit = (celsius*9/5)+32
     return  fahrenheit
print(converter(0))
# 79. Função que soma lista.
def somar_lista():
    lista_numeros = [1000,2000,4000,900,500,700,]
    return sum(lista_numeros),max(lista_numeros),min(lista_numeros)
print(somar_lista())
# 80 funcao que retorna o maior da lista
def maior_lista():
     lista_numeros = [1000,2000,4000,900,500,700,]
     return max(lista_numeros)
print(maior_lista())
# 81 cria um dicionario com nome e idade e cidade
dic = {'Nome': 'Marcos Pedro', 'Idade':27,'Cidade': 'Luanda'}
# 82 Mostrar nome do dicionario
print(dic['Nome'])
# 83 Adicione cidade.
dic['Cidade'] = 'Nova york'
# 84 actualizar idade
dic['Idade'] = 30
# 85. Remova cidade.
dic.pop('Cidade')

# 86. Verifique chave nome.
print('Nome'in dic)
# 87. Mostre chaves
dic.keys()
print(dic)
# 88. mostrar valores
dic.values()
print(dic)
# 89 Lista de dicionario
lista_dic = [{'Nome': 'Peterson', 'Idade':27, 'Cidade': 'Benguela'}]
print(lista_dic)
# 90 Mostra nomes da lista
team = ['mendez','maria','joana','martins','miguel']
for nome in team:
    print(nome)

# 91 Pedir 5 numeros e calcular a media
def calcular_media():
    soma = 0
    for i in range(5):
        n = int(input('Digite um numero: '))
    soma = soma + n
    media = soma / 5
    return media
print(calcular_media())
# 92 contar letras em uma frase
cont = 0
frase = 'Antonio caio do pau'
for letra in frase:
    if letra != ' ':
        cont += 1
    print(cont)
# 93 mostar numeros pares de uma lista
lista_numer = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for numero in lista_numer:
    if numero %2==0:
        print(numero)
# 94 Calcular total produtos
def calcular_produtos():
    produtos = [1500,400,8000,3324,10000,]
    for numero in produtos:
     valor =  max(produtos) 
     valor = sum(produtos)
    return  valor,
print(calcular_produtos())
# 95 Tente senha 3 vezes
senha_correta = 1234
tentativa = 3
while tentativa > 0:
    senha = int(input('Digite a senha: '))
    if senha == senha_correta:
        print('Seja bem vindo')
        break
    else:
        if senha != senha_correta:
            tentativa -=1
            print('Senha incorreta','restam',tentativa,'Tentativa')
# 96 Mostrar maior numero
maior_numero = [10,20,30,40,50,60,70,80,90,]
print(max(maior_numero))
# 97 funcao que retorna impar
def impar():
    impar_numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    numeros = []
    for i in impar_numeros:
        if i % 2 == 1:
            numeros.append(i)
        
    return numeros
print(impar())
# 98 verificar palindromo
palavras = input('digite uma frase: ')
palindromo = palavras [::-1]
if palavras == palindromo:
    print('E Palindromo')
else:
    print('Nao e um palindromo')
# 99 Mostrar nomes que comecam com a Letra A
nomes = 'ana','arao', 'joana','amelia','minga','alana'
for i in nomes:
    if i[0]=='a':
        print(i)
# 100 Calcula a media e mostra aprovacao
def calcular_media():
    soma = 0
    for i in range(3):
        numero = float(input('Digite a sua nota: '))
        soma = soma + numero 
    media = soma  / 3
    if media >= 10:
        print('aprovado')
    else:
        print('reprovado')
    return media
(calcular_media())
