from math import *
from dictionary import *


Hash_Fijas=[None]*97
Hash_Moviles=[None]*97
AutosCargados=[]


archivo=open("local_path.txt")

def createGraph(V, A):
  Graph = []
  for vertice in V:
    list=[]
    list.append(vertice)
    Graph.append(list)
  for vertice in Graph:
  #se recorren los vertices
    for edge in A:
      vertice[0]
      if vertice[0]==edge[0]:
        vertice.append(edge[1])
  return Graph

def create_map(archivo):
    linea1=archivo.readline()
    linea2=archivo.readline() 
    esquinas=[]
    subcad=''
    #OBTENEMOS LISTA DE ESQUINAS
    for i in range(0, len(linea1)):
        if linea1[i-1]=='{':
            break
    for i in range(i, len(linea1)):
        if linea1[i] != ',' and linea1[i] != '\n' and linea1[i]!= ' ' and linea1[i]!='}':
            subcad+=linea1[i]
        else:
            if subcad!='':
                esquinas.append(subcad)
                subcad=''

    Lista_calles=[]
    calle=[None, None, None]
    espacio=0
    subcad=''
    i=0
    #OBTENEMOS LISTA DE CALLES
    for i in range(i, len(linea2)):
        if linea2[i-1]=='<':
            for i in range(i, len(linea2)):
                if linea2[i] != ',' and linea2[i] != '\n' and linea2[i]!= ' ' and linea2[i]!='>':
                    subcad+=linea2[i]
                else:
                    if subcad!='':
                        calle[espacio]=subcad
                        subcad=''
                        espacio += 1
                    if espacio==3:
                        CALLE_P=(calle[0], calle[1], int(calle[2]))
                        Lista_calles.append(CALLE_P)
                        calle=[None, None, None]
                        espacio=0
                        break
    
    MAPA=createGraph(esquinas, Lista_calles)
    print('map created succesfully  :)\n')
    return MAPA

MAPA=create_map(archivo)

def crear_lista_calles(archivo):
        archivo=open('local_path.txt','r')
        linea1=archivo.readline()
        linea2=archivo.readline()
        
        Lista_calles=[]
        calle=[None, None, None]
        espacio=0
        subcad=''
        i=0
        for i in range(i, len(linea2)):
            if linea2[i-1]=='<':
                for i in range(i, len(linea2)):
                    if linea2[i] != ',' and linea2[i] != '\n' and linea2[i]!= ' ' and linea2[i]!='>':
                        subcad+=linea2[i]
                    else:
                        if subcad!='':
                            calle[espacio]=subcad
                            subcad=''
                            espacio += 1
                        if espacio==3:
                            CALLE_P=(calle[0], calle[1], int(calle[2]))
                            Lista_calles.append(CALLE_P)
                            calle=[None, None, None]
                            espacio=0
                            break
        return(Lista_calles) 

Lista_Calles=crear_lista_calles(archivo)
archivo.close()

def verify_street(Lista_Calles, direccionA, direccionB):
    booleano=False
    for i in range(0, len(Lista_Calles)):
        if Lista_Calles[i][0]==direccionA[0]:
            if Lista_Calles[i][1]==direccionB[0]:
                if Lista_Calles[i][2]==(direccionA[1]+direccionB[1]):
                    booleano=True
    if booleano == False:
        for i in range(0, len(Lista_Calles)):
            if Lista_Calles[i][0]==direccionB[0]:
                if Lista_Calles[i][1]==direccionA[0]:
                    if Lista_Calles[i][2]==(direccionA[1]+direccionB[1]):
                        booleano=True
    return booleano

def load_fix_element(ubiFija, Hash_Fijas):
    if ubiFija==None or Hash_Fijas==None:
        return None
    else:
        nombre, direccion=ubiFija
        casillero=UberHash(nombre)
        if Hash_Fijas[casillero]==None:
            Hash_Fijas[casillero]=[]
            Hash_Fijas[casillero].append(ubiFija)
        else:
            Hash_Fijas[casillero].append(ubiFija)
        print('\nUbicación cargada correctamente.\n')

