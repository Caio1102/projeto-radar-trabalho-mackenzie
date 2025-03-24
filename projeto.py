placa_do_carro = input("Digite a placa do seu veículo: ").upper()
nome_motorista = input("Digite o seu nome: ").upper()
velocidade_registrada = int(input("Informe a velocidade registrada (Km/h): "))
velocidade_permitida = int(input("Informe qual era a velocidade permitida da via (Km/h): "))



def tipo_de_multa():
    diferenca_velocidade = velocidade_registrada - velocidade_permitida
    if velocidade_registrada <= velocidade_permitida:
        print("Não houve nenhuma infração")
    elif diferenca_velocidade >= 50 * 0.01 * velocidade_permitida:
        infracao_gravissima()
    elif diferenca_velocidade >= 20 * 0.01 * velocidade_permitida:
        infracao_grave()
    else:
        infracao_leve()


def infracao_leve():
    print("""Você cometeu uma infração leve que e andar até 20% acima do limite permitido, o valor da multa e de R$ 130,16 e nenhum ponto na CNH.""")
    multa_anterior = input("Você sofreu alguma multa anteriormente? (S/N): ").upper()
    total = 130.16
    pontos = 0
    esq = input("Você deseja realizar o pagamento agora mesmo? caso sim podemos disponibilizar um desconto de 20% sobre a multa (S/N): ").upper()
    if esq == "S":
        total= total - (total*0.20) 
        print(f"Você devera pagar R${total} e tomara {pontos} na CNH")
    if esq == "N":
        print(f"Você devera pagar R${total} e tomara {pontos} na CNH")
    voltar_ao_menu_principal()


def infracao_grave():
    print("""Você cometeu uma infração grave que e andar entre 20% e 50% acima do limite permitido, o valor da multa e de R$ 195,23 e adição de 5 pontos na CNH.""")
    multa_anterior = input("Você sofreu alguma multa anteriormente? (S/N): ").upper()
    if multa_anterior == "S":
        total = 195.23 * 2
        print(f"O valor da Multa sera dobrado para R${total}")
    else: 
        total = 195.23
    pontos = 5
    esq = input(f"Você deseja realizar o pagamento da multa no valor de R${total} agora mesmo? caso sim podemos disponibilizar um desconto de 20% sobre a multa (S/N): ").upper()
    if esq == "S":
        total= total - (total*0.20) 
        print(f"Você devera pagar R${total} e tomara {pontos} na CNH")
    if esq == "N":
        print(f"Você devera pagar R${total} e tomara {pontos} na CNH")
    voltar_ao_menu_principal()


def infracao_gravissima():
    print("""Você cometeu uma infração gravíssima que e andar 50% acima do limite permitido, o valor da multa e de R$ 880,41, adição de 7 pontos na CNH e suspensão imediata do direito de dirigir.""")
    multa_anterior = input("Você sofreu alguma multa anteriormente? (S/N): ").upper()
    if multa_anterior == "S":
        total = 880.41 * 2
        print(f"O valor da multa sera dobrado para {total}")
    else: 
        total = 880.41
    pontos = 7
    esq = input(f"Você deseja realizar o pagamento da multa no valor de R${total} agora mesmo? caso sim podemos disponibilizar um desconto de 20% sobre a multa (S/N): ").upper()
    if esq == "S":
        total= total - (total*0.20) 
        print(f"Você devera pagar R${total} e tomara {pontos} na CNH alem de ser obrigado a realizar um curso de reciclagem no Detran")
    if esq == "N":
        print(f"Você devera pagar R${total} e tomara {pontos} na CNH alem de ser obrigado a realizar um curso de reciclagem no Detran")
    voltar_ao_menu_principal()


def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()


def opcao_invalida():
    print('Opção inválida')
    voltar_ao_menu_principal()


def main():
    tipo_de_multa()


if __name__ == '__main__':
    main()


