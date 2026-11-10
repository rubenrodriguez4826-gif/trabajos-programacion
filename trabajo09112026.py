LIMITE = 2_000_000
 
# es_primo[i] es True si i es primo
es_primo = [True] * LIMITE
es_primo[0] = es_primo[1] = False
 
# Criba de Eratóstenes
for i in range(2, int(LIMITE ** 0.5) + 1):
    if es_primo[i]:
        for j in range(i * i, LIMITE, i):
            es_primo[j] = False
 
# Imprimir y sumar
suma = 0
cantidad = 0
 
for i in range(2, LIMITE):
    if es_primo[i]:
        print(i)
        suma += i
        cantidad += 1
 
print()
print("Cantidad de primos:", cantidad)
print("Suma:", suma)
 