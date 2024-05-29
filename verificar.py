import getpass

validation = input("Ingrese el correo electrónico: ")
correo = "gossos1029@gmail.com"
contrasena = "Gossos1029"

if validation == correo:
    password_input = getpass.getpass("Ingrese su contraseña: ")

    if password_input == contrasena:
        print("Correo electrónico y contraseña válidos")
        print("Gracias por ser de gossos1029.")
        print("Envía un mensaje con tu nombre y las credenciales correspondientes:")
        print("Número pin: 39023")
        print("Tu nombre, puesto y dónde vives.")
    else:
        print("Contraseña incorrecta")
else:
    print("Correo electrónico no válido")
