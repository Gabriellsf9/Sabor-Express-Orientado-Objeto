from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Comida mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_mexicano.alternar_estado()
restaurante_japones.receber_avaliacao('Samir', 5)
restaurante_mexicano.receber_avaliacao('Rudney', 1)
restaurante_praca.receber_avaliacao('Silvia', 3)
    
bebida_suco = Bebida('Suco de melancia',5.0,'Grande')
prato_pao = Prato('Pao',2.0,'O melhor pão da cidade')

def main():
    Restaurante.listar_restaurantes()
    Restaurante.media_avaliacoes
    print('Cardapio:')
    print(bebida_suco)
    print(prato_pao)

if __name__ == '__main__':
    main()