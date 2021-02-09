from src import mkdir,mkfile,mksoup

def main():
	# Guardar la busqueda
	search_query = input("Introduce un atleta o equipo: ")
	searches = 25

	# Creamos los directorios
	mkdir.mkdirs()
	mkdir.mkdirsearch(search_query)

	# Obtenemos las urls en los archivos
	urls = mkfile.searchgoogle(search_query,searches)
	mkfile.file_write(urls)
	urls_list = mkfile.file_read()

	# Se obtiene la informacion y las imagenes
	mksoup.soup_re(urls_list,search_query)
	mksoup.soup_img(urls_list,search_query)

if __name__ == '__main__':
	main()