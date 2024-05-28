class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def __str__(self):
        return f"Cor: {self.cor} \nPlaca: {self.placa} \nNúmero de rodas: {self.numero_rodas}"

    def ligar_motor(self):
        print("Ligando motor...")
        print("Motor ligado.")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, esta_carregado):
        super().__init__(cor, placa, numero_rodas)
        self.esta_carregado = esta_carregado
    
    def __str__(self):
        return f"{super().__str__()} \nEstá carregado? {'Sim' if self.esta_carregado else 'Não'}"


print("\n-- Ficha da motocicleta --")
moto = Motocicleta("preto", "12AB", 2)
print(moto)

print("\n-- Ficha do carro --")
carro = Carro("branco", "34CD", 4)
print(carro)

print("\n-- Ficha do caminhão --")
caminhao = Caminhao("vermelho", "56EF", 8, False)
print(caminhao)