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
        pass
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
            colaLIFO=[]
            for item in reversed(self._queue):
                colaLIFO.append(item)
            return colaLIFO
    ################ OBTENER TAMAÑO DE COLA  #################
    def size(self):
        cola=self._queue
        cola_size=len(cola)
        return cola_size
    ################ GUARDAR EN ARCHIVO JSON COLA ############
    def save_json(self):
        cola=self._queue
        cont=0
        diccFIFO={}
        for item in cola:
            diccFIFO.update({str(cont) : str(item)})
            cont=int(cont)
            cont=cont+1
        
        if "FIFO" in self._mode:
            with open('clientesFIFO.json', 'w') as file:
                json.dump(diccFIFO, file, indent=1)
            print('\n Archivo creado ---> '+'clientesFIFO.json')
            
        elif "LIFO" in self._mode:
            cont=0
            diccLIFO={}
            for item in reversed(self._queue):
                diccLIFO.update({str(cont) : str(item)})
                cont=int(cont)
                cont=cont+1
    ################ ############### ##########################
            with open('clientesLIFO.json', 'w') as file:
                json.dump(diccLIFO, file, indent=1)
            print('\n Archivo creado ---> '+'clientesLIFO.json')
    ################ LEER ARCHIVO JSON E INCORPORAR COLA  ######
    def load_json(self):
        if "FIFO" in self._mode:
            diccFIFO={}
            with open('clientesFIFO.json') as file:
                diccFIFO = json.load(file)
                print(diccFIFO)
                for item in diccFIFO:
                    self._queue.append(diccFIFO[item])
                print('\n Archivo CARGADO FIFO---> '+'clientesFIFO.json')
        elif "LIFO" in self._mode:
            diccLIFO={}
            colaLIFO=[]
            with open('clientesLIFO.json') as file:
                diccLIFO = json.load(file)
                for item in diccLIFO:
                    colaLIFO.append(diccLIFO[item])
                for valor in reversed(colaLIFO):
                    self._queue.append(valor)
                #print(colaLIFO)
                #print(self._queue)
                print('\n Archivo CARGADO LIFO---> '+'clientesLIFO.json')