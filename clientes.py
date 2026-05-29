import re

clientes = []


# --- CLASES Y VALIDACIONES EXIGIDAS POR LOS TESTS ---
class Cliente:
    """Representa a un cliente del sistema con sus datos de contacto"""
    def __init__(self, nombre, email, telefono=""):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def es_valido(self):
        return validar_nombre(self.nombre) and validar_email(self.email)


def validar_nombre(nombre):
    """Comprueba si el nombre introducido es válido y no está vacío.

    Args:
        nombre: Texto con el nombre del cliente.

    Returns:
        True si es válido, False si está vacío.
    """
    if nombre is None or nombre.strip() == "":
        return False
    return True


def validar_email(email):
    """Verifica si el correo electrónico tiene un formato correcto.

    Args:
        email: Texto con el correo electrónico.

    Returns:
        True si el formato es correcto, False en caso contrario.
    """
    patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if email is None or not re.match(patron, email):
        return False
    return True


# --- TU CÓDIGO ORIGINAL ---
def menu_clientes():
    terminar = False
    while terminar == False:
        print("\n--- CLIENTES ---")
        print("1. Añadir cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Volver")
        op = input("Opción: ")

        if op == "1":
            crear_cliente()
        elif op == "2":
            listar_clientes()
        elif op == "3":
            buscar_cliente()
        elif op == "4":
            terminar = True
        else:
            print("No existe esa opción")


def crear_cliente():
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")

    if nombre == "":
        print("El nombre no puede estar vacío")
    else:
        cliente = {"nombre": nombre, "telefono": telefono, "email": email}
        clientes.append(cliente)
        print("Cliente añadido")


def listar_clientes():
    print("\nLISTADO DE CLIENTES")
    if len(clientes) == 0:
        print("No hay clientes")
    else:
        i = 0
        while i < len(clientes):
            c = clientes[i]
            print(str(i + 1) + ". " + c["nombre"] + " - " + c["telefono"] + " - " + c["email"])
            i = i + 1


def buscar_cliente():
    texto = input("Texto a buscar: ")
    encontrado = False
    for c in clientes:
        if texto.lower() in c["nombre"].lower() or texto in c["telefono"] or texto.lower() in c["email"].lower():
            print(c["nombre"] + " - " + c["telefono"] + " - " + c["email"])
            encontrado = True
    if encontrado == False:
        print("No se encontraron clientes")