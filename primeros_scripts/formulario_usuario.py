#Desarrollar un script llamado
#formulario_usuario.py
#que pida:
#Nombre
#Edad
#Ciudad
#Profesión
#Años de experiencia
#Y devuelva una presentación estructurada como:
#Nombre: LauraEdad: 29Ciudad: RosarioProfesión: Analista de datosExperiencia: 3 años

nombre = input("dime tu nombre ")
edad = input("dime tu edad ")
ciudad = input("¿dónde vives? ")
profesión = input("¿a qué te dedicas? ")
años_de_experiencia = input("¿años de experiencia? ")

print(f"Te llamas, {nombre}, tienes {edad} años, vives en {ciudad}, eres {profesión}, y tienes {años_de_experiencia} años de seniority.")
