class Atm:
    def __init__(self):
        self.listD = {'Usuario': ["Daniel"], 'Pin': [123]}
        self.saldo= {'Transaccion': [1000.00]}
        self.menup()


    def menu(self):
        print("**")
        print("Menu principal")
        print("**")
        print("Qué acción desea realizar?")
        print("1 Ingresar saldo\n#2Retirar Dinero\n#3 Consultar saldo\n #4 Salir")
        opcion = int(input("Digita la opción"))
        if opcion==1:
            self.ingresar()
        elif opcion ==2:
            self.retirar()
        elif opcion==3:
            self.consultar()
        elif opcion==4:
            print("Gracias!")
            quit()


    def usuarioN(self ):
        usuario=input("Digita tu nombre de usuario")
        if usuario in self.listD['Usuario']:
            print("El usuario existe intenta con otro")
        else:
            pin =int(input("Digita tu nuevo pin: "))
            self.listD['Usuario'].append(usuario)
            self.listD['Pin'].append((pin))
            self.IngresarCuenta()


    def retirar(self):
        cantidad=float(input("Cuál es la cantidad que deseas retirar"))
        self.saldo['Transaccion'][-1] = self.saldo['Transaccion'][-1]-cantidad
        print(self.saldo)


    def ingresar(self):
        cantidad = float(input("Cuál es la cantidad que deseas ingresar"))
        self.saldo['Transaccion'][-1] = self.saldo['Transaccion'][-1] + cantidad
        print(self.saldo)


    def consultar(self):
        print(f"Este es tu saldo actual: {self.saldo}")


    def IngresarCuenta(self):
            usuario, pin = input('Ingresa tu usuario'), input('Ingresa tu pin')
            if usuario in self.listD['Usuario'] and int(pin) in self.listD['Pin']:
                self.menu()
                return True
            else:
                print('usuario y/o pin incorrectos')
                self.IngresarCuenta()

    def menup(self):
        print("**")
        print("Menu principal")
        print("**")
        print("Qué acción desea realizar?")
        print("1 Ingresar Usuario\n#2: Registrarte\n#3 salir")
        opcion = int(input("Digita la opción"))

        if opcion ==1:
            self.IngresarCuenta()
        elif opcion == 2:
            self.usuarioN()


a=Atm()