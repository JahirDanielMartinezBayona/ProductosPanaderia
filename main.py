menuGeneral=dict({
    "PANES":{
        "Producto":list([
           {"Nombre": "PAN BLANCO", "cuesta":3200}, 
           {"Nombre": "PAN INTEGRAL", "cuesta":2800}, 
           {"Nombre": "PAN DE CENTENO", "cuesta":3500}, 
           {"Nombre": "PAN DE OLIVA", "cuesta":4500},
           {"Nombre": "PAN DE MAIZ", "cuesta":5500}, 
           {"Nombre": "PAN ARABE", "cuesta":5000}, 
           {"Nombre": "PAN ESPELTA", "cuesta":5700}, 
        ]),
        "Promociones":list([
           {"Codigo": 4, "descuento": "Descuento A", "valor":0.2}, 
           {"Codigo": 8, "descuento": "Descuento B", "valor":0.15},
        ]),
    },
    "BOLLERIA":{
        "Producto":list([
           {"Nombre": "DONAS", "cuesta":2500},
           {"Nombre": "CROAISSANTS", "cuesta":2800},
           {"Nombre": "TARTEL", "cuesta":5000},
           {"Nombre": "MARAÑUELA", "cuesta":4800},
           {"Nombre": "CONSAIMADA", "cuesta":4200},
        ]),
        "Promociones":list([
           {"Codigo": 1, "descuento": "Descuento C", "valor":0.18},
           {"Codigo": 4, "descuento": "Descuento D", "valor":0.2}, 
        ]),
    },
    "TARTAS":{
        "Producto":list([
           {"Nombre": "TARTA MOUSSE DE CHOCOLATE", "cuesta":14000},
           {"Nombre": "TARTA DE FRESA", "cuesta":12000},
           {"Nombre": "CHEESECAKE DE JENGIBRE", "cuesta":9000},
           {"Nombre": "TARTA ARABE", "cuesta":10000},
           {"Nombre": "TARTA DE PERAS", "cuesta":12000},
          ]),
          "Promociones":list([
           {"Codigo": 7, "descuento": "Descuento E", "valor":0.1},
           {"Codigo": 9, "descuento": "Descuento F", "valor":0.25}, 
        ]),
    },
})
print("BIENVENIDO A ENJOYBREAD, LA PANADERÍA NÚMERO UNO EN SABOR DE LEVADURA")
print ("Nuestro menu: ")
listaMenu=list(menuGeneral.keys())
for posicionIndice, valorCategoria in enumerate(menuGeneral.keys()):
    print(f"{posicionIndice}. {valorCategoria}")
opcionSeleccionarCategoria=int(input())
datosContenido=menuGeneral.get(listaMenu[opcionSeleccionarCategoria])
productosRecibirDetalle=datosContenido.get("Producto")

#seleccion del producto
print (f"Seleccione el producto de acuerdo a la categoria {listaMenu[opcionSeleccionarCategoria]} en la que desea comprar: ")
for posicionProductosRecibirDetalle, valorProductosRecibirDetalle in enumerate(productosRecibirDetalle):
    name=valorProductosRecibirDetalle["Nombre"]
    value=valorProductosRecibirDetalle["cuesta"]
    print(f"{posicionProductosRecibirDetalle} {name} con precio de ${value}")
opcionProductos=int(input())
mostrarn = productosRecibirDetalle[opcionProductos].get("Nombre")
mostrarp= productosRecibirDetalle[opcionProductos].get("cuesta")
promociones=datosContenido["Promociones"]

#seleccionar unidades del producto
print ("¿Cuantas unidades deseas comprar?")
cantidad=int(input())
promocion=list()
for valor in promociones:
    if (valor.get("Codigo") == opcionProductos):
            promocion.append(valor)
descuento=valor["descuento"]
precioAValer=valor["valor"]
descuentoProducto=int(precioAValer*100)
mul=mostrarp*cantidad
precioA=mul * precioAValer
precioB=mul - precioA
#estado de las promociones
if (len(promocion)== 0):
    print (f"No hay promociones disponibles para {mostrarn}")
    print ("VALOR A PAGAR : $",mul)
else:
    print(f"El producto {mostrarn} tiene {descuento} del",descuentoProducto,"% de descuento")
    print()
    print ("¿Desea adquirir el descuento? Ingrese (1) para SI o ingrese (2) para NO")
    decdes=int(input())
    if decdes==1:
      print("Valor regular: $",mul)
      print("VALOR A PAGAR CON DESCUENTO: $",int(precioB))
      mul=int(precioB)
    else:
      print("VALOR A PAGAR: $",mul)
#estado del dinero a pagar
dineroPagar=int(input ("Ingrese la cantidad a pagar $"))
cambioConclusion=dineroPagar-mul
if dineroPagar>=mul:
     print("Su cambio es $",cambioConclusion)
else:
    print(f"Su dinero no alcanza, le faltan $ {-cambioConclusion}")