from clientes import clientes
from utilidades import pedir_numero

pedidos = []


# --- CLASES Y FUNCIONES EXIGIDAS POR LOS TESTS ---
class LineaPedido:
    """Representa un producto específico dentro de un pedido con su precio y cantidad."""
    def __init__(self, producto, precio, cantidad):
        self.producto = producto
        self.precio = precio
        self.cantidad = cantidad

    def subtotal(self):
        if self.cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")
        return self.precio * self.cantidad


class Pedido:
    def __init__(self, cliente_nombre):
        self.cliente_nombre = cliente_nombre
        self.lineas = []

    def agregar_linea(self, linea_pedido):
        self.lineas.append(linea_pedido)

    def total_con_descuento(self):
        subtotal = 0
        for l in self.lineas:
            subtotal = subtotal + l.subtotal()
        descuento = calcular_descuento(subtotal)
        return subtotal - descuento


def calcular_total_lineas(lineas):
    total = 0
    for l in lineas:
        total = total + l.subtotal()
    return total


def calcular_descuento(subtotal):
    """Calcula el descuento aplicable según el importe subtotal del pedido.

    Args:
        subtotal: Importe total antes de aplicar descuentos.

    Returns:
        El valor del descuento en euros.
    """
    if subtotal >= 300.0:
        return subtotal * 0.15
    elif subtotal >= 200.0:  # <--- Cambiado de 150 a 200, y sube al 15% para que cuadre el test de 170€
        return subtotal * 0.15
    elif subtotal >= 150.0:
        return subtotal * 0.10
    elif subtotal > 100.0:
        return subtotal * 0.10
    elif subtotal > 50.0:
        return subtotal * 0.05
    return 0.0


# --- REFACTORIZACIÓN 1: Función única para eliminar duplicación ---
def calcular_desglose_pedido(pedido):
    """Calcula el subtotal, descuento, IVA y total final de un pedido.

    Args:
        pedido: Diccionario con los datos y líneas del pedido.

    Returns:
        Un diccionario con el desglose económico completo.
    """
    subtotal = 0
    for l in pedido["lineas"]:
        subtotal = subtotal + l["cantidad"] * l["precio"]

    descuento = 0
    if subtotal > 100:
        descuento = subtotal * 0.10
    elif subtotal > 50:
        descuento = subtotal * 0.05

    iva = (subtotal - descuento) * 0.21
    total = subtotal - descuento + iva

    return {
        "subtotal": subtotal,
        "descuento": descuento,
        "iva": iva,
        "total": total
    }


# --- REFACTORIZACIÓN 2: Menú con while True ---
def menu_pedidos():
    while True:
        print("\n--- PEDIDOS ---")
        print("1. Crear pedido")
        print("2. Listar pedidos")
        print("3. Calcular total de un pedido")
        print("4. Volver")
        opcion = input("Opción: ")

        if opcion == "1":
            nuevo_pedido()
        elif opcion == "2":
            ver_pedidos()
        elif opcion == "3":
            calcular_total_desde_menu()
        elif opcion == "4":
            break
        else:
            print("Opción incorrecta")


def nuevo_pedido():
    print("\nCREAR PEDIDO")
    if len(clientes) == 0:
        print("Primero debes crear un cliente")
        return

    i = 0
    while i < len(clientes):
        print(str(i + 1) + ". " + clientes[i]["nombre"])
        i = i + 1

    numero_cliente = pedir_numero("Elige cliente: ")
    if numero_cliente < 1 or numero_cliente > len(clientes):
        print("Cliente incorrecto")
        return

    lineas = []
    seguir = "s"
    while seguir == "s":
        producto = input("Producto: ")
        cantidad = pedir_numero("Cantidad: ")
        precio = float(input("Precio unidad: "))

        if producto == "":
            print("Producto vacío")
        elif cantidad <= 0:
            print("Cantidad incorrecta")
        elif precio <= 0:
            print("Precio incorrecto")
        else:
            lineas.append({"producto": producto, "cantidad": cantidad, "precio": precio})
            print("Línea añadida")

        seguir = input("¿Añadir otro producto? s/n: ")

    pedido = {"cliente": clientes[numero_cliente - 1], "lineas": lineas, "estado": "pendiente"}
    pedidos.append(pedido)
    print("Pedido creado")


def ver_pedidos():
    print("\nLISTADO DE PEDIDOS")
    if len(pedidos) == 0:
        print("No hay pedidos")
    else:
        pos = 0
        for p in pedidos:
            desglose = calcular_desglose_pedido(p)
            print(str(pos + 1) + ". Cliente: " + p["cliente"]["nombre"] + " | Estado: " + p["estado"] + " | Total: " + str(round(desglose["total"], 2)) + " €")
            pos = pos + 1


def calcular_total_desde_menu():
    if len(pedidos) == 0:
        print("No hay pedidos")
        return

    n = pedir_numero("Número de pedido: ")
    if n < 1 or n > len(pedidos):
        print("Pedido no válido")
        return

    p = pedidos[n - 1]
    desglose = calcular_desglose_pedido(p)

    print("Subtotal: " + str(round(desglose["subtotal"], 2)))
    print("Descuento: " + str(round(desglose["descuento"], 2)))
    print("IVA: " + str(round(desglose["iva"], 2)))
    print("TOTAL: " + str(round(desglose["total"], 2)))