import re

def validar_placa(placa_do_carro):
    """" Valida se a placa esta no formato correto"""
    padrao = r"^[A-Z]{3}-\d{4}$"
    if re.match(padrao,placa_do_carro):
        return True
    else:
        return False
    
def voltar_ao_menu_principal():
    """Responsavel a voltar ao menu principal"""
    input("Digite uma tecla para voltar ao menu principal. ")
    main()

def opcao_invalida():
    """Mostra que a pessoa colocou uma opção invalida """
    print("Opção invalida. tente novamente... ")
    voltar_ao_menu_principal()

def tipo_de_multa(velocidade_registrada, velocidade_permitida):
    """ Identifica o tipo de infração """
    diferenca_velocidade = velocidade_registrada - velocidade_permitida
    if velocidade_registrada <= velocidade_permitida:
        print("Não houve nenhuma infração.")
    elif diferenca_velocidade >= 50 * 0.01 * velocidade_permitida:
        infracao_gravissima()
    elif diferenca_velocidade >= 20 * 0.01 * velocidade_permitida:
        infracao_grave()
    else:
        infracao_leve()

def infracao_leve():
    """Trata infrações leves """
    print("Você cometeu uma infração leve que e andar até 20% acima do limite permitido, o valor da multa e de R$ 130,16 e nenhum ponto na CNH.")
    total = 130.16
    aplicar_desconto(total, 0)

def infracao_grave():
    """Trata infrações graves """
    print("Você cometeu uma infração grave que e andar entre 20% e 50% acima do limite permitido, o valor da multa e de R$ 195,23 e adição de 5 pontos na CNH.")
    total = 195.23
    if verificar_multa_anterior():
        total = total * 2
        print(f"O valor da multa sera dobrado para R${total} por reincidência! ")
    aplicar_desconto(total, 5)

def infracao_gravissima():
    """Trata infrações gravissimas """
    print("Você cometeu uma infração gravíssima que e andar 50% acima do limite permitido, o valor da multa e de R$ 880,41, adição de 7 pontos na CNH, suspensão imediata do direito de dirigir e Você precisa fazer um curso de reciclagem no Detran.")
    total= 880.41
    if verificar_multa_anterior():
        total = total*2
        print(f"O valor da multa sera dobrado para R${total} por reincidência!")
    aplicar_desconto(total, 7)

def verificar_multa_anterior():
    """Verifica se ja tomou multra antes """
    multa_anterior = input("Você sofreu alguma multa anteriormente? (S/N): ").upper()
    return multa_anterior == "S"

def aplicar_desconto(total, pontos):
    """aplica desconto caso pague no momento da multa"""
    esq = input(f"Você deseja realizar o pagamento da multa no valor de R${total} agora? caso sim conseguimos disponibilizar 20% de desconto. (S/N): ").upper()
    if esq == "S":
         total= total - (total*0.20)  
         print(f"Você devera pagar R${total} e tomara {pontos} na CNH")
    elif esq == "N":
        print(f"Você devera pagar R${total} e tomara {pontos} na CNH")
    else: 
        opcao_invalida()

def main():
    placa_do_carro = input("Digite a placa do seu veículo no padrão ABC-1234 : ").upper()
    if validar_placa(placa_do_carro):
        print("Placa Valida")
    else:
        print("Você digitou o formato da placa de forma incorreta. ")
        opcao_invalida()
        return
    
    nome_motorista = input("Digite o seu nome: ").upper()
    try:
        velocidade_registrada = int(input("Informe a velocidade registrada (Km/h): "))
        velocidade_permitida = int(input("Informe qual era a velocidade permitida da via (Km/h): "))
        tipo_de_multa(velocidade_registrada, velocidade_permitida)
    except ValueError:
        print("Você digitou os valores numericos da velocidade de forma invalida, tente novamente: .")
        opcao_invalida()

if __name__ == "__main__":
    main()