def load_movil_element(ubiMovil, Hash_Moviles):
    if ubiMovil==None or Hash_Moviles==None:
        return None
    else:
        nombre, direccion, monto=ubiMovil
        casillero=UberHash(nombre)
        if Hash_Moviles[casillero]==None:
            Hash_Moviles[casillero]=[]
            Hash_Moviles[casillero].append(ubiMovil)
        else:
            Hash_Moviles[casillero].append(ubiMovil)
        print('\nUbicación cargada correctamente.\n')
        
def Search(HashTable, nombre): 
    if HashTable!=None and nombre!=None:
        pos=UberHash(nombre)
        if HashTable[pos]==None:
            return False
        else:
            current=HashTable[pos][0]
            for j in range(0, len(HashTable[pos])):
                if current[j]==nombre:
                    return True

#####
class DijkstraNode():
    nombre=None
    padre=None
    delta=None
    adjuntos=None

archivo=open('local_path.txt')
linea1=archivo.readline()
Lista_nodos=[]  #LISTA CON NODOS PARA CADA ESQUINA
subcad=''

for i in range(0, len(linea1)):
    if linea1[i-1]=='{':
        break
for i in range(i, len(linea1)):
    if linea1[i] != ',' and linea1[i] != '\n' and linea1[i]!= ' ' and linea1[i]!='}':
        subcad+=linea1[i]
    else:
        if subcad!='':
            Lista_nodos.append(subcad)
            subcad=''

Lista_esquinas=[]  #LISTA CON NOMBRES DE LAS ESQUINAS

for i in range(0, len(Lista_nodos)):
    node=DijkstraNode()
    Lista_esquinas.append(Lista_nodos[i])
    node.nombre=Lista_nodos[i]
    Lista_nodos[i]=node

archivo.close()

for i in range(0, len(Lista_nodos)):
    Lista_nodos[i].adjuntos=MAPA[i]
    Lista_nodos[i].adjuntos.remove(Lista_nodos[i].nombre)


for i in range(0, len(Lista_nodos)):
    nodo=Lista_nodos[i]
    if len(nodo.adjuntos)>=1:
        for j in range(0, len(nodo.adjuntos)):
            pos=Lista_esquinas.index(nodo.adjuntos[j])
            nodo.adjuntos[j]=Lista_nodos[pos]

def pedir_ubicacion(Lista_Calles):
    ea=input("Ingrese una de las esquinas de la calle donde se encuentra la ubicacion:   ")
    da=int(input("Ingrese la distancia en metros de la ubicación a la primer esquina:   "))
    direccionA=(ea, da)
    
    eb=input("Ingrese la segunda esquina de la calle donde se encuentra la ubicacion:   ")
    db=int(input("Ingrese la distancia en metros de la ubicación a la segunda esquina:   "))
    direccionB=(eb, db)

    booleano=verify_street(Lista_Calles, direccionA, direccionB)

    while booleano!=True:
        print('UBICACIÓN INCORRECTA\nINGRESE LOS DATOS NUEVAMENTE')
        ea=input("Ingrese una de las esquinas de la calle donde se encuentra la ubicacion:   ")
        da=int(input("Ingrese la distancia en metros de la ubicación a la primer esquina:   "))
        direccionA=(ea, da)
    
        eb=input("Ingrese la segunda esquina de la calle donde se encuentra la ubicacion:   ")
        db=int(input("Ingrese la distancia en metros de la ubicación a la segunda esquina:   "))
        direccionB=(eb, db)
        booleano=verify_street(Lista_Calles, direccionA, direccionB)

    if booleano==True:
        direccion=(direccionA, direccionB)
        return direccion

def pedir_nombre(HashTable):
    nombre=input('Ingrese el nombre:   ')
    nombre=nombre.upper()
    exist=Search(HashTable, nombre)
    while exist==True: 
        nombre=input('Ese nombre ya existe\nIngrese un nuevo nombre:   ')
        exist=Search(HashTable, nombre) 
    return nombre

def calculate_delta(u, v, Lista_Calles):
    for i in range(0, len(Lista_Calles)):
        if Lista_Calles[i][0]==u.nombre:
            if Lista_Calles[i][1]==v.nombre:
                return Lista_Calles[i][2]

def initRelax(G, s):   #G= LISTA NODOS      S=RAIZ
    for v in G:
        v.delta=inf
        v.padre=None
    s.delta=0

def Relax(u, v, Lista_Calles):
    if v.delta > (u.delta + calculate_delta(u, v, Lista_Calles)):
        v.delta= u.delta + calculate_delta(u, v, Lista_Calles)
        v.padre=u

