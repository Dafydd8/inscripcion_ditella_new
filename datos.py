import csv
""" 
	los datos de acceso deben ser strings 

	Ejemplo:
		usuario = 'gcarlos@mail.utdt.edu'
		clave = '010101789'
"""

usuario = ''
clave = ''

""" 
	los datos horarios deben ser cargados como numeros y segun formato de
	24 horas 
	Ejemplo:
		anio = 2020 
		mes = 2 
		dia = 19
		hora = 15
		minutos = 30
"""

anio = 2025
mes = 7
dia = 25
hora = 16
minutos = 0
segundos = 0

"""
	cambiar el PATH (absolute path) del chromedriver, para no tener problemas
	con los distintos interpretadores.
	
	Ejemplo:
		chromedriverpath = 'users/usuario/inscripcion-utdt/chromedriver'
"""

chromedriverpath = './chromedriver'

"""
	Si la variable esperar es True, el programa espera hasta la hora indicada para empezar la inscripcion. Si es False, empieza ni bien es ejecutado el programa.
	La variable loops indica la cantidad de veces que el programa intenta inscribirse en cada materia.
"""

esperar = True
loops = 10