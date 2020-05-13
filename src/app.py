import json
from DataStructures import Queue
from sms import send

# there queue has to be declared globally (outside any other function)
# that way all methods have access to it
#queue = Queue(mode="FIFO")

def print_queue():  
    # you must print on the console the entire queue list
    print("Printing the entire list...")
    print(queue.get_queue())

def add(item):
    agregando=queue.enqueue(item)
    ##Tamaño de cola##
    size=sizeCola=queue.size()
    size=size-1
    ##Mensaje de encolamiento##
    mensaje=item+', tienes: '+str(size)+" Clientes antes que tu"
    enviando_mensaje=send(mensaje)
    print(item+", tienes: "+str(size)+" Clientes antes que tu")
    pass

def dequeue():
    cliente=queue.dequeue()
    mensaje='Es el  turno para almorzar de: '+cliente
    enviando_mensaje=send(mensaje)
    print('Le toca turno a: '+cliente)
    pass

def sizequeue():
    sizeCola=queue.size()
    print(sizeCola)
    pass

def save():
    cola_json=queue.save_json()
    pass

def load():
    load_cola_json=queue.load_json()
    pass 
        
    
print("\nHello, this is the Command Line Interface for a Queue Managment application.")
stop = False
while stop == False:
    
    print('''
What would you like to do (type a number and press Enter)?
- Type 1: Que tipo de cola quiere crear?
- Type 2: For adding someone to the Queue.
- Type 3: For removing someone from the Queue.
- Type 4: For printing the current Queue state.
- Type 5: To export the queue to the queue.json file.
- Type 6: To import the queue from the queue.json file.
- Type 7: Cola Size.
- Type 8: To quit
    ''')

    option = int(input("Enter a number:"))
    # add your options here using conditionals (if)    
    try: 
        if option == 1:
            Tipo=input("\n1.-FIFO \n 2.-LIFO \n")
            if "1" in Tipo:
                Tipo="FIFO"
                queue = Queue(mode=Tipo)
            elif "2" in Tipo:
                Tipo="LIFO"
                queue = Queue(mode=Tipo)
            else:
                Tipo="FIFO"
                queue = Queue(mode=Tipo)
                
        elif option == 2:
            user=input("Agregue el nombre del usuario a la cola: ")
            add(user)      
        
        elif option == 3:
            dequeue()
        
        elif option == 4:
            print_queue()
        
        elif option == 5:
            save()
        
        elif option == 6:
            Tipo=input("Que tipo de cola desea cargar?: \n 1.-FIFO \n 2.-LIFO\n")
            if "1" in Tipo:
                Tipo="FIFO"
                queue = Queue(mode=Tipo)
                load()

            elif "2" in Tipo:
                Tipo="LIFO"
                queue = Queue(mode=Tipo)
                load()
        
            else:
                Tipo="FIFO"
                queue = Queue(mode=Tipo)
                load()
            
        elif option == 7:
            sizequeue()
                        
        elif option == 8:
            print("Bye bye!")
            stop = True
        else:
            print("Invalid option "+str(option))
    except:
                    print('No ha creado una cola aun')