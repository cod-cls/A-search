class Ordenado:
    
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
        
    
    def inserir(self,cidade):
        
        if Ordenado.cheio(self):
            print('vetor está cheio')
        else:
            if Ordenado.vazio(self):
                self.vetor[0] = cidade
            else:        
                index = self.elementos
                for a in range(self.elementos):
                   if cidade.distanciaObjetivo <= self.vetor[a].distanciaObjetivo:
                      index = a
                      break
                if index == self.elementos:
                      self.vetor[index] = cidade
                else:                  
                    for a in range(self.elementos - 1, index - 1, -1):
                        self.vetor[a + 1] = self.vetor[a]
                    self.vetor[index] = cidade
                        
            self.elementos += 1
            
            
            
    def getPrimeiro(self):
        return self.vetor[0]
    
    def listar(self):
        for a in range(self.elementos):
            print('{} --> {}'.format(self.vetor[a].nome,self.vetor[a].cidadeObjetivo))
            
            
            
            



'''
-------------------------------------------------------------------------------

minha forma 2: melhor tempo --> 0.038718223571777344

import time

class Ordenado:
    
    def __init__(self,tamanho):
        self.tamanho = tamanho
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
        
    
    def inserir(self,valor):
        
        if Ordenado.cheio(self):
            print('vetor está cheio')
        else:
            if Ordenado.vazio(self):
                self.vetor[0] = valor
            else:        
                self.vetor[self.elementos] = valor
                self.vetor = self.vetor[:self.elementos + 1]
                self.vetor.sort()
                self.vetor += (self.tamanho - self.elementos) * [None]
               
            self.elementos += 1
            


     

-------------------------------------------------------------------------------

minha forma 1: melhor tempo --> 0.04687237739562988

import time

class Ordenado:
    
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
        
    
    def inserir(self,valor):
        
        if Ordenado.cheio(self):
            print('vetor está cheio')
        else:
            if Ordenado.vazio(self):
                self.vetor[0] = valor
            else:        
                index = self.elementos
                for a in range(self.elementos):
                   if valor <= self.vetor[a]:
                      index = a
                      break
                if index == self.elementos:
                      self.vetor[index] = valor
                else:                  
                    for a in range(self.elementos - 1, index - 1, -1):
                        self.vetor[a + 1] = self.vetor[a]
                    self.vetor[index] = valor
                        
            self.elementos += 1

ordenado = Ordenado(3)  
ordenado.vetor
ordenado.inserir(3)   
ordenado.inserir(1)        
'''
       
                      
                
      
                  
        