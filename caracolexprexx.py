import os
os.system("cls")

menu = '''                                MENU
---------------------------------------------------------------------------------------------
    1. Registrar usuario
    2. Buscar producto
    3. Listar productos
    4. Salir '''

listacodigo = [111111,222222,333333]
listanombre = ['TV', 'COCINA', 'TECLADO']
listacategoria = ['ELECTRONICA', 'HOGAR','TECNOLOGIA']
listaprecio = [200000,150000,30000]
listastock = [2,5,0]

def Agregarproducto():
        while True:
            try:
                codigo = int(input("Ingrese codigo: "))
                if codigo > 99999 and codigo < 1000000:
                   listacodigo.append(codigo)
                   break
                else:
                    print("Error, ingrese codigo valido")
            except:
                print("Error de digitacion")
        while True:        
          nombre = input("Ingrese Nombre: ")
          if len(nombre) >= 2 and len(nombre) < 50:
             listanombre.append(nombre)
             break
          else:
              print("Error, maximo de caracteres")
        while True:
                categoria = input("ingrese categoria: ")
                if len(categoria) >= 2 and len(categoria) < 50:
                    listacategoria.append(categoria)
                    break
                else:
                 print("Error, digite categoria valida")                   
        while True:
                try:            
                    precio = int(input("Ingrese precio: "))
                    if precio > 0:
                        listaprecio.append(precio)
                        break
                    else:
                        print("Seleccione precio valido")
                except:
                    print("Error, ingrese precio valido")  
        while True:
                try:            
                    stock = int(input("Ingrese stock: "))
                    if stock >= 0:
                        listastock.append(stock)
                        break
                    else:
                        print("Seleccione rango valido")
                except:
                    print("Error, ingrese rango valido")                    
def Listarlistar(): 
    print("                            LISTADO GENERAL  ")
    print("--+------------+----------------------+---------------------------+-----------+-------------+")
    print("N°|   CODIGO   |        NOMBRE        |         CATEGORIA         |  PRECIO   |    STOCK    |")
    print("--+------------+----------------------+---------------------------+-----------+-------------+")
    for i in range(len(listacodigo)):
        if listastock[i] >= 5:
                stokkk = "CON STOCK"
        elif listastock[i] < 5  and listastock[i] > 0:
                stokkk = "POCO STOCK"
        else:
                stokkk = "SIN STOCK" 
        print(f"{i+1} | {listacodigo[i]:10d} | {listanombre[i]:20s} | {listacategoria[i]:25s} | ${listaprecio[i]:8d} | {stokkk}   | ")
        print("--+------------+----------------------+---------------------------+-----------+-------------+")
def Buscarcodigo():
    while True:
        try:
            codigon = int(input("CODIGO a buscar: "))
            for i in range(len(listacodigo)):
                if codigon == listacodigo[i]:
                    print("--+------------+---------------------------+---------------------------+-----------+")
                    print("N°|   CODIGO   |        NOMBRE             |         CATEGORIA         |  PRECIO   |")
                    print("---------------+---------------------------+---------------------------+-----------+")
                    print(f"{i+1} | {listacodigo[i]:10d} | {listanombre[i]:25s} | {listacategoria[i]:25s} | ${listaprecio[i]:8d} | ")
                    print("---------------+---------------------------+---------------------------+-----------+")
                    return menu           
            else:
                print("Error,codigo no encontrado")
            break
        except:
            print("ERROR DE DIGITACION")
            return menu

while True:
    try:
        print(menu)
        opc = int(input("Seleccione opcion: "))
        if opc == 1:
            Agregarproducto()
        elif opc == 2:
            Buscarcodigo()
        elif opc == 3:
            Listarlistar()    
        elif opc == 4:
            break
        else:
            print("Error, seleccione opcion valida")
    except:
        print("Error, seleccione opcion valida")
input("ENTER PARA TERMINAR")










