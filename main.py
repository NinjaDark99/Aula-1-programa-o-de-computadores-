def soma(a, b):
    return a + b
    
n1 = 5
n2 = 3
r = soma(n1, n2)

print(f"{n1} + {n2} = {r}")
   
def funcao(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"
    
numero = 8
resutado = funcao(numero)
print(resutado)


numeros = [10, 20, 30, 40, 50]
maior_numero = numeros[0]
for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero

print(maior_numero)

tabuada = 5
for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)))

soma = sum(range(1, 101))
print(soma)

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
    
numero = 10
resultado = fatorial(numero)
print(f"O fatorial de {numero} é {resultado}")

contagem = 11
for count in range(11):
    print("%d" % (contagem-(count+1)))