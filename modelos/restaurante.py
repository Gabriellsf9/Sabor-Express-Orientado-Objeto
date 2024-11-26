from modelos.avaliacao import Avaliacao
from modelos.pratos import Pratos

class Restaurante:
    
    restaurantes = []
    
    def __init__(self, nome, categoria):        
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._pratos = []
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(25)}\n')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante._ativo}')
            
    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'False'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
        
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
        
    def listar_cardapio(self,pratos, bebidas, sobremesas):
        pratos = Pratos(pratos, bebidas,sobremesas)
        self._pratos.append(pratos)