def minQueue(V):
    Q=[]
    for vertice in V:
        enqueue_priority(Q, vertice)
    return Q

def enqueue_priority(Q, node):
    if Q != None:
        if len(Q)==0:
            Q.append(node)
        else:
            for i in range(0,len(Q)):
                if Q[i].delta > node.delta:
                    if i+1<len(Q):
                        if Q[i+1].delta <= node.delta:
                            Q.insert(i+1, node)
                            break
                    else:
                        Q.append(node)
                else:
                    Q.insert(i, node)
                    break

def DIJKSTRA(Lista_nodos, raiz, Lista_Calles):
    ListaVertices=Lista_nodos
    initRelax(Lista_nodos, raiz)
    S=[]
    Q=minQueue(ListaVertices)
    if raiz not in Q:
        Q.append(raiz)
    while len(Q)>0:
        u=Q.pop()
        S.insert(0,u)
        for v in u.adjuntos:
            Relax(u,v,Lista_Calles)
        
            for nodo in S:
                for v in nodo.adjuntos:
                    Relax(nodo,v,Lista_Calles)
    return S

def Buscar_Autos(AutosCargados, persona, DireccionPersona, Lista_nodos,Lista_Calles):
    AUTOS_DISPONIBLES=[]
    sumaDist=0
    if len(AutosCargados)<1:
        print('Aun no hay vehículos cargados en el sistema.')
    else:                                           #en direccionPersona tengo [(e1,50),(e2,100)]  
        for i in range(0, len(AutosCargados)):      #en autos cargados ya tengo(nombre, esquina, monto)
            raiz=None                               #persona=(nombre, direccion, monto)
            for j in range(0, len(Lista_nodos)):    #Coche(Nombre auto, distancia, monto/tarifa)
                if AutosCargados[i][1]==Lista_nodos[j].nombre:
                    raiz=Lista_nodos[j]
            if raiz!=None:
                caminoAuto=DIJKSTRA(Lista_nodos, raiz, Lista_Calles)
                for nodo in caminoAuto:
                    sumaDist=0
                    if nodo.nombre==DireccionPersona[0][0]:
                        if nodo.delta!=inf: 
                            pos=UberHash(AutosCargados[i][0])
                            sumaDist+=DireccionPersona[0][1]+Hash_Moviles[pos][0][1][0][1]
                            coche=(AutosCargados[i][0],nodo.delta+sumaDist,AutosCargados[i][2])
                            AUTOS_DISPONIBLES.append(coche)
    #costo camino mas corto(auto a persona)+(tarifa)/4

  
    for coche in AUTOS_DISPONIBLES:
        if persona[2]<=(coche[1]+(coche[2]/4)):         #ACA FILTRAMOS AUTOS Q NO PUEDA PAGAR
            AUTOS_DISPONIBLES.remove(coche)
    TOP3=[]        
    
    for i in range(0, len(AUTOS_DISPONIBLES)):
        if len(TOP3)>=3:
            break
        menor=inf
        for i in range(0, len(AUTOS_DISPONIBLES)):
            
            if AUTOS_DISPONIBLES[i][1]<menor:
                menor= AUTOS_DISPONIBLES[i][1]
                
            if menor!=inf:
                if AUTOS_DISPONIBLES[i] not in TOP3:
                    TOP3.append(AUTOS_DISPONIBLES[i])
                   
    return TOP3


