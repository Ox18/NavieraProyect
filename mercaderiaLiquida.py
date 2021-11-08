## Importando clase padre
from mercaderia import Mercaderia

## Clase hija que hereda de la clase Mercaderia(Clase padre)
class MercaderiaLiquida(Mercaderia):
    ## Permitiendo el uso de los atributos/metodos de la clase padre
    pass
    
    volumen = 0 ## Volumen de la mercaderia
    type = "mercaderiaLiquida" ## Tipo de mercaderia

    ## GETTERS

    def getVolumen(self):
        return self.volumen
    
    ## SETTERS

    def setVolumen(self, volumen):
        self.volumen = volumen