from modelos.restaurante import Restaurante
    
restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Samir', 10)
restaurante_praca.receber_avaliacao('Rudney', 6)
restaurante_praca.receber_avaliacao('Silvia', 3)

def main():
    Restaurante.listar_restaurantes()
    restaurante_praca.listar_cardapio(['Lasanha'], ['Coca-Cola'], ['Sorvete'])

if __name__ == '__main__':
    main()