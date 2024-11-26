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
        print(f'{'nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'.ljust(25)}\n')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante._ativo}\n')
            
    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'False'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
        
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property  
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
        
    def listar_cardapio(self, pratos, bebidas, sobremesas):
        print("Cardápio:")
        print("Pratos Principais:")
        for prato in pratos:
            print(f"- {prato}")
        print("Bebidas:")
        for bebida in bebidas:
            print(f"- {bebida}")
        print("Sobremesas:")
        for sobremesa in sobremesas:
            print(f"- {sobremesa}")    