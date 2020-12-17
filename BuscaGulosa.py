from VetorOrdenado import Ordenado


class Gulosa:
    
    def __init__(self,objetivo):
        self.objetivo = objetivo
        self.achou = False
        
    def Buscar(self, atual):
      print("\033[0;32m" + 'cidade atual: {}'.format(atual.nome) + "\033[0;0m")
      if atual == self.objetivo:
          self.achou = True
      else:   
        atual.visitado = True
        self.fronteira = Ordenado(len(atual.adjacentes))
        for a in atual.adjacentes:
            if not a.cidade.visitado == True:
                print('adjacentes: {} - distancia: {}'.format(a.cidade.nome,a.distanciaAEstrela))
                a.cidade.visitado = True
                self.fronteira.inserir(a.cidade)
        if not self.fronteira.vazio():
            Gulosa.Buscar(self,self.fronteira.getPrimeiro())
                


from Mapa import Mapa
mapa = Mapa()
gulosa = Gulosa(mapa.curitiba)
gulosa.Buscar(mapa.portoUniao)

'''
from VetorOrdenado import Ordenado


class Gulosa:
    
    def __init__(self,inicio,objetivo):
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo
        self.lista = []
        self.vetor = Ordenado(5)
        self.lista.append(self.inicio)      
        
    def Buscar(self):
        
      print('ultimo addicionado: {}'.format(self.lista[-1].nome)) 
      if not self.objetivo.visitado == True:
        adj = self.lista[-1].adjacentes
        x = Ordenado(5)
        for a in adj:
            if not a.cidade.visitado == True:
                print('adjacente: {} distancia: {}'.format(a.cidade.nome, a.cidade.cidadeObjetivo))
                a.cidade.visitado = True
                x.inserir(a.cidade)    
        self.lista.append(x.getPrimeiro())
        Gulosa.Buscar(self)
        
from Mapa import Mapa
mapa = Mapa()
gulosa = Gulosa(mapa.a, mapa.p)
gulosa.Buscar()
'''