def create_trip(AutosCargados, USUARIO, DireccionPersona, Lista_nodos,Lista_Calles):
            TOP3=Buscar_Autos(AutosCargados, USUARIO, DireccionPersona, Lista_nodos,Lista_Calles)
            print('\nAUTOS DISPONIBLES: ')
            for i in range(0, len(TOP3)):
                print('\n',i+1,')  Coche: ',TOP3[i][0],' Dist.: ',TOP3[i][1],' Tarifa: ',TOP3[i][2])
                print(' $---',TOP3[i][1]+(TOP3[i][2]/4))
            print(' ',len(TOP3)+1,') CANCELAR VIAJE ')
            select_auto=int(input('Ingrese el auto con el cual desea comenzar su viaje:  '))
            
            while select_auto>(len(TOP3)+1) or select_auto<1:
                print('\nOpción inválida\n')
                print('AUTOS DISPONIBLES: ')
                for i in range(0, len(TOP3)):
                    print('\n',i+1,')  Coche: ',TOP3[i][0],' Dist.: ',TOP3[i][1],' Tarifa: ',TOP3[i][2])
                    print(' $---',TOP3[i][1]+(TOP3[i][2]/4))
                print(' ',len(TOP3)+1,') CANCELAR VIAJE ')
                select_auto=int(input('Ingrese el auto con el cual desea comenzar su viaje:  '))
                if select_auto==(len(TOP3)+1):
                    break
                #auto designado=(nombre, delta, tarifa)
            if select_auto!=(len(TOP3)+1):
                Auto_Designado=TOP3[select_auto-1]
                pos=UberHash(Auto_Designado[0])
                for i in range(0, len(Hash_Moviles[pos])):
                    if Hash_Moviles[pos][i][0]==Auto_Designado[0]:
                        Hash_Moviles[pos][i][1]=DireccionViaje
                
                Hash_Moviles[posUSUARIO][indexUSUARIO][1]=DireccionViaje
                Hash_Moviles[posUSUARIO][indexUSUARIO][2]-=(Auto_Designado[1]+(Auto_Designado[2]/4))

########################################    MENU    ################################################
opcion=None

