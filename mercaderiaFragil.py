## Importando clase padre
from mercaderia import Mercaderia

## Clase hija que hereda de la clase Mercaderia(Clase padre)
class MercaderiaFragil(Mercaderia):
    ## Permitiendo el uso de los atributos/metodos de la clase padre
    pass

    tipoEmbalaje = "" ## Propiedad adicional
    type = "MercaderiaFragil" ## Tipo de mercaderia

    ## Getters

    def getTipoEmbalaje(self):
        return self.tipoEmbalaje

    ## Setters
    def setTipoEmbalaje(self, tipoEmbalaje):
        self.tipoEmbalaje = tipoEmbalaje