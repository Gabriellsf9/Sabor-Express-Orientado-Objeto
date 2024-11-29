from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')

restaurante_praca.receber_avaliacao('Silvia', 3)
    
bebida_suco = Bebida('Suco de melancia',5.0,'Grande')
bebida_suco.aplicar_desconto()
prato_pao = Prato('Pao',2.0,'O melhor pão da cidade')
prato_pao.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pao)


def main():
    Restaurante.listar_restaurantes()
    Restaurante.media_avaliacoes
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()