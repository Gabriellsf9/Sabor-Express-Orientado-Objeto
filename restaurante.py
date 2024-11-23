import os

os.system('clear')
class Restaurante:
    
    restaurantes = []
    
    def __init__(self, nome, categoria):        
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

restaurantes = [restaurante_praca, restaurante_pizza]

print(restaurante_praca)
print(restaurante_pizza)
