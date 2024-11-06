

#Funcion:suma_dos_numeros

def suma_dos_numeros( num_uno , num_dos):
    if type(num_uno) == int and type(num_dos) == int:
        print("La suma: ",  num_uno + num_dos )
    else:
        print("Tipo de dato incorrecto")


suma_dos_numeros( 40 , 20 )
suma_dos_numeros( 100 , 35 )
suma_dos_numeros( 73 , 11 )
suma_dos_numeros("Juan", "30")





def saludar_usuarios( nombre , apellido ):      
    print("Nombre: ", nombre , "Apellido: " , apellido)



# PARAMETROS
saludar_usuarios("Juan" , "Lopez")
saludar_usuarios("Pedro" , "Ramos")
saludar_usuarios("Jimenez" , "Analia")













