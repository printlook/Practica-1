class Auto:
    def __init__(self, placa, marca, modelo, descripcion, precio_unitario):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.descripcion = descripcion
        self.precio_unitario = precio_unitario

class Cliente:
    def __init__(self, nombre, correo_electronico, nit):
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.nit = nit

class Compra:
    def __init__(self, id, cliente):
        self.id = id
        self.cliente = cliente
        self.lista_autos = []
        self.costo_total = 0.0

    def agregar_auto(self, auto, agregar_seguro=False):
        self.lista_autos.append(auto)
        costo_auto = auto.precio_unitario
        if agregar_seguro:
            costo_auto += 0.15 * auto.precio_unitario
        self.costo_total += costo_auto

    def generar_factura(self):
        factura = f"Factura ID: {self.id}\nCliente: {self.cliente.nombre} (NIT: {self.cliente.nit})\n"
        factura += "Autos Comprados:\n"
        for auto in self.lista_autos:
            factura += f"{auto.placa} - {auto.marca} {auto.modelo} - Q{auto.precio_unitario:.2f}\n"
        factura += f"Costo Total: Q{self.costo_total:.2f}\n"
        return factura

autos_registrados = {}
clientes_registrados = {}
compras_realizadas = []
id_compra = 1

def registrar_auto():
    placa = input("Ingrese la placa del auto: ")
    marca = input("Ingrese la marca del auto: ")
    modelo = input("Ingrese el modelo del auto: ")
    descripcion = input("Ingrese una descripción del auto: ")
    precio_unitario = float(input("Ingrese el precio unitario del auto: "))
    
    auto = Auto(placa, marca, modelo, descripcion, precio_unitario)
    autos_registrados[placa] = auto
    print(f"Auto {placa} registrado exitosamente.\n")

def registrar_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    correo_electronico = input("Ingrese el correo electrónico del cliente: ")
    nit = input("Ingrese el NIT del cliente: ")
    
    cliente = Cliente(nombre, correo_electronico, nit)
    clientes_registrados[nit] = cliente
    print(f"Cliente {nit} registrado exitosamente.\n")

def realizar_compra():
    global id_compra
    nit_cliente = input("Ingrese el NIT del cliente: ")
    
    if nit_cliente not in clientes_registrados:
        print("Cliente no registrado.")
        return
    
    cliente = clientes_registrados[nit_cliente]
    compra = Compra(id_compra, cliente)
    
    while True:
        print("1. Agregar Auto")
        print("2. Terminar Compra y Facturar")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            placa_auto = input("Ingrese la placa del auto: ")
            if placa_auto in autos_registrados:
                agregar_seguro = input("¿Desea agregar seguro al auto? (si/no): ").lower() == "si"
                compra.agregar_auto(autos_registrados[placa_auto], agregar_seguro)
            else:
                print("Auto no registrado.")
        elif opcion == "2":
            compras_realizadas.append(compra)
            print(compra.generar_factura())
            id_compra += 1
            break
        else:
            print("Opción no válida.")

def reporte_compras():
    print("------------- REPORTE DE COMPRAS -------------")
    total_general = 0
    for compra in compras_realizadas:
        print(f"CLIENTE:\nNombre: {compra.cliente.nombre}\nCorreo electrónico: {compra.cliente.correo_electronico}\nNIT: {compra.cliente.nit}")
        print("AUTO(S) ADQUIRIDO(S):")
        for auto in compra.lista_autos:
            print(f"{auto.placa} - {auto.marca} {auto.modelo} - Q{auto.precio_unitario:.2f}")
        print(f"TOTAL: Q{compra.costo_total:.2f}")
        print("==============================================")
        total_general += compra.costo_total
    print(f"Total General: Q{total_general:.2f}")
    print("---------------------------------------------")

def datos_estudiante():
    print("Nombre del estudiante: Pablo Isai Matusalen Cutzal Mazariegos ")
    print("Carnet: 202209622\n")

def menu_principal():
    while True:
        print("------------- Menú Principal -------------")
        print("1. Registrar Auto")
        print("2. Registrar Cliente")
        print("3. Realizar Compra")
        print("4. Reporte de Compras")
        print("5. Datos del Estudiante")
        print("6. Salir")
        print("------------------------------------------")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_auto()
        elif opcion == "2":
            registrar_cliente()
        elif opcion == "3":
            realizar_compra()
        elif opcion == "4":
            reporte_compras()
        elif opcion == "5":
            datos_estudiante()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.\n")

if __name__ == "__main__":
    menu_principal()
