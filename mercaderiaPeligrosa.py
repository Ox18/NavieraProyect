## Importando clase padre
from mercaderia import Mercaderia

## Clase hija que hereda de la clase Mercaderia(Clase padre)
class MercaderiaPeligrosa:
    ## Permitiendo el uso de los atributos/metodos de la clase padre
    pass

    nivelPeligrosidad = 0 ## Nivel de peligrosidad
    type = "MercaderiaPeligrosa" ## Tipo de mercaderia

    ## GETTERS

    def getNivelPeligrosidad(self):
        return self.nivelPeligrosidad

    ## SETTERS

    def setNivelPeligrosidad(self, nivelPeligrosidad):
        self.nivelPeligrosidad = nivelPeligrosidad

    ## Sustituyendo al método que indica si el requerimiento es pelgrioso o no
    