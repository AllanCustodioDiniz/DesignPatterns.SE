from abc import ABC, abstractmethod

class Carro(ABC):
    @abstractmethod
    def dirigir(self):
        pass

class CarroSedan(Carro):
    def dirigir(self):
        return "Dirigindo um Sedan."

class CarroHatch(Carro):
    def dirigir(self):
        return "Dirigindo um Hatch."

class FabricaCarros(ABC):
    @abstractmethod
    def fabricar_carro(self):
        pass

class FabricaCarroSedan(FabricaCarros):
    def fabricar_carro(self):
        return CarroSedan()

class FabricaCarroHatch(FabricaCarros):
    def fabricar_carro(self):
        return CarroHatch()

def main():
    sedan_factory = FabricaCarroSedan()
    hatch_factory = FabricaCarroHatch()

    carro_sedan = sedan_factory.fabricar_carro()
    carro_hatch = hatch_factory.fabricar_carro()

    print(carro_sedan.dirigir())  # Saída: Dirigindo um Sedan.
    print(carro_hatch.dirigir())  # Saída: Dirigindo um Hatch.

if __name__ == "__main__":
    main()
