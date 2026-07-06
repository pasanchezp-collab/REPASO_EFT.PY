
productos_list = []



def validar_inventario(inventario):
    if not inventario >= 0:
        print("ERROR, CANTIDAD DEBE SER MAYOR A 0")
        return False

    return True


def validar_disponible(disponible):
    if not disponible in ["SI", "NO"]:
        print("ERROR, EL CARACTER INGRESADO DEBE SER SI O NO")
        return False

    return True


def validar_precio(precio):
    if not precio > 0:
        print("ERROR, EL PRECIO DEBE SER MAYOR A 0")
        return False

    return True


def validar_texto(texto):
    if len(texto.strip()) == 0:
        print("ERROR, DEBE INGRESAR DATOS PARA CONTINUAR")
        return False

    if " " in texto:
        print("ERROR, EL TEXTO INGRESADO NO PUEDE CONTENER ESPACIOS")
        return False

    return True


def validar_codigo(codigo):
    for producto in productos_list:
        if producto["codigo"] == codigo:
            print("ERROR, EL CODIGO YA ESTA INGRESADO")
            return False

    if len(codigo.strip()) == 0:
        print("ERROR, DEBE INGRESAR DATOS PARA PODER CONTINUAR")
        return False

    return True


def imprimir_producto(producto):
    disponible = "Disponible" if producto["disponible"] == True else "No-Disponible"
    print(f"""
=========Producto========
Nombre: {producto["nombre"]}
Categoria: {producto["categoria"]}
Precio: ${producto["precio"]}
Disponible: {disponible}
=========================""")


def imprimir_inventario(producto):
    print(
        f"Codigo: {producto["codigo"]} [Stock:{producto["stock"]} / Vendidos:{producto["vendidos"]}]"
    )

    def stock_por_categoria():
    if (len(productos_list)) == 0:
        print("ERROR, NO EXISTEN DATOS REGISTRADOS HASTA EL MOMENTO")
    else:
        print("\n === STOCK ===")
        categoria = str(input("Ingrese [Categoria] del producto: ")).strip().upper()
        while not validar_texto(categoria):
            categoria = str(input("Ingrese [Categoria] del producto: ")).strip().upper()
        bandera_stock = False
        for producto in productos_list:
            if producto["categoria"] == categoria:
                bandera_stock = True
                imprimir_inventario(producto)
        if bandera_stock == False:
            print(f"NO EXISTEN REGISTROS DE CATEGORIA: {categoria}-")


def buscar_por_precio():
    if (len(productos_list)) == 0:
        print("NO EXISTEN REGISTROS POR EL MOMENTO")
    else:
        print("\n === Busqueda por rango de precios ===")
        while True:
            try:
                min = int(input("Rango minimo para buscar: "))
                while not validar_precio(min):
                    min = int(input("Rango minimo para buscar: "))
                break
            except:
                print("ERROR, RANGO MINIMO DEBE SER UN NUMERO")
        while True:
            try:
                max = int(input("Rango maximo para buscar: "))
                while not validar_precio(max):
                    max = int(input("Rango maximo para buscar: "))
                break
            except:
                print("ERROR, EL MAXIMO INGRESADO DEBE SER UN NUMERO")
        flag_rango_precios = False
        for producto in productos_list:
            if min <= producto["precio"] <= max:
                flag_rango_precios == True
                imprimir_producto(producto)
        if flag_rango_precios == False:
            print("NO EXISTE PRODUCTO EN ESTE RANGO DE PRECIO")


