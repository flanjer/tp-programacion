nombre_de_usuario = input("NOMBRE DE USUARIO: ")
print ("Hola",nombre_de_usuario)
#PUNTO 2
A=int (input ("INGRESE UN NUMERO: "))
print (A)
B=int (input ("INGRESE OTRO NUMERO: "))
print (B)
C= A+B
print ("LA SUMA DE A+B ES",C)
#PUNTO 3
#datos usuario
nombre = input ("INGRESE SU NOMBRE: ")
num_comision = input ("ingrese el numero de comision: ")
asignatura = input ("ingrese asignatura: ")
presente = input("¿Estuvo presente? (Sí/No): ")
#registro
print (nombre)
print (num_comision)
print (asignatura)
print (presente)
#PUNTO 4
lado = input("Ingrese la longitud del lado del cuadrado: ")
lado = int (lado)
area = lado * lado
print (area) 
#PUNTO 5
ladoA = float(input("Ingrese la longitud del primer lado del rectángulo: "))
ladoB = float(input("Ingrese la longitud del segundo lado del rectángulo: "))
area = ladoA * ladoB
print("La superficie del rectángulo con lados", ladoA, "y", ladoB, "es", area)
#PUNTO 6

base = float(input("Ingrese la base del triangulo: "))
altura = float(input("Ingrese la altura: "))
area = (base * altura) / 2
print("La superficie del triangulo con base ", base, "y altura ", altura, "es", area)
#PUNTO 7
nombre_producto = str (input("ingrese el nombre del producto ")) 
precio = float (input("ingrese el precio "))
precio_iva = precio * 1.21
print ("el precio de ", nombre_producto, " con iva es ",precio_iva)
#PUNTO 8
alumno = input ("nombre del alumno: ")
apellido = input ("Apellido: ")
nota1 = float (input("ingrese primer nota: "))
nota2 = float (input("ingrese segunda nota: "))
nota3 = float (input("ingrese tercer nota: "))
promedio = (nota1 + nota2 + nota3) / 3
print ("tu promedio es", promedio)
#PUNTO 9
NOMBRE = input ("nombre: ")
edad = int(input("Introduce tu edad: "))
Edad_futura  = edad + 10
print (Edad_futura)