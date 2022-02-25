import Paciente

def menu():
 i=0
 while True:
    
    print("------------------Bienvenido------------------")
    print ("Digite 1 si quieres agregar una cita ")
    print ("Digite 2 si quieres  buscar citas  ")
    print ("Digite 3 si quieres eliminar  citas  ")
    print ("Digite 4 si quieres VER las citas ")
    print ("Digite 5 si quieres SALIR   ")
    a = int(input())
    if a == 1:
        i=i+1
        Paciente.agregar(i)
        
    elif a == 2:
        Paciente.buscar()
    elif a ==3:
        Paciente.borrar()
    elif a ==4:
        Paciente.ver()
    else:
        break
    
