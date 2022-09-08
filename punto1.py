cantidad = int(input("defina una cantidad de numeros a ingresar: "))

multiplos2 = 0
multiplos3 = 0

for i in range(cantidad):
    numero=int(input("dijite un numero entero"))

    if numero%2==0:
        multiplos2=multiplos2+1

    if numero%3==0:
        multiplos3=multiplos3+1
print(f"la cantidad de multiplos de 2 fue {multiplos2} ")
print(f"la cantidad de multiplos de 3 fue {multiplos3} ")
                       

