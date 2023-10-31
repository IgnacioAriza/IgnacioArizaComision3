class Persona:
    def __init__(self,name="",age=0,dni=0):
        self.name = name
        self.age = age
        self.dni = dni
       
    def get_name(self):
        return self.name
   
    def set_name(self,new_name):
        try:
            if not new_name.isalpha():
                aux = 1/0
            else:
                self.name = new_name
        except:
            print("Ingrese un nombre valido")
            aux = input()
            self.set_name(aux)
       
    #def set_dni(self,dni):
    #    try:
           
person_1 = Persona()


aux = input("Ingrese su nombre: ")
person_1.set_name(aux)

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def get_titular(self):
        return self.titular

    def set_titular(self, titular):
        self.titular = titular

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.cantidad = cantidad

    def mostrar(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.cantidad}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad

# Ejemplo de uso
cuenta1 = Cuenta("Juan Pérez", 1000.0)
cuenta1.mostrar()

# Realizar depósito e impresión
cuenta1.ingresar(500.0)
cuenta1.mostrar()

# Realizar retiro e impresión
cuenta1.retirar(200.0)
cuenta1.mostrar()

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def tipo_de_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"

    def lado_mayor(self):
        return max(self.lado1, self.lado2, self.lado3)

# Solicitar al usuario ingresar los lados del triángulo
lado1 = float(input("Ingrese la longitud del primer lado: "))
lado2 = float(input("Ingrese la longitud del segundo lado: "))
lado3 = float(input("Ingrese la longitud del tercer lado: "))

triangulo = Triangulo(lado1, lado2, lado3)

print(f"El triángulo es de tipo {triangulo.tipo_de_triangulo()}.")
print(f"El lado con mayor longitud es de tamaño {triangulo.lado_mayor()}.")

class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self, nombre, telefono, email):
        contacto = Contacto(nombre, telefono, email)
        self.contactos.append(contacto)

    def listar_contactos(self):
        for contacto in self.contactos:
            print(f"Nombre: {contacto.nombre}")
            print(f"Teléfono: {contacto.telefono}")
            print(f"Email: {contacto.email}")
            print("")

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                print(f"Nombre: {contacto.nombre}")
                print(f"Teléfono: {contacto.telefono}")
                print(f"Email: {contacto.email}")
                return
        print(f"Contacto con el nombre '{nombre}' no encontrado.")

    def editar_contacto(self, nombre, nuevo_telefono, nuevo_email):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                contacto.telefono = nuevo_telefono
                contacto.email = nuevo_email
                print(f"Contacto '{nombre}' editado exitosamente.")
                return
        print(f"Contacto con el nombre '{nombre}' no encontrado.")

    def menu(self):
        while True:
            print("Menú de Agenda")
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nombre = input("Nombre: ")
                telefono = input("Teléfono: ")
                email = input("Email: ")
                self.añadir_contacto(nombre, telefono, email)

            elif opcion == "2":
                self.listar_contactos()

            elif opcion == "3":
                nombre = input("Nombre a buscar: ")
                self.buscar_contacto(nombre)

            elif opcion == "4":
                nombre = input("Nombre del contacto a editar: ")
                nuevo_telefono = input("Nuevo teléfono: ")
                nuevo_email = input("Nuevo email: ")
                self.editar_contacto(nombre, nuevo_telefono, nuevo_email)

            elif opcion == "5":
                print("Agenda cerrada.")
                break
            else:
                print("Opción no válida. Por favor, elija una opción válida.")

# Ejemplo de uso
agenda = Agenda()
agenda.menu()
