class Bicicleta:
    def __init__(self, cor, modelo, ano, preco):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.preco = preco

    def buzinar(self):
        print("Trim trim")
    
    def parar(self):
        print("Parando a bicicleta...")
        print("Bicicleta parada.")
    
    def correr(self):
        print("Vrummm...")

    # def __str__(self):
    #    return f"Cor: {self.cor} \nModelo: {self.modelo} \nAno: {self.ano} \nPreço: {self.preco}"

    def __str__(self):
        return f"{self.__class__.__name__} - {', '.join([f"{chave}: {valor}" for chave, valor in self.__dict__.items()])}"


bicicleta = Bicicleta("vermelha", "caloi", 2024, 600)

bicicleta.buzinar()
bicicleta.correr()
bicicleta.parar()

print("\n-- Informações sobre a bicicleta --")
print(bicicleta)