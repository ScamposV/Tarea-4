import os
import bcrypt

'''
PARA CRACKEAR LOS ARCHIVOS
'''
def crack():
    path= os.path.join(os.getcwd(),'hashcat-6.2.2')
    print("----------------------------------------------------")
    hash = input("Ingresa la ruta del archivo: ")
    print("----------------------------------------------------")
    #modo 0 - 10 - 10 - 1000 - 1800
    print("Para \nMD5 ingresar 0 \nMD5 con salt ingresar 10 \nNTLM ingresar 1000 \nsha512crypt ingresar 1800")
    modo = input('Modo: ')
    print("----------------------------------------------------")
    d = input('Diccionario: ')
    dd = input('Diccionario: ')
    print("----------------------------------------------------")
    #lo guarda en la carpeta "hashcat-6.2.2"
    textoplano = input('Nombre del nuevo archivo: ')
    print("----------------------------------------------------")
    os.chdir(path)
    try:
        os.remove('hashcat.potfile')
        abrir=str(os.path.join(textoplano))
        os.system(f"hashcat.exe -m {modo} -a 0 {hash} {d} {dd} --outfile={abrir}.txt --force")
    except:
         pass
'''
HASHEAMOS EL TEXTO PLANO DE LOS crackArchivo
'''
def newHash():
    '''EJEMPLO DE BCRYPT
    password = "You know my name"
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(encoding='utf-8'), salt)
    print (hashed)
    '''
    #PARA HASHEAR
    archivo=input("Ingrese direccion del archivo: ")
    salt= bcrypt.gensalt()
    #PARA GUARDAR LOS HASHES
    archive = input('Ingresa el nombre con el que se guardara el archivo: ')
    guardando = open(f'{archive}.txt','w')
    #HASHEANDO
    abrir=open(archivo,"r").readlines()
    print("---------------HASHEANDO---------------")
    for linea in abrir:
        newline=linea.strip().rsplit(':',1)[1]
        encrypted = bcrypt.hashpw(newline.encode(encoding='utf-8'), salt)
        guardando.write(encrypted.decode()+'\n')
