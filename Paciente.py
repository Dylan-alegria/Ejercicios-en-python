
Citas ={
    1122:["ID:",2,"mes", 2,"Dia:",9,"Hora:  ", "9am" "   Especialidad: ","odontologia" ],
    155:["ID:",2,"mes", 4,"Dia:",19,"Hora:  ", "9am" "   Especialidad: ","hola " ],
    113:["ID:",2,"mes",1,"Dia:",1,"Hora:  ", "10am" "   Especialidad: ","sangre "],
    991244:["ID:",3,"mes", 3,"Dia:",9,"Hora:  ", "9am" "   Especialidad: ","odontologia"],
    8888:["ID:",5,"mes",9,"Dia:",10,"Hora:  ", "10am" "   Especialidad: ","sangre "],
    8392:["ID:",77,"mes", 4,"Dia:",30,"Hora:  ", "9am" "   Especialidad: ","odontologia"]


}
def agregar (i):#funcion para agregar 
    #pide los datos, para luego  insertalo en diccionario 
    #los datos se insertaran como una lista para el mejor dominio de los datos 
    print("Digite la Cedula")
    cedula= int(input())
    print("Digite el mes de la Cita(numeros)")
    mes= int(input())
    print("Digite el dia de la Cita(numeros)")
    dia= int(input())
    print("Digite la Hora de la Cita ")
    hora= input()
    print("Digite la Especialidad ")
    especialidad = input()
    Citas[i]=["ID:",cedula,'Mes:',mes,"Dia:", dia ,"Hora:"+ hora +"   Especialidad:"+ especialidad ]
    

  

    
def buscar():#funcion para buscar en el diccionario buscar por medio de la llame 
    print ("Digite Dni")
    dni= int(input())
    d=Citas
    for i in Citas:
        d=Citas[i][1]
        if d == dni :
            print(i,Citas[i])
            
            
            
def borrar ():#funcion para  borrar  una cita por medio dela fecha y del mes 
    pi=[]#lista 
    print ('----------------ADVERTENCIA----------------')
    print ("si ingresas una fecha las Citas antes de esta se eliminaran  ")
    mes = int (input("Digite el mes "))
    dia = int (input("Digite el dia  "))

    for i in Citas: # recorre el diciionario 
      # a y b guarda  la llave  y la pocision del mes  
        a=Citas[i][3]#El mes  se guarda en esta posicion 
        b=Citas[i][5]      
        if a == mes and b< dia : #si el mes es igual y el dia menor que los digitados se meten a la lista 
          pi.append(i)#Los datos que pasan los dos if se guardan en la lista 
        if a<mes :# si el  mes es menor al digitado entrara a la lista 
          pi.append(i) 
          
    for we in pi :## este for recorre la lista de los datos que pasaron los if  
       Citas.pop(we)#los datos de la lista pi se borran 
       print("borrado con exito")

def ver ():
    for a in Citas:
        print(a,Citas[a])
        
    

       
       


          

    
        
  