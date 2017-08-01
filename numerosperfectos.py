class numerosPerfectos():

	def __init__(self):
		print('Bienvenido al modulo de numeros perfectos')

	def inicio (self):
		numero_ciclos = int(input('Ingrese la cantidad de ciclos que desea obtener los numeros perfectos: '))
		resultado_ciclos_uno = self.numeros_perfectos_ciclos(numero_ciclos)
		self.imprimir_numeros_perfectos_listado(resultado_ciclos_uno)

	def numeros_perfectos(self,n):
		x=n-1
		resultado_uno = 2**x
		resultado_dos = (2**n)-1
		resultado_tres = resultado_uno * resultado_dos
		return resultado_tres

	def numeros_perfectos_ciclos(self,ciclos):
		listado_numeros_perfectos = []
		for elemento in range((ciclos+1)):
			resultado_ciclos= self.numeros_perfectos(elemento)
			listado_numeros_perfectos.append(resultado_ciclos)
		return listado_numeros_perfectos

	def imprimir_numeros_perfectos_listado(self,listado):
		height = len(listado)
		if(height>0):
			for elemento in range(height):
				print(listado[elemento])
		else:
			print('La lista esta vacia')

temporal = numerosPerfectos()
temporal.inicio()