while opcion!='C':
 

    print("\n\nElija la opcion a realizar:"+"\n"+
    "1)Cargar una ubicacion fija (F)"+"\n"+
    "2)Cargar una ubicación movil(M)"+"\n"+
    "3)realizar un viaje(V)\n4)Buscar ubicaciones(B)\n"+"5)Cerrar app(C)")
    opcion=input('Ingrese la opción deseada:   ')
    opcion=opcion.upper()
    if opcion=='C':
        print('CERRANDO APP...')
        break
    else:

        while opcion!='F' and opcion!='M' and opcion!='V' and opcion!='B':
            if opcion!='F' and opcion!='M' and opcion!='V'and opcion!='B':
                opcion=input('OPCIÓN INCORRECTA\nINGRESE NUEVAMENTE\n'+"1)Cargar una ubicacion fija (F)"+"\n"+
    "2)Cargar una ubicación movil(M)"+"\n"+
    "3)realizar un viaje(V)\n4)Buscar ubicaciones(B)\n")
                opcion=opcion.upper()

        if opcion=='B':
            busqueda=int(input('Que tipo de ubicación desea conocer?\n1)Ubicación móvil\n2)Ubicacion fija\n'))
            while busqueda<1 or busqueda>2:
                print('\nOpción incorrecta\n')
                busqueda=int(input('Que tipo de ubicación desea conocer?\n1)Ubicación móvil\n2)Ubicacion fija\n'))
            
            if busqueda==1:
                nombre=input('Ingrese el nombre de la ubicacion movil:  ')
                booleano=Search(Hash_Moviles, nombre)
                if booleano==False:
                    print('\nEsa ubicación no está registrada.\n')
                else:
                    pos=UberHash(nombre)
                    if len(Hash_Moviles[pos])==1:
                        print('La ubicación de ',nombre,' es: ', Hash_Moviles[pos][1])
                    else:
                        for i in range(0, len(Hash_Moviles[pos])):
                            if Hash_Moviles[pos][i][0]==nombre:
                                print('La ubicación de ',nombre,' es: ', Hash_Moviles[pos][i][1])
                                break
            if busqueda==2:
                nombre=input('Ingrese el nombre de la ubicacion fija:'  )                           
                booleano=Search(Hash_Fijas, nombre)
                if booleano==False:
                    print('Esa ubicación no está registrada.')
                else:
                    pos=UberHash(nombre)
                    if len(Hash_Fijas[pos])==1:
                        print('La ubicación de ',nombre,' es: ', Hash_Fijas[pos][1])
                    else:
                        for i in range(0, len(Hash_Fijas[pos])):
                            if Hash_Fijas[pos][i][0]==nombre:
                                print('La ubicación de ',nombre,' es: ', Hash_Fijas[pos][i][1])
                                break

        if opcion=='F':
            nombre=pedir_nombre(Hash_Fijas)
            direccion=pedir_ubicacion(Lista_Calles)
            ubicacionFija=(nombre, direccion)
            load_fix_element(ubicacionFija, Hash_Fijas)

        if opcion=='M':

            elemento_movil=input('\n1)Cargar auto (C)\n2)Cargar persona (P)\n')
            elemento_movil=elemento_movil.upper()
            while elemento_movil!='C' and elemento_movil!='P':
                elemento_movil=input('\n1)Cargar auto (C)\n2)Cargar persona (P)\n')
                elemento_movil=elemento_movil.upper()
            
            nombre=pedir_nombre(Hash_Moviles)
            direccion=pedir_ubicacion(Lista_Calles)
            monto=float(input('Ingrese el monto de la ubicación movil:   '))
            while monto<0:
                monto=float(input('MONTO INVÁLIDO\nIngrese el monto de la ubicación movil:   '))
            ubicacionMovil=[nombre, direccion, monto]
            if elemento_movil=='C':
                AutosCargados.append((nombre,direccion[0][0], monto))   #LISTA DE AUTOS CARGADOS
                print('\nAUTOS Cargados: ', AutosCargados)
            load_movil_element(ubicacionMovil, Hash_Moviles)
            
       
        if opcion=='V':
            persona=input("ingrese su nombre de usuario Ej:P1 ")
            persona=persona.upper()
            exist=Search(Hash_Moviles, persona)
            while exist==False:
                print('\nLa persona ingresada no está registrada\nIntente nuevamente con otra persona.')
                persona=input("ingrese su nombre de usuario Ej:P1    ")
                persona=persona.upper()
                exist=Search(Hash_Moviles, persona)
            pos=UberHash(persona)
            if len(Hash_Moviles[pos])==1:
                DireccionPersona=Hash_Moviles[pos][0][1]
                USUARIO=Hash_Moviles[pos][0]                       #PERSONAAAAAAAA
                posUSUARIO=pos
                indexUSUARIO=0

            elif len(Hash_Moviles[pos])>1:
                for i in range(0, len(Hash_Moviles[pos])):
                    if Hash_Moviles[pos][i][0]==persona:
                        DireccionPersona=Hash_Moviles[pos][i][1]  #DIRECCION DE LA PERSONA Q VIAJA
                        USUARIO=Hash_Moviles[pos][i][0]
                        posUSUARIO=pos
                        indexUSUARIO=i

            print("\nElija la forma en la que desea cargar el lugar de destino:"+"\n"+
            "1)Cargar ubicacion fija con nombre (N)"+"\n"+
            "2)Cargar una ubicación fija con direccion(D)")
            cargaubi=input("Ingrese la opcion deseada  ")
            cargaubi=cargaubi.upper()
            while cargaubi!='N' and cargaubi!='D':
                if cargaubi!='N' and cargaubi!='D':
                    cargaubi=input('OPCIÓN INCORRECTA\nINGRESE NUEVAMENTE\n'+"1)Cargar una ubicacion fija con nombre (N)"+"\n"+
                    "2)Cargar una ubicación fija con direccion(D)")
                    cargaubi=cargaubi.upper()
            if cargaubi=="N":
                ubiViaje=input('\nIngrese el nombre del lugar al cual quiere dirigirse\nPor ejemplo: H1   ')
                ubiViaje=ubiViaje.upper()
                exist=Search(Hash_Fijas, ubiViaje)
                while exist==False:
                    print('La ubicacion ingresada no está registrada\nIntente nuevamente con otra.')
                    ubiViaje=input('\nIngrese el nombre del lugar al cual quiere dirigirse\nPor ejemplo: K3   ')
                    ubiViaje=ubiViaje.upper()
                    exist=Search(Hash_Fijas, ubiViaje)
                pos=UberHash(ubiViaje)
                if len(Hash_Fijas[pos])==1:
                    DireccionViaje=Hash_Fijas[pos][0][1]
                   

                elif len(Hash_Fijas[pos])>1:
                    for i in range(0, len(Hash_Fijas[pos])):
                        if Hash_Fijas[pos][i][0]==ubiViaje:
                            DireccionViaje=Hash_Fijas[pos][i][1]   #DIRECCIÓN DEL LUGAR 
                            

            if cargaubi=='D':
                DireccionViaje=pedir_ubicacion(Lista_Calles)   #DIRECCION INGRESADA POR USUARIO

            create_trip(AutosCargados, USUARIO, DireccionPersona, Lista_nodos,Lista_Calles)



