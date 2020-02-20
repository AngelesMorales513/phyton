#aceptado_cine.py  
edad = int(input("¿Cuántos años tiene? "))
a = int(input("Que clasificacion desea ver?")) 
if edad > 1:
    if a == 1:
        print("Puede ver la pelicula")
elif edad > 1:
        if a == 2:
            print("Puede ver la pelicula")
elif edad > 18:
    if a == 3:
         print("Puede ver la pelicula")
else:
    print("Tiene que ser mayor de edad")
print("¡Hasta la próxima!")
