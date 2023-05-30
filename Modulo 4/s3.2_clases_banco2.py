"""
Clase Banco:
- Atributos: nombre (string), código (int), dirección (string), lista_cuentas (list)
- Métodos: 
- crear_cuenta(self, tipo_cuenta, titular, saldo_inicial): crea una nueva cuenta y la añade a la lista de cuentas del banco.
- transferencia(self, cuenta_origen, cuenta_destino, monto): transfiere un monto determinado desde una cuenta de origen a una de destino.
- obtener_cuenta_por_num(self, num_cuenta): devuelve la cuenta correspondiente a un número de cuenta específico.
- obtener_cuentas_por_titular(self, titular): devuelve una lista con todas las cuentas de un titular específico.

Clase Cuenta:
- Atributos: numero (int), titular (string), saldo (float)
- Métodos:
- depositar(self, monto): *aumenta el saldo de la cuenta por un monto determinado.
- consultar_saldo(self): *devuelve el saldo actual de la cuenta.

Clase CuentaAhorro (hereda de Cuenta):
- Atributos: retiros (int)
- Métodos:
- retirar(self, monto): *realiza un retiro de dinero de la cuenta y aumenta en uno el contador de retiros.

Clase CuentaCorriente (hereda de Cuenta):
- Atributos: limite_rojo (float)
- Métodos:
- retirar(self, monto): *realiza un retiro de dinero de la cuenta, pero verifica que el monto no supere el límite de la cuenta y 
*cambia el saldo a rojo si corresponde.

Clase Cliente:
- Atributos: nombre (string), direccion (string), identificacion (int)
- Métodos: ninguno
"""

# Definición de la clase Banco
class Banco:
    def __init__(self, nombre, codigo, direccion):
        self.nombre = nombre
        self.codigo = codigo
        self.direccion = direccion
        self.lista_cuentas = []

    def crear_cuenta(self, tipo_cuenta, titular, saldo_inicial):
        numero_cuenta = len(self.lista_cuentas) + 1
        if tipo_cuenta == "ahorro":
            nueva_cuenta = CuentaAhorro(numero_cuenta, titular, saldo_inicial)
        else:
            nueva_cuenta = CuentaCorriente(numero_cuenta, titular, saldo_inicial)
        self.lista_cuentas.append(nueva_cuenta)
        print("Cuenta creada exitosamente")

    def transferencia(self, cuenta_origen, cuenta_destino, monto):
        origen = self.obtener_cuenta_por_num(cuenta_origen)
        destino = self.obtener_cuenta_por_num(cuenta_destino)
        if origen.saldo >= monto:
            origen.saldo -= monto
            destino.saldo += monto
            print("Transferencia realizada exitosamente")
        else:
            print("La cuenta de origen no tiene suficientes fondos")

    def obtener_cuenta_por_num(self, num_cuenta):
        for cuenta in self.lista_cuentas:
            if cuenta.numero == num_cuenta:
                return cuenta
        print("No se encontró la cuenta")
        return None

    def obtener_cuentas_por_titular(self, titular):
        cuentas_titular = []
        for cuenta in self.lista_cuentas:
            if cuenta.titular == titular:
                cuentas_titular.append(cuenta)
        if cuentas_titular:
            return cuentas_titular
        else:
            print("No se encontraron cuentas para el titular especificado")
            return None

# Definición de la clase Cuenta
class Cuenta:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto
        print("Depósito realizado exitosamente")

    def consultar_saldo(self):
        return self.saldo

# Definición de la clase CuentaAhorro
class CuentaAhorro(Cuenta):
    def __init__(self, numero, titular, saldo):
        super().__init__(numero, titular, saldo)
        self.retiros = 0

    def retirar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            self.retiros += 1
            print("Retiro realizado exitosamente")
        else:
            print("Saldo insuficiente para realizar el retiro")

# Definición de la clase CuentaCorriente
class CuentaCorriente(Cuenta):
    def __init__(self, numero, titular, saldo):
        super().__init__(numero, titular, saldo)
        self.limite_rojo = -1000

    def retirar(self, monto):
        if self.saldo + self.limite_rojo >= monto:
            self.saldo -= monto
            if self.saldo < 0:
                print("La cuenta ha entrado en saldo negativo")
            print("Retiro realizado exitosamente")
        else:
            print("Monto solicitado supera el límite de la cuenta corriente")

# Definición de la clase Cliente
class Cliente:
    def __init__(self, nombre, direccion, identificacion):
        self.nombre = nombre
        self.direccion = direccion
        self.identificacion = identificacion

# Ejemplo
# Crear banco
banco = Banco("Banco Scode CL", 12345, "Av. Integración 2023")

# Crear cuentas
banco.crear_cuenta("ahorro", "Guido van Rossum", 150000)
banco.crear_cuenta("corriente", "Guido van Rossum", 3000000)
banco.crear_cuenta("ahorro", "James Gosling", 2800000)

# Consultar saldo de una cuenta
cuenta1 = banco.obtener_cuenta_por_num(1)
saldo_cuenta1 = cuenta1.consultar_saldo()
print("El saldo de la cuenta 1 es:", saldo_cuenta1)

# Realizar transferencia
banco.transferencia(2, 1, 2000000)

# Consultar cuentas de un titular
cuentas_juan = banco.obtener_cuentas_por_titular("Guido van Rossum")
for cuenta in cuentas_juan:
    print("Cuenta", cuenta.numero)
    print("Saldo:", cuenta.saldo)

# Realizar retiro de cuenta de ahorro
cuenta2 = banco.obtener_cuenta_por_num(2)
cuenta2.retirar(500000)

# Realizar retiro de cuenta corriente con límite de rojo alcanzado
cuenta3 = banco.obtener_cuenta_por_num(3)
cuenta3.retirar(2800000)