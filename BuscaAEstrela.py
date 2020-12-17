from VetorOrdenadoAdjacente import OrdenadoAdjacente


class AEstrela:
    
    def __init__(self,objetivo):
        self.objetivo = objetivo
        self.achou = False
        
    def Buscar(self, atual):
      print("\033[0;32m" + 'cidade atual: {}'.format(atual.nome) + "\033[0;0m")
      if atual == self.objetivo:
          self.achou = True
      else:   
        atual.visitado = True
        self.fronteira = OrdenadoAdjacente(len(atual.adjacentes))
        for a in atual.adjacentes:
            if not a.cidade.visitado == True:
                print('adjacentes: {} - distancia: {}'.format(a.cidade.nome,a.distanciaAEstrela))
                a.cidade.visitado = True
                self.fronteira.inserir(a)
        if not self.fronteira.vazio():
            AEstrela.Buscar(self,self.fronteira.getPrimeiro().cidade)
                


from Mapa import Mapa
mapa = Mapa()
aestrela = AEstrela(mapa.curitiba)
aestrela.Buscar(mapa.portoUniao)