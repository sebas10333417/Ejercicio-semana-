print("!!!Bienvenido al Menú!!!")
#se crea una lista vacia en la cual se almacenaran datos
productos = []
continuar = True
# Se utiliza el el bucle white que permitira crear un ciclo para ingresar nuevos productos
while continuar:
# Se crean cariables en las cuales se le pide al usuario ingresar ciertos datos que se requieren para agregar a la lista
    print("\nPor favor ingresa los siguientes datos:")
    producto = input("Nombre del producto: ")
    cantidad = int(input("Cantidad del producto: "))
    precio_unitario = float(input("Precio unitario del producto: "))
    descuento = float(input("Descuento en % (ej. 10 para 10%): "))
# Se crean variable las cuales se utilizan para generar la operacion que nos indica cual es el valor unitario + la suta total y el descuento
    subtotal = precio_unitario * cantidad
    monto_descuento = subtotal * (descuento / 100)
    total_con_descuento = subtotal - monto_descuento
# Se cra un diccionario el cual permite mantener un orden y permite acceder dinamicamente
    producto_info = {
        "nombre": producto,
        "cantidad": cantidad,
        "precio_unitario": precio_unitario,
        "descuento": descuento,
        "subtotal": subtotal,
        "descuento_aplicado": monto_descuento,
        "total_con_descuento": total_con_descuento
    }

    productos.append(producto_info)
# Se cierra el bucle white con la condicion N si no desea regitrar mas productos
    salir = input("¿Deseas registrar más productos? (N para salir): ").lower()
    if salir == "n":
        continuar = False

# Se muestra el resumen de la compra
print("\n--- Resumen de la compra ---")
total_final = 0
total_descuentos = 0
# Se utiliza el bucle for para recorrer el diccionario y imprima los datos solicitados
for p in productos:
    print(f"\nProducto: {p['nombre']}")
    print(f"Cantidad: {p['cantidad']}")
    print(f"Precio unitario: ${p['precio_unitario']:.2f}")
    print(f"Subtotal: ${p['subtotal']:.2f}")
    print(f"Descuento: {p['descuento']}% -> ${p['descuento_aplicado']:.2f}")
    print(f"Total con descuento: ${p['total_con_descuento']:.2f}")

    total_final += p['total_con_descuento']
    total_descuentos += p['descuento_aplicado']
# Se muestra resumen de descuento
print("\n----------------------------")
print(f"Total de descuentos aplicados: ${total_descuentos:.2f}")
print(f"Total a pagar: ${total_final:.2f}")