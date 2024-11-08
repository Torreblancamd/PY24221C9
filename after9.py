

opcion = ""
lista_de_productos = [{"nombre":"Lampara","stock":30},
                      {"nombre":"Mouse","stock":5},
                      {"nombre":"Camara Web","stock":10} ]

while opcion != "4":
    print("Bienvenido/a al sistema E-Mart")
    opcion = input("Ingrese la opcion: 1) Agregar producto 2) Mostrar lista de productos 3)Eliminar Producto 4) Salir")

    if opcion == "1":
        nombre_producto = input("Ingrese el nombre del producto")
        cantidad = int(input("Ingrese el stock"))
        datos_producto = {"nombre":nombre_producto, "stock":cantidad}
        lista_de_productos.append(datos_producto)
    elif opcion == "2":
        print("Lista de productos")
        print("")
        for producto in lista_de_productos:
            print("")
            print("<---Producto--->")
            print("Nombre: ", producto["nombre"] )
            print("Nombre: ", producto["stock"] )
            print("")
    elif opcion == "4":
        print("Gracias por visitarnos")
    else:
        print("OPCION NO ENCONTRADA")