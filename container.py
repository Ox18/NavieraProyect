class Container:
    id = "" ## codigo identificador del contenedor
    mercaderias = [] ## Lista de mercaderias

    def __init__(self, id):
        self.id = id
        self.mercaderias = []
  
    ## GETTERS

    def getId(self):
        return self.id
    
    def getMercaderias(self):
        return self.mercaderias
    
    ## SETTERS

    def setId(self, id):
        self.id = id

    def setMercaderias(self, mercaderias):
        self.mercaderias = mercaderias

    ## OTROS METODOS

    ## Metodo que me permite agregar más mercaderias a mi contenedor
    def AdicionarMercaderia(self, mercaderia):
      self.mercaderias.append(mercaderia)

    ## Metodo para mostrar en pantalla el manifiesto
    def MostrarManifiesto(self):
      pesoTotal = self.GetPesoTotal();
      precioFOBTotal = self.GetPrecioFOBTotal()
      volumenTotalLiquidos = self.getVolumenTotalLiquidos()
      cargaPeligrosa = self.esPeligroso()
      cantidadMercaderias = len(self.mercaderias)

      print("################################################")
      print("ID: " + self.getId() + " - Peso total: " + pesoTotal + " - precio FOB total: " + precioFOBTotal + " - Volumen total liquidos: " + volumenTotalLiquidos + " - carga peligrosa: " + cargaPeligrosa + " - Cantidad de mercaderias: " + cantidadMercaderias)

    ## Metodo para obtener el volumen total de los requerimientos
    def getVolumenTotalLiquidos(self):
      total = 0
      for mercaderia in self.mercaderias():
        if(mercaderia.getType() == "mercaderiaLiquida"):
          total += mercaderia.getVolumen()  
      return total

    ## Metodo para obtener el precio Fob total
    def GetPrecioFOBTotal(self):
      total = 0
      for mercaderia in self.mercaderias():
        total += mercaderia.getValorFOB()
      return total

    ## Metodo para obtener el peso total de los requerimientos
    def GetPesoTotal(self):
      total = 0
      for mercaderia in self.mercaderias:
        total += mercaderia.getPeso()
      return total

    ## Metodo para saber si el contenedor es peligroso
    def esPeligroso(self):
      peligroso = "NO"
      for mercaderia in self.mercaderias:
        if(mercaderia.getType() == "MercaderiaPeligrosa" and mercaderia.getNivelPeligrosidad() == 1):
          peligroso = "SI"
          break
      return peligroso
      
    def mostrarManifiestoCargas(self):
      print("Contenedor: " + self.getId())
      ##codigo descripcion peso volumen tipo valor_fob
      print("codigo descripcion peso volumen tipo VALOR-FOB")
      for mercaderia in self.mercaderias:
        volumen = 0
        if(mercaderia.getType() == "mercaderiaLiquida"):
          volumen += mercaderia.getVolumen()
        print(mercaderia.getId() + " " + mercaderia.getDescripcion() + " " + mercaderia.getPeso() + " " + volumen + " " + mercaderia.getType() + " " + mercaderia.getValorFOB())
      
