
def calcular_interes( monto , cuotas):

    interes = 0

    if cuotas == 1:
        interes = monto * 0.10
        return interes        
    elif cuotas == 3:
        interes = monto * 0.30
        return interes
    elif cuotas == 6:
        interes = monto * 0.60
        return interes
    elif cuotas == 12:
        interes = monto * 0.90
        return interes



def mostrar_datos_prestamo( monto , cuotas , total ):
        print("Detalle del prestamo")
        print("Monto solicitado: ", monto)
        print("Cuotas: ", cuotas)
        print("Total: ",  total)



print("Bienvenido/a a Prestamo Now")
monto = input("Ingrese el monto que quiere solicitar")
monto = int(monto)
cuotas = input("Ingrese la cantidad de cuotas: 1, 3, 6 o 12")
cuotas = int(cuotas)

interes_calculado = calcular_interes(monto,cuotas)
total = monto + interes_calculado

mostrar_datos_prestamo( monto , cuotas , total )