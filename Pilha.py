class Pilha:
    
    def __init__(self,tamanho):
        
        self.tamanho = tamanho
        self.cidades = []
        self.topo = -1
        
    def empilhar(self, cidade):
        
        if not Pilha.PilhaCheia(self):
         self.topo+=1
         self.cidades.append(cidade)
         
        else:
             print("Pilha cheia")


    def desempilhar(self):
    
     if not Pilha.PilhaVazia(self):
        
        self.cidades.pop(self.topo)
        self.topo -= 1
        
     else:
        print("pilha vazia")
        return None
      
    def getTopo(self):
    
     return self.cidades[self.topo]

    def PilhaVazia(self):
     return self.topo == -1

    def PilhaCheia(self):
     return self.topo >= self.tamanho - 1 
 


'''LINHA 9

o topo indica se existe ciade atribuidas, quantas,  e a suas posições
self.cidades[self.topo] = cidade:
self.cidades[self.topo] indica a posição do vetor, ex:
se o tamanho for 5, significa que: self.cidades = [5]. Ao executar a função 
empilhar, self.cidades[self.topo] é igual a self.cidades[0] = cidade, logo,
a posição 0 do vetor cidades armazena cidade. ex:
lista = 5
lista[0] = "montes claros" '''

'''LINHA 19  MEU MÉTODO
   
       if not Pilha.PilhaVazia(self):
        
        self.cidades[self.topo] = None
        self.topo-=1  
        
       else:
           print("pilha vazia")'''      
           
'''indices de 0 até 4'''

