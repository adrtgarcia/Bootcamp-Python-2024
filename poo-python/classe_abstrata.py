from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

class ControleTv(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("TV ligada!\n")

    def desligar(self):
        print("Desligando a TV...")
        print("TV desligada!\n")

controle = ControleTv()
controle.ligar()
controle.desligar()