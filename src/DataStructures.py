import json

class Queue:

    def __init__(self, mode, current_queue=[]):
        self._queue = current_queue
        self._mode = mode 
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        #if mode is None:
        #    raise "Please specify a queue mode FIFO or LIFO"
        #else:
        #    self._mode = mode 
        
    ################ ENCOLAR  ##########################
    def enqueue(self, item):
        self._queue.append(item)
    
    ################ DESENCOLAR  #######################
    def dequeue(self):
        try:
            if "FIFO" in self._mode:
                cliente= self._queue.pop(0)
                return cliente
            elif "LIFO" in self._mode:   
                cliente= self._queue.pop()
                return cliente
        except:
            raise ValueError("La cola está vacía")

    
    ################ OBTENER COLA  ##########################
    def get_queue(self):
        
    ################ COLA-FIFO   ############################
        if "FIFO" in self._mode:
            return self._queue
        
    ################ COLA-LIFO   ############################
        elif "LIFO" in self._mode:
            i=len(self._queue)-1
            #colaLIFO=[]
            # for item in range(len(self._queue)):
            #     #print(self._queue[i])
            #     colaLIFO.append(self._queue[i])
            #     i=i-1
            colaLIFO=[]
            for item in reversed(self._queue):
                colaLIFO.append(item)
            return colaLIFO
    ################ OBTENER TAMAÑO DE COLA  #################
    def size(self):
        cola=self._queue
        cola_size=len(cola)
        return cola_size
        pass
    ################ GUARDAR EN ARCHIVO JSON COLA ############
    def save_json(self):
        cola=self._queue
        
        if "FIFO" in self._mode:
            with open('clientesFIFO.json', 'w') as file:
                json.dump(cola, file, indent=1)
                print(cola)
            print('\n Archivo creado ---> '+'clientesFIFO.json')
            
        elif "LIFO" in self._mode:
            colaLIFO=[]
            for item in reversed(self._queue):
                colaLIFO.append(item)
    ################ ############### ##########################
            with open('clientesLIFO.json', 'w') as file:
                json.dump(colaLIFO, file, indent=1)
                print(cola)
            print('\n Archivo creado ---> '+'clientesLIFO.json')
    ################ LEER ARCHIVO JSON E INCORPORAR COLA  ######
    def load_json(self):
        if "FIFO" in self._mode:
            with open('clientesFIFO.json') as file:
                self._queue = json.load(file)
                print('\n Archivo CARGADO FIFO---> '+'clientesFIFO.json')
        elif "LIFO" in self._mode:
            with open('clientesLIFO.json') as file:
                self._queue = json.load(file)
                print('\n Archivo CARGADO LIFO---> '+'clientesLIFO.json')