class Hero:
    def __init__(self, nome, idade, tipo, arma):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
        self.arma = arma

    def atacar(self):
        print(f'O herói {self.nome} ({self.tipo}) atacou usando {self.arma}.')

# Criando heróis e armazenando em uma lista
herois = [
    Hero('Gandalf', 1000, 'mago', 'cajado'),
    Hero('Aragorn', 87, 'guerreiro', 'espada'),
    Hero('Legolas', 293, 'arqueiro', 'arco'),
]

# Loop para atacar
for heroi in herois:
    heroi.atacar()
