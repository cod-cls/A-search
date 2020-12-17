from Pilha import Pilha

class Profundidade:
    def __init__(self,inicio,objetivo):
        self.inicio = inicio
        self.objetivo = objetivo
        self.fronteira = Pilha(20)
        self.inicio.visitado = True
        self.fronteira.empilhar(inicio)
        self.achou = False
        
    def Busca(self):
        
        topo = self.fronteira.getTopo()
        print('topo: {}'.format(self.fronteira.getTopo().nome))
        '''se a cidade que está no topo da pilha neste momento for a que você estiver procurando então self.achou é verdadeiro
           e essa é uma forma de fazer com que a cidade objetivo estivesse na pilha para depois toda a pilha ser desempilhada'''
        if topo == self.objetivo:
         self.achou = True
         '''a diferença do else é que sem ele o for iria contuar rodando quando chegasse na cidade destino além de negar adjacentes que não forem
            o objetivo. Com o else não irá acontecer o for quandoo objetvo estiver no topo'''
        else:
         #precisamos verificar os adjacentes da cidade inicio e depois as cidades do topo
         for a in topo.adjacentes:
             print('topo continua com: {}'.format(self.fronteira.getTopo().nome))
             '''o comando abaixo fará: quando for achado a cidade objetivo, o for que continuará rodando não aceite mais alguma cidade sequer.
                se não existisse essa linha abaixo mas ainda com o else (linha 22), o for ainda continuaria rodando'''
             if not self.achou == True:
                #precisa-se de escolher qualquer cidade adjacente  não visitada da cidade que está no topo
                if not a.cidade.visitado == True:
                  a.cidade.visitado = True
                  #depois necessit-se empilha-la
                  self.fronteira.empilhar(a.cidade)
                  #chamar a função Busca
                  Profundidade.Busca(self)
                '''se não existir cidades adjacentes que não foram visitadas talvez exista na cidade que estava no topo anteriormente;
                o for irá parar quando uma cidade não tiver mais adjacentes que não foram visitados
                então para percorrer todo o caminho possível temos que verificar isso em todas as cidades(topo) e desempilhar aquelas cidades
                que possui adjacentes todos visitados'''
        print('desempilhado: {}'.format(self.fronteira.getTopo().nome))
        self.fronteira.desempilhar()
     
        
            
from Mapa import Mapa
mapa = Mapa()
profundidade = Profundidade(mapa.a , mapa.b)
profundidade.Busca()