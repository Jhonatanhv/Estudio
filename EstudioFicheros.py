try:
    fichero = open("Estudio.py" , "r")
except:
    print("el programa no existe")
else:
    lineas = (fichero.readlines())
    fichero.close
    print( "/n",lineas, "/n")