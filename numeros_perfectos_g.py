
class NumerosPerfectosGenerator():
    """
        Herramienta para trabajar con numeros perfectos
    """
    
    def __init__(self):
        print('Bienvenido al modulo de numeros perfectos con generator')

    def numero_perfecto(self, numero):
        numero -= 1
        resultado_uno = 2**numero
        resultado_dos = (2**numero)-1
        resultado_tres = resultado_uno * resultado_dos
        return resultado_tres

    def numeros_perfectos_interador(self, ciclos:int):
        """
            Esta implementacion es un poco mas rapida que la version de
            almacenar las cosas en un list y tiene un costo computacional
            inferior ya que no se almacena nada en la computadora asimismo
            se puede utilizar para guardar en un archivo o DB mas rapido
        """
        for elemento in range(ciclos+1):
            yield self.numero_perfecto(elemento)

    def imprimir_numeros_perfectos(self):
        """
            se encarga de llamar a la funcion para imprimir los numeros perfectos
            en la pantalla
        """
        cantidad = int(input('Ingrese la cantidad de ciclos o repeticiones que desea '))
        for numero in self.numeros_perfectos_interador(cantidad):
            print(numero)
    

temporal = NumerosPerfectosGenerator()
temporal.imprimir_numeros_perfectos()
