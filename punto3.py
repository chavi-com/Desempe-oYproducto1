opcion=100

print("*****Supermercado TBK****")
print("0. Salir")
print("1. Ingresar Producto")
print("2. Mostrar Productos")
print("3. Editar Precio de un Producto")
print("4. Eliminar Producto")

productos=[]

while opcion!=0:
    producto={}
    opcion=int(input("Ingrese la opción deseada: "))

    if opcion == 1:
        producto['codigo']=input("Ingrese el código del producto: ")
        producto['nombre']=input("Ingrese el nombre del producto: ")
        producto['precio']=int(input("Ingrese el precio del producto: "))
        productos.append(producto)
    
    elif opcion == 2:
        print(productos)

    elif opcion == 3:
        productoBusqueda=input("Ingrese el código del producto que desea editar su precio: ")
        for producto in productos:
            encontrado=False
            if producto['codigo']==productoBusqueda:
                producto['precio']=int(input("Ingrese el nuevo precio del producto: "))
                encontrado=True
            
        if encontrado:
            print("¡El precio del producto fue cambiado con éxito!")
        else:
            print("El producto ingresado no existe.")
    
    elif opcion == 4:
        productoBusqueda=input("Ingrese el código del producto que desea eliminar: ")
        for producto in productos:
            encontrado=False
            eliminado={}
            if producto['codigo']==productoBusqueda:
                eliminado=producto
                productos.remove(producto)
                encontrado=True
            
        if encontrado:
            print(f"El producto {eliminado} fue eliminado con éxito.")
        else:
            print("El producto ingresado no existe.")
    
    elif opcion == 0:
        break
    else:
        print("Ingrese una opción válida.")