class Fila:
    
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.listaFila = [None] * tamanho
        self.inicio = 0
        self.fim = -1
        self.elementos = 0
        
    def prox(self, iorf):       
        if iorf == self.tamanho - 1:
            return 0
        else: return iorf + 1
             
    def adicionar(self,cidade):
        prox = Fila.prox(self,self.fim)  
        if self.listaFila[prox] == None: 
            self.fim = prox
            self.listaFila[self.fim] = cidade
            self.elementos += 1       
        else: print('Fila cheia')
            
    def retirar(self):
        if self.listaFila[self.inicio] != None:
            self.listaFila[self.inicio] = None 
            prox = Fila.prox(self,self.inicio) 
            self.inicio = prox
            self.elementos -= 1
        else: print('Fila vazia')
        
    def getInicio(self):
        return self.listaFila[self.inicio]
    
    def getElementos(self):
        return self.elementos
    
    def vazia(self):
        if self.elementos == 0:
            return True
        else: False
        
    def cheia(self):
        if self.elementos == self.tamanho:
            return True
        else: False
'''
fila = Fila(3)
fila.adicionar('a')
fila.adicionar('b')
fila.adicionar('c')
fila.adicionar('d')
fila.retirar()
fila.listaFila
fila.inicio
fila.fim
fila.elementos

 FILA CIRCULAR:
    fila que possui um tamanho limitado e alocação dinamica, em que do final da 
    lista passa para o inicio da lista.'''
        
        
        
       