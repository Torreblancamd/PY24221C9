

def saludar_usuarios( nombre ):      
    print("Hola Usuario: ", nombre)



# PARAMETROS
saludar_usuarios("Juan")
saludar_usuarios("Pedro")



#
def mayor_de_edad( edad_usuario ):

    if type(edad_usuario) == int:
        if edad_usuario >= 18:
            print("Bienvenido al sistema")
        else:
            print("No podes ingresar")
    else:
        print("No se acepta el tipo de dato: ", type(edad_usuario))


mayor_de_edad(20)
mayor_de_edad(10)
mayor_de_edad("Juan")