frutas = []

for i in range(10):
    fruta={}
    fruta['nombre']=input(f"Ingrese el nombre de la fruta {i+1}: ")
    fruta['color']=input(f"Ingrese el color de la fruta {i+1}: ")
    fruta['precio']=input(f"Ingrese el precio de la fruta {i+1}: ")
    frutas.append(fruta)

print(f'Orden original: {frutas}')

inversoFrutas=list(reversed(frutas))

print(f'Orden inverso: {inversoFrutas}')