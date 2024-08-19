
class Auto:
     def __init__(self, placa, marca, modelo, descripcion, precioUnitario):
         self.placa = placa
         self.marca = marca
         self.modelo = modelo
         self.descripcin = descripcion
         self.precioUnitario = precioUnitario

class Cliente:
    def __init__(self, nombre, correoElectronico, Nit):
        self.nombre = nombre
        self.correoElectronico = correoElectronico
        self.Nit = Nit
        self.carros_comprados = []

class Compra:
    def __init__(self, listaProductos, cliente, Id, CostoTotal):
        self.listaProductos = listaProductos
        self.cliente = cliente
        self.Id = Id
        self.CostoTotal = CostoTotal

autos_registrados = []
clientes_registrados = []
compras_realizadas = []

def registrar_auto():
    placa = input('Ingrese la Placa: ')
    marca = input('Ingrese la marca: ')
    modelo = input('Ingrese la modelo: ')
    descripcion = input('Ingrese la descripcion: ')
    precioUnitario = int(input('Ingrese la preciounitario: '))
    auto = Auto(placa, marca, modelo, descripcion, precioUnitario)
    autos_registrados.append(auto)
    print("")
    print(f'auto {marca} {modelo} y placa {placa} registrado con exito')

def mostrar_autos():
    if not autos_registrados:
        print("No hay autos registrados.\n")
    else:
        for i, auto in enumerate(autos_registrados, 1):
            print(f"Auto {i}: Marca: {auto.marca}, Modelo: {auto.modelo}, Placa: {auto.placa}, Precio: Q{auto.precioUnitario:.2f} ")

def registrar_cliente():
    nombre = input('Ingrese el nombre del cliente: ')
    correo = input('Ingrese el correo electronico: ')
    Nit = int(input('Ingrese el Nit: '))
    cleinte = Cliente(nombre, correo, Nit)
    clientes_registrados.append(cleinte)
    print("")
    print(f'Cliente {nombre} registrado con exito')


def realizar_compra():
    b = 0.15
    nit = int(input("Ingrese el NIT del cliente: "))
    cliente = next((c for c in clientes_registrados if c.Nit == nit), None)

    if cliente is None:
        print("Cliente no encontrado.\n")
        return

    autos_comprados = []
    while True:
        print("1. Agregar auto a la compra")
        print("2. Terminar compra y facturar")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrar_autos()
            Placa_auto = input("Ingrese el número de placa del auto que desea agregar: ")

            auto_seleccionado = next((auto for auto in autos_registrados if auto.placa == Placa_auto), None)

            if auto_seleccionado:
                autos_comprados.append(auto_seleccionado)
                print("")
                print(f"Auto {auto_seleccionado.marca} {auto_seleccionado.modelo} agregado a la compra.\n")
            else:
                print("Número de auto inválido.\n")

        elif opcion == '2':
            seguro = input("¿Desea agregar un seguro de auto?: ")
            if seguro == "si":
                total1 = b * sum(auto.precioUnitario for auto in autos_comprados) + sum(auto.precioUnitario for auto in autos_registrados)
                id_compra = len(compras_realizadas) + 1
                compra = Compra(autos_comprados, cliente, id_compra, total1)
                compras_realizadas.append(compra)
                print("")
                print(f"Factura ID: {compra.Id}")
                print(f"Cliente: {cliente.nombre} (NIT: {cliente.Nit})")
                for auto in autos_comprados:
                    print(f"- {auto.marca} {auto.modelo}, Placa: {auto.placa}, Precio: ${auto.precioUnitario + b * auto.precioUnitario:.2f}")
                print(f"Total a pagar: ${total1:.2f}\n")
                break
            elif seguro == "no":
                total = sum(auto.precioUnitario for auto in autos_comprados)
                id_compra = len(compras_realizadas) + 1
                compra = Compra(autos_comprados, cliente, id_compra, total)
                compras_realizadas.append(compra)
                print("")
                print(f"Factura ID: {compra.Id}")
                print(f"Cliente: {cliente.nombre} (NIT: {cliente.Nit})")
                for auto in autos_comprados:
                    print(f"- {auto.marca} {auto.modelo}, Placa: {auto.placa}, Precio: ${auto.precioUnitario:.2f}")
                print(f"Total a pagar: ${total:.2f}\n")
                break
            else:
                print("Opción no válida.\n")

def generar_reporte_compras():
    if not compras_realizadas:
        print("No se han realizado compras.\n")
    else:
        print("")
        print("-------------------REPORTE DE COMPRAS----------------------")
        print("==========================================================")
        for compra in compras_realizadas:
            print("CLIENTE: ")
            print(f"    Cliente: {compra.cliente.nombre}")
            print(f"    NIT: {compra.cliente.Nit}")
            print("")
            print("AUTO(S) ADQUIRIDO(S)")
            for auto in compra.listaProductos:
                print(f"    {auto.marca} {auto.modelo}, Placa: {auto.placa}")
            print(f"Total pagado: ${compra.CostoTotal:.2f}")
            print("========================================================== \n")
        TOTAL = sum(compra.CostoTotal for compra in compras_realizadas)
        print(f"Total General: Q{TOTAL:.2f}")
        print("------------------------------------------------------------\n")

def menu():
    while True:
        print("--------------Menú Principal------------")
        print("1. Registrar Auto")
        print("2. Registrar Cliente")
        print("3. Realizar Compra")
        print("4. Reporte de compras")
        print("5. Datos del estudiante")
        print("6. Salir")
        print("----------------------------------------")
        Opcion = input("Elija su opción: ")

        if Opcion == "1":
            registrar_auto()
        elif Opcion == "2":
            registrar_cliente()
        elif Opcion == "3":
            realizar_compra()
        elif Opcion == "4":
            generar_reporte_compras()
        elif Opcion == "5":
            print("")
            print("Ottoniel Fabricio Vásquez Pineda")
            print("202307820")
        elif Opcion == "6":
            break

if __name__ == "__main__":
    menu()
