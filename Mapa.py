from Cidade import Cidade
from Adjacentes import Adjacentes

class Mapa:
    portoUniao = Cidade("Porto União", 203)
    pauloFrontin = Cidade("Paulo Frontin", 172)
    canoinhas = Cidade("Canoinhas", 141)
    irati = Cidade("Irati", 139)
    palmeira = Cidade("Palmeira", 59)
    campoLargo = Cidade("Campo Largo", 27)
    curitiba = Cidade("Curitiba", 0)
    balsaNova = Cidade("Balsa Nova", 41)
    araucaria = Cidade("Araucária", 23)
    saoJose = Cidade("São José dos Pinhais", 13)
    contenda = Cidade("Contenda", 39)
    mafra = Cidade("Mafra", 94)
    tijucas = Cidade("Tijucas do Sul", 56)
    lapa = Cidade("Lapa", 74)
    saoMateus = Cidade("São Mateus do Sul", 123)
    tresBarras = Cidade("Três Barras", 131)
    
    portoUniao.addCidadeAdjacente(Adjacentes(pauloFrontin, 46))  
    portoUniao.addCidadeAdjacente(Adjacentes(canoinhas, 78))
    portoUniao.addCidadeAdjacente(Adjacentes(saoMateus, 87))
       
    pauloFrontin.addCidadeAdjacente(Adjacentes(portoUniao, 46))
    pauloFrontin.addCidadeAdjacente(Adjacentes(irati, 75))
    
    canoinhas.addCidadeAdjacente(Adjacentes(portoUniao, 78))
    canoinhas.addCidadeAdjacente(Adjacentes(tresBarras, 12))
    canoinhas.addCidadeAdjacente(Adjacentes(mafra, 66))
    
    irati.addCidadeAdjacente(Adjacentes(pauloFrontin, 75))
    irati.addCidadeAdjacente(Adjacentes(palmeira, 75))
    irati.addCidadeAdjacente(Adjacentes(saoMateus, 57))
    
    palmeira.addCidadeAdjacente(Adjacentes(irati, 75))
    palmeira.addCidadeAdjacente(Adjacentes(saoMateus, 77))
    palmeira.addCidadeAdjacente(Adjacentes(campoLargo, 55))
    
    campoLargo.addCidadeAdjacente(Adjacentes(palmeira, 55))
    campoLargo.addCidadeAdjacente(Adjacentes(balsaNova, 22))
    campoLargo.addCidadeAdjacente(Adjacentes(curitiba, 29))
    
    curitiba.addCidadeAdjacente(Adjacentes(campoLargo, 29))
    curitiba.addCidadeAdjacente(Adjacentes(balsaNova, 51))
    curitiba.addCidadeAdjacente(Adjacentes(araucaria, 37))
    curitiba.addCidadeAdjacente(Adjacentes(saoJose, 15))
    
    balsaNova.addCidadeAdjacente(Adjacentes(curitiba, 51))
    balsaNova.addCidadeAdjacente(Adjacentes(campoLargo, 22))
    balsaNova.addCidadeAdjacente(Adjacentes(contenda, 19))
    
    araucaria.addCidadeAdjacente(Adjacentes(curitiba, 37))
    araucaria.addCidadeAdjacente(Adjacentes(contenda, 18))
    
    saoJose.addCidadeAdjacente(Adjacentes(curitiba, 15))
    saoJose.addCidadeAdjacente(Adjacentes(tijucas, 49))
    
    contenda.addCidadeAdjacente(Adjacentes(balsaNova, 19))
    contenda.addCidadeAdjacente(Adjacentes(araucaria, 18))
    contenda.addCidadeAdjacente(Adjacentes(lapa, 26))

    mafra.addCidadeAdjacente(Adjacentes(tijucas, 99))
    mafra.addCidadeAdjacente(Adjacentes(lapa, 57))
    mafra.addCidadeAdjacente(Adjacentes(canoinhas, 66))
    
    tijucas.addCidadeAdjacente(Adjacentes(mafra, 99))
    tijucas.addCidadeAdjacente(Adjacentes(saoJose, 49))

    lapa.addCidadeAdjacente(Adjacentes(contenda, 26))
    lapa.addCidadeAdjacente(Adjacentes(saoMateus, 60))
    lapa.addCidadeAdjacente(Adjacentes(mafra, 57))
    
    saoMateus.addCidadeAdjacente(Adjacentes(palmeira, 77))
    saoMateus.addCidadeAdjacente(Adjacentes(irati, 57))
    saoMateus.addCidadeAdjacente(Adjacentes(lapa, 60))
    saoMateus.addCidadeAdjacente(Adjacentes(tresBarras, 43))
    saoMateus.addCidadeAdjacente(Adjacentes(portoUniao, 87))
    
    tresBarras.addCidadeAdjacente(Adjacentes(saoMateus, 43))
    tresBarras.addCidadeAdjacente(Adjacentes(canoinhas, 12))


