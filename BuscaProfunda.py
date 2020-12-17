
from Pilha import Pilha

#sem objetivo

class Profundidade:
    
    def __init__(self, inicio, objetivo):        
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo 
        self.fronteira = Pilha(17)
        self.fronteira.empilhar(inicio)
        self.achou = False
  
    def buscar(self):
            topo = self.fronteira.getTopo()
            print('Topo: {}'.format(topo.nome))
        
            for a in topo.adjacentes:
                
                   
                    if a.cidade.visitado == False:
                        print('já visitado: {}'.format(a.cidade.nome))
                        a.cidade.visitado = True
                        self.fronteira.empilhar(a.cidade)
                        Profundidade.buscar(self)      
            print('desempilhou:{}'.format(self.fronteira.getTopo().nome))
            self.fronteira.desempilhar()
  
        
from Mapa import Mapa
mapa = Mapa()
profundidade = Profundidade(mapa.a , mapa.b)
profundidade.buscar()

''' 

from Pilha import Pilha

#com objetivo

class Profundidade:
    
    def __init__(self, inicio, objetivo):        
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo 
        self.fronteira = Pilha(17)
        self.fronteira.empilhar(inicio)
        self.achou = False
  
    def buscar(self):
        topo = self.fronteira.getTopo()
        print('Topo: {}'.format(topo.nome))
        
        if topo == self.objetivo:
            self.achou = True
        else:
            for a in topo.adjacentes:
                if self.achou == False:
                    print('Verificando se já visitado: {}'.format(a.cidade.nome))
                    if a.cidade.visitado == False:
                        a.cidade.visitado = True
                        self.fronteira.empilhar(a.cidade)
                        Profundidade.buscar(self)      
        print('desempilhou:{}'.format(self.fronteira.getTopo().nome))
        self.fronteira.desempilhar()
  
        
from Mapa import Mapa
mapa = Mapa()
profundidade = Profundidade(mapa.a , mapa.b)
profundidade.buscar()
'''