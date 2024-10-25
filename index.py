class Auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año


class ValorMulta(Auto):
    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)
        self.valor_multa = 10000 if año <= 2013 else 30000


class TipoMulta(ValorMulta):
    def __init__(self, marca, modelo, año, multa):
        super().__init__(marca, modelo, año)
        self.multa = multa.lower()
        
        if self.multa == "exceso de velocidad":
            self.valor_multa += 75000
        elif self.multa == "falta de papeles":
            self.valor_multa += 100000
        elif self.multa == "consumo de sustancia":
            self.valor_multa += 200000
        elif self.multa == "tenencia de sustancias":
            self.valor_multa = "Carcel"

    def mostrar_multa(self):
        return f"La multa para el vehículo {self.marca} {self.modelo} del año {self.año} es: {self.valor_multa}"


def ingresar_vehiculo():
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    año = int(input("Año: "))
    return marca, modelo, año


def seleccionar_infraccion():
    print("\n** Seleccionar Infracción **")
    print("1. Exceso de velocidad")
    print("2. Falta de papeles")
    print("3. Consumo de sustancia")
    print("4. Tenencia de sustancias")
    print("5. Otra (Ingrese)")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        return "Exceso de velocidad"
    elif opcion == "2":
        return "Falta de papeles"
    elif opcion == "3":
        return "Consumo de sustancia"
    elif opcion == "4":
        return "Tenencia de sustancias"
    elif opcion == "5":
        return input("Ingrese la infracción: ").lower()


def emitir_multa():
    marca, modelo, año = ingresar_vehiculo()
    infraccion = seleccionar_infraccion()
    multa = TipoMulta(marca, modelo, año, infraccion)
    print(multa.mostrar_multa())

    confirmar = input("¿Desea confirmar y emitir la multa? (s/n): ").lower()
    if confirmar == "s":
        print("Multa emitida con éxito.")
    else:
        print("Multa no emitida.")


def menu_principal():
    while True:
        print("\n** Sistema de Multas Automático **")
        print("1. Ingresar vehículo y calcular multa")
        print("2. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            emitir_multa()
        elif opcion == "2":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")


menu_principal()
