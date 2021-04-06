# FUNCION PARA CALCULAR EL PERCENTIL 

def percentil():
    L=[]
    n=int(input("Ingresar la cantidad de elementos de la lista: "))
    for i in range(n):
        print("Ingrese la posición ",i+1,": ")
        L.append(float(input()))
    #print(L)
    L.sort()
    #print(L)
    print("Ingrese el percentil que desea obtener que debe estar entre 0 y 1:")
    k=float(input())
    if  0<k<1:
        z = (n+1)*k
        a = int(z)
        b = round((z-a),2)
    
    p = L[a-1] + b*(L[a]-L[a-1])
    print("El percentil ",k," es: ",p)
    
# FUNCION PARA HALLAR EL TIPO DE DISTRIBUCION

def cAsimetria():
    L=[]
    n=int(input("Ingresar la cantidad de elementos de la lista: "))
    for i in range(n):
        print("Ingrese la posición ",i+1,": ")
        L.append(float(input()))
    
    s=0
    for x in L:
        s = s+x
    media = s/n
    print("El promedio de la lista es: ",media)
    
    from math import sqrt
    c =0
    for j in L:
        c = c+j**2
    v = (c - n*(media**2))/(n-1)
    des = round(sqrt(v),2)
    
    a =0
    for h in L:
        a = a + (h-media)**3
    A = a/(n*(des**3))
    print(A)
    
    if A>0:
        print("Presenta distribución asimétrica positiva")
    else:
        if A==0:
            print("Presenta distribución simétrica")
        else:
            print("Presenta distribución asimétrica negatica")
    
# FUNCION PARA SABER EL TIPO DE CURTOSIS

def curtosis():
    L=[]
    n=int(input("Ingresar la cantidad de elementos de la lista: "))
    for i in range(n):
        print("Ingrese la posición ",i+1,": ")
        L.append(float(input()))
    
    s=0
    for x in L:
        s = s+x
    media = s/n
    print("El promedio de la lista es: ",media)
    
    from math import sqrt
    c =0
    for j in L:
        c = c+j**2
    v = (c - n*(media**2))/(n-1)
    des = round(sqrt(v),2)
    
    a =0
    for h in L:
        a = a + (h-media)**4
    Cu = (a/(n*(des**4)))- 3
    print(Cu)
    
    if Cu>0:
        print("Presenta distribución Leptocúrtica")
    else:
        if Cu==0:
            print("Presenta distribución Mesocúrtica")
        else:
            print("Presenta distribución Platicúrtica")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    