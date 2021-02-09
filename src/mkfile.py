import os, errno

# Verificar la instalacion
try:
	from googlesearch import search
except:
	os.system("pip install googlesearch-python")
	os.system("clear")

# Realizamos la busqueda en google
def searchgoogle(search_query,searches):
	urls = search(search_query,num_results=searches)
	return urls

# Escribir las urls en un archivo obtenidas de la busqueda
def file_write(urls):
	with open('url/urls.txt', 'w') as file:
		for line in urls:
			if "http" in line:
				file.write(line+"\n")

# Leer las urls mediante el archivo creado y regresamos una lista con las urls
def file_read():
	with open('url/urls.txt', 'r') as file:
		fileread = ""
		for line in file:
			fileread += line
		urls_list = fileread.split()
	return urls_list