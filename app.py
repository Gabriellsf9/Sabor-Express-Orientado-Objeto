from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Samir', '10')
restaurante_praca.receber_avaliacao('Rudney', '6')
restaurante_praca.receber_avaliacao('Silvia', '8')

restaurante_praca.listar_cardapio('Lasanha', 'coca-cola', 'sorvete')

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
