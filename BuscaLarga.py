from Fila import Fila

#com objetivo

class Largura:
    
    def __init__(self,inicio,objetivo):
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo
        self.fronteira = Fila(10)
        self.fronteira.adicionar(inicio)
        self.achou = False
        
    def Buscar(self):
         init = self.fronteira.getInicio()
         print('inicio da fila: {}'.format(init.nome))
         self.fronteira.retirar()
         print('retirado: {}'.format(init.nome))
            
         if init == self.objetivo:
             self.achou = True
                 
         else:
        
            for a in init.adjacentes:
                if a.cidade.visitado != True:
                    a.cidade.visitado = True
                    self.fronteira.adicionar(a.cidade)
                    print('adjacentes: {}'.format(a.cidade.nome))
            
           
            if not self.fronteira.vazia():
               Largura.Buscar(self)
        
from Mapa import Mapa
mapa = Mapa()

largura = Largura(mapa.a,mapa.b)
largura.Buscar()


'''


from Fila import Fila

#sem objetivo

class Largura:
    
    def __init__(self,inicio,objetivo):
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo
        self.fronteira = Fila(10)
        self.fronteira.adicionar(inicio)
        self.achou = False
        
    def Buscar(self):
            init = self.fronteira.getInicio()
            print('inicio da fila: {}'.format(init.nome))
            self.fronteira.retirar()
            print('retirado: {}'.format(init.nome))
        
            for a in init.adjacentes:
                if a.cidade.visitado != True:
                    a.cidade.visitado = True
                    self.fronteira.adicionar(a.cidade)
                    print('adjacentes: {}'.format(a.cidade.nome))
            
           
            if not self.fronteira.vazia():
               Largura.Buscar(self)
        
from Mapa import Mapa
mapa = Mapa()

largura = Largura(mapa.a,mapa.b)
largura.Buscar()

'''