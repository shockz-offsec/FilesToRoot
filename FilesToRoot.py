import os
import sys
import shutil
import stat

#Esta funcion se encarga de quitar el permiso readonly
def del_rw(action, name, exc):
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)

#Obligatoriamente tiene que tener 2 argumentos, 1º es el propio script, 2º la ruta del directorio raiz (inicial)
if len(sys.argv) !=2:
    print("Error numero incorrecto de argumentos")
    sys.exit()

root = sys.argv[1]#Se asigna la ruta raiz a la variable root
tam = 0#Contador de tamaño por directorio

#os.system(f'attrib -R "{root}" > nul')#Quitar readonly (test)

#Se recorre recurisvamente el directorio raiz, obteniendo la lista de nombre del directorio, los nombres de los subdirectorios y los nombres de los archivos
for dirName, subdirList, fileList in os.walk(root):
    for fname in fileList:#Para cada archivo de la lista de archivos
        #temp=fname
        #os.rename(fname,"temp.mkv")
        full_path = dirName+"\\"+fname #Se guarda en full path la ruta completa del archivo que se este procesando
        if fname.endswith(".rar") or fname.endswith(".zip") or fname.endswith(".mp4") or fname.endswith(".mkv") or fname.endswith(".srt"):#Si el archivo termina en alguna de estas extensiones
            try:
                shutil.move(full_path, root)#Dicho archivo se mueve al directorio raiz
            except Exception as e:
                print(e)
        else:#Si no se encuentra se alamcena el valor en MB de los archivos que haya en el directorio
            tam += os.path.getsize(full_path)/1048576#B to MB
    if dirName != root and tam < 300:#Si dicho directorio contiene archivos cuya suma de tamaños total sea de menos de 300MB (significa que no queda ningun archivo relevante)
        try:
            shutil.rmtree(dirName, ignore_errors=False,onerror=del_rw)#Se elemina la carpeta, si se produce algun error (no poder borrar debido al permiso readonly), se llamada a del_rw() y se elimina
        except Exception as e:
            print(e)
    tam = 0#Reset de la variable para el siguiente subdirectorio