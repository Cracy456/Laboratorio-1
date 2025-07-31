#Parte 1 de laboratorio
#1 y 2
lista = ["Ana", "Luis", "Pedro"] 
lista.remove("Ana")
#3
while True:
 print("Hola")
 break

#4
diccionario = {
    "Nombre": "Mario Rolando",
    "Edad": "19",
    "Carrera" : "Ingerienria en Sistemas"
}

#5
print("Una lista es mutable (se puede cambiar), y una tupla es inmutable (no se puede cambiar).")

#parte 2 laboratorio

#1
num = 1
sum = 0
while num > 0:
    num = int(input("Ingrese un numero, el programa se detendra al ingresar 0: "))
    sum += num
    print (f"La suma es {sum}")

#2
lista = [10,20,30,40]
m = 2
for i in lista:
    mul = m * i
    print(mul)

#3
producto = {
    "Nombre": "Platanos",
    "Precio": "Q3.65",
    "Stock" : "165"
}