import math

def volumen(radio, altura):
    v=math.pi*math.pow(radio,2)*altura
    return v
def area(radio, altura):
    a=2*math.pi*radio*altura + 2*math.pi*math.pow(radio,2)
    return a



def main():
    #escribe tu código abajo de esta línea
    
    r=float(input('Ingrese un radio: '))
    h=float(input('Ingrese una altura: '))

    if r>=0 and h>=0:
        calculov=volumen(r,h)
        calculoa=area(r,h)

        print(round(calculov, 2))
        print(round(calculoa,2))

    

if __name__=='__main__':
    main()
