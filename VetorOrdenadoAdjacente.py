class OrdenadoAdjacente:
    
    def __init__(self,tamanho):
     
        self.vetor = [None] * tamanho
        self.elementos = 0
        
    def cheio(self):
        if self.vetor[-1] != None:
            return True
        else: return False
        
    def vazio(self):
        if self.vetor[0] == None:
            return True
        else: return False
        
    
    def inserir(self,adjacente):
        
        if OrdenadoAdjacente.cheio(self):
            print('vetor está cheio')
        else:
            if OrdenadoAdjacente.vazio(self):
                self.vetor[0] = adjacente
            else:        
                index = self.elementos
                for a in range(self.elementos):
                   if adjacente.distanciaAEstrela <= self.vetor[a].distanciaAEstrela:
                      index = a
                      break
                if index == self.elementos:
                      self.vetor[index] = adjacente
                else:                  
                    for a in range(self.elementos - 1, index - 1, -1):
                        self.vetor[a + 1] = self.vetor[a]
                    self.vetor[index] = adjacente
                        
            self.elementos += 1
            
            
            
    def getPrimeiro(self):
        return self.vetor[0]
    
    def listar(self):
        for a in range(self.elementos):
            print('{} --> {}'.format(self.vetor[a].nome,self.vetor[a].cidadeObjetivo))
            
            



