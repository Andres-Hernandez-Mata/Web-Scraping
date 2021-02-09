import os, errno

# Crear directorios

def mkdirs():
# Carpeta para alamacenar las urls mediante el modulo os 
	try:
		os.mkdir('url')
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise
# Carpeta para alamacenar las imagenes mediante el modulo os 
	try:
		os.mkdir('img')
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise

def mkdirsearch(search):
# Crea una carpeta con el nombre del atleta/equipo para almacenar imagenes
	try:
		os.mkdir('img/'+search)
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise
