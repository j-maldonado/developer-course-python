#convertir los segundos ingresados a minutos correspondientes

seg=int(input("ingrese cantidad de segundos "))
minutos=0

while seg >= 60:
    seg = seg-60
    minutos = minutos+1
    
print("los segundos ingresados son",minutos,"minutos y", seg, "segundos")
