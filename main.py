from mercaderiaFragil import MercaderiaFragil
from mercaderiaLiquida import MercaderiaLiquida
from mercaderiaPeligrosa import MercaderiaPeligrosa
from viaje import Viaje
from container import Container


print("---Creando viaje---")
print("Introduce el ID del viaje")
idViaje = input()
print("Introduce el nombre del barco: ")
nombreBarco = input()
print("Introduce el punto de origen")
origen = input()
print("Introduce el punto de destino")
destino = input()
print("Introduce la fecha de partida")
fechaPartida = input()

containers = []

print("Cuantos contenedores tendra el viaje")
numContainers = int(input())

for i in range(numContainers):
    print("Contenedor #" + str(i + 1))
    print("Introduce el ID del contenedor: ")
    idContainer = str(input())
    print("Cuantas mercaderias tendra este contenedor?")
    numMercaderias = int(input())
    container = Container(idContainer)

    for pointerMercaderia in range(numMercaderias):
        print("-----------------")
        print("Mercaderia #" + str(pointerMercaderia + 1))
        print("-----------------")
        print("Que tipo de mercaderia es?")
        print("1. Mercaderia Liquida")
        print("2. Mercaderia Peligrosa")
        print("3. Mercaderia Fragil")
        tipoMercaderia = int(input())
        print("-----------------")
        print("Introduce el ID de la mercaderia: ")
        idMercaderia = str(input())
        print("Introduce la descripcion de la mercaderia: ")
        descripcion = str(input())
        print("Introduce el peso de la mercaderia: ")
        peso = float(input())
        print("Introduce el valor FOB de la mercaderia: ")
        valorFOB = float(input())
        mercaderia = None
        if tipoMercaderia == 1:
            print("Introduce el volumen de la mercaderia: ")
            volumen = float(input())
            mercaderia = MercaderiaLiquida(idMercaderia, descripcion, peso, valorFOB)
            mercaderia.setVolumen(volumen)
        elif tipoMercaderia == 2:
            print("Introduce el nivel de peligrosidad: ")
            nivelPeligrosidad = int(input())
            mercaderia = MercaderiaPeligrosa(idMercaderia, descripcion, peso, valorFOB)
            mercaderia.setNivelPeligrosidad(nivelPeligrosidad)
        elif tipoMercaderia == 3:
            print("Introduce el tipo de embalaje")
            tipoEmbalaje = str(input())
            mercaderia = MercaderiaFragil(idMercaderia, descripcion, peso, valorFOB)
            mercaderia.setTipoEmbalaje(tipoEmbalaje)
        container.AdicionarMercaderia(mercaderia)
    containers.append(container)

viaje = Viaje(idViaje, nombreBarco, origen, destino, fechaPartida, containers)
viaje.MostrarReporte()