def actualizar_precio():
    if (len(productos_list)) == 0:
        print("NO EXISTE REGISTRO DE DATOS HASTA EL MOMENTO")
    else:
        print("\n === ACTUALIZAR PRECIO DE LOS PRODUCTOS ===")
        codigo = str(input("Ingrese codigo del producto: ")).strip().upper()
        while not validar_codigo(codigo):
            codigo = str(input("Ingrese codigo del producto: ")).strip().upper()
        flag_actualizar_precio = False
        for producto in productos_list:
            if producto["codigo"] == codigo:
                flag_actualizar_precio = True
                while True:
                    try:
                        precio = int(input("Ingrese nuevo $Valor del producto: "))
                        while not validar_precio(precio):
                            precio = int(input("Ingrese nuevo $Valor del producto: "))
                        break
                    except:
                        print("ERROR, EL VALOR INGRESADO DEBE SER UN NUMERO")
                producto["precio"] = precio
        if flag_actualizar_precio == False:
            print(f"NO EXISTE REGISTRO DE ESTE CODIGO: {codigo}")


def agregar_producto():
    print("\n === AGREGAR PRODUCTOS POR CODIGO ===")
    codigo = str(input("Ingrese codigo del producto: ")).strip().upper()
    while not validar_codigo(codigo):
        codigo = str(input("Ingrese codigo de producto: ")).strip().upper()
    nombre = str(input("Ingrese Nombre del producto: ")).strip().upper()
    while not validar_texto(nombre):
        nombre = str(input("Ingrese Nombre del producto: ")).strip().upper()
    categoria = str(input("Ingrese [Categoria] del producto: ")).strip().upper()
    while not validar_texto(categoria):
        categoria = str(input("Ingrese [Categoria] del producto: ")).strip().upper()
    while True:
        try:
            precio = int(input("Ingrese $valor del producto: "))
            while not validar_precio(precio):
                precio = int(input("Ingrese $valor del producto: "))
            break
        except:
            print("ERROR, EL PRECIO DEBE SER UN NUMERO")
    disponible = str(input("""
¿Producto disponible?
        Si/No: """)).strip().upper()
    while not validar_disponible(disponible):
        disponible = str(input("""
¿Producto disponible?
        Si/No: """)).strip().upper()
    esta_disponible = True if disponible == "SI" else False
    while True:
        try:
            stock = int(input("Ingrese [STOCK] de producto: "))
            while not validar_inventario(stock):
                stock = int(input("Ingrese [STOCK] de producto: "))
            break
        except:
            print("ERROR, EL STOCK INGRESADO DEBE SER UN NUMERO")
    while True:
        try:
            vendidos = int(input("Ingrese la cantidad vendida: "))
            while not validar_inventario(vendidos):
                vendidos = int(input("Ingrese la cantidad vendida: "))
            break
        except:
            print("ERROR, LA CANTIDAD VENDIDA DEBE SER VALIDA ")
    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "disponible": esta_disponible,
        "stock": stock,
        "vendidos": vendidos,
    }

    productos_list.append(producto)
    print("...EL PRODUCTO HA SIDO AGREGADO EXITOSAMENTE...")

def eliminar_producto():
    if (len(productos_list)) == 0:
        print("NO HAY DATOS REGISTRADOS POR EL MOMENTO")
    else:
        print("=== PRODUCTOS A ELIMINAR ===")
        codigo = str(input("Ingrese el codigo del producto que desea eliminar: ")).strip().upper()
        while not validar_codigo(codigo):
            codigo = (
                str(input("Ingrese el codigo del producto que desea eliminar: ")).strip().upper()
            )
        flag_eliminar = False
        for producto in productos_list:
            if producto["codigo"] == codigo:
                flag_eliminar = True
                productos_list.remove(producto)
                print(f"¡¡...Producto: {codigo} eliminado exitosamente...!!")
        if flag_eliminar == False:
            print(f"NO EXISTE REGISTRO PARA ESTE CODIGO: {codigo}")

def mostrar_productos():
    if (len(productos_list)) == 0:
        print("NO EXISTE REGISTRO DE ESTE PRODUCTO")
    else:
        print("=== LISTADO DE PRODUCTOS ===")
        for producto in productos_list:
            imprimir_producto(producto)


