class Viaje:
    id = 0 ## codigo Identificador
    nombreBarco = "" ## Nombre del barco
    origen = "" ## Lugar de origen
    destino = "" ## Lugar de destino
    fechaPartida = "" ## Fecha de partida
    containers = [] ## Lista de contenedores

    def __init__(self, id, nombreBarco, origen, destino, fechaPartida, containers):
        self.id = id
        self.nombreBarco = nombreBarco
        self.origen = origen
        self.destino = destino
        self.fechaPartida = fechaPartida
        self.containers = containers
        
    ## GETTERS

    def getId(self):
        return self.id

    def getNombreBarco(self):
        return self.nombreBarco
        
    def getOrigen(self):
        return self.origen

    def getDestino(self):
        return self.destino

    def getFechaPartida(self):
        return self.fechaPartida
    
    def getContainers(self):
        return self.containers
    
    ## SETTERS

    def setContainers(self, containers):
        self.containers = containers

    def setId(self, id):
      self.id = id

    def setNombreBarco(self, nombreBarco):
      self.nombreBarco = nombreBarco

    def setDestino(self, destino):
      self.destino = destino

    def setFechaPartida(self, fechaPartida):
      self.fechaPartida = fechaPartida

    ## OTROS METODOS

    ## Mostrar reporte
    def MostrarReporte(self):
      for container in self.containers:
        container.MostrarManifiesto()