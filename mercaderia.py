class Mercaderia:
    id = "" ## codigo Identificador de la mercaderia
    descripcion = "" ## Descripción que tiene la mercaderia
    peso = 0 ## Peso que tiene la mercaderia
    valorFOB = 0 ## valor FOB que tiene la mercaderia
    type = "" ## Tipo de mercaderia

    ## Método constructor
    def __init__(self, id, descripcion, peso, valorFOB):
        self.id = id
        self.descripcion = descripcion
        self.peso = peso
        self.valorFOB = valorFOB
    
    ## GETTERS

    def getId(self):
        return self.id
    
    def getDescripcion(self):
        return self.descripcion

    def getPeso(self):
        return self.peso

    def getValorFOB(self):
        return self.valorFOB

    def getType(self):
        return self.type

    ## SETTERS

    def setId(self, id):
        self.id = id

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def setPeso(self, peso):
        self.peso = peso

    def setValorFOB(self, valorFOB):
        self.valorFOB = valorFOB

    def setType(self, type):
        self.type = type