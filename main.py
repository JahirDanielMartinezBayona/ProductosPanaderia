#---  Categoria ---
#1) Pan Barra o Pistola
panBarraPistola = list([{"Nombre": "PAN BLANCO", "cuesta":3200}, 
{"Nombre": "PAN CANDEAL", "cuesta":2800}, 
{"Nombre": "PAN RÚSTICO", "cuesta":3500}])

promocionPanBarraPistola = list([
           {"Codigo": 4, "descuento": "Descuento A", "valor":0.2}, 
           {"Codigo": 8, "descuento": "Descuento B", "valor":0.15},
        ])
#2) Pan Integral
panIntegral = list([
           {"Nombre": "MULTICEREALES", "cuesta":2500},
           {"Nombre": "TRIGO BLANCO", "cuesta":2800},
           {"Nombre": "NUECES Y PASAS", "cuesta":5000},
           {"Nombre": "AVENA Y MIEL", "cuesta":4800},
           {"Nombre": "SALVADO", "cuesta":4200},
        ])
promocionPanIntegral = list([
           {"Codigo": 1, "descuento": "Descuento C", "valor":0.18},
           {"Codigo": 4, "descuento": "Descuento D", "valor":0.2}, 
        ])
#3) ESPECIALES O GOURMET
panEspecialesGourmet = list([
           {"Nombre": "BAGUETTE PARISIENNE", "cuesta":14000},
           {"Nombre": "BATARD", "cuesta":12000},
           {"Nombre": "MANTOU", "cuesta":9000},
           {"Nombre": "MOGOLLÓN DE SEMILLAS POR FUERA", "cuesta":10000},
           {"Nombre": "DE CÚRCUMA Y PIPAS DE CALABAZA", "cuesta":12000},
          ])

promocionPanEspecialesGourmet = list([
           {"Codigo": 7, "descuento": "Descuento E", "valor":0.1},
           {"Codigo": 9, "descuento": "Descuento F", "valor":0.25}, 
        ])

menuGeneral=dict({
    "BARRA O PISTOLA":{
        "Producto":panBarraPistola,
        "Promociones":promocionPanBarraPistola,
    },
    "INTEGRAL":{
        "Producto":panIntegral,
        "Promociones":promocionPanIntegral,
    },
    "ESPECIALES O GOURMET":{
        "Producto":panEspecialesGourmet,
          "Promociones":promocionPanEspecialesGourmet,
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