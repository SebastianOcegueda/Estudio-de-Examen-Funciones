def piescm(opcion, cantidad):
    if opcion==1:
        conver=cantidad/.0328
        return conver
    elif opcion==2:
        conver=cantidad*2.54
        return conver
    else:
        conver=cantidad*91.44
        return conver


def main():
    #escribe tu código abajo de esta línea
    
    a=int(input("Selecciona 1, 2 o 3: "))
    b=int(input('Cuanto quieres convertir: '))

    if 0<a<3 and b>=0:
        calculo= piescm(a,b)
        print(round(calculo,2))
    else:
        print('Error')

if __name__=='__main__':
    main()
