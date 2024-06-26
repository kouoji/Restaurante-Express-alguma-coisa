import os
from ativado.desativado import Restaurante

class ProgramaExpresso:
    def __init__(self):
        self.restaurantes = [
            Restaurante('Laçador', 'Espeto Corrido', True),
            Restaurante('Outback', 'Steakhouse', False),
            Restaurante('O Hamburgueiro', 'Hamburgueria', False)
        ]

    def finalizar_app(self):
        os.system("clear")
        os.system("cls")
        print("Finalizando o app\n")

    def voltar_menu_principal(self):
        input("Digite uma tecla para voltar ao menu principal: ")

    def mostrar_subtitulo(self, texto):
        os.system("clear")
        linha = '*' * (len(texto))
        print(linha)
        print(texto)
        print(linha)
        print()

    def listarRestaurantes(self):
        self.mostrar_subtitulo('Listando os Restaurantes'.ljust(20))
        print("Nome:".ljust(27), "Categoria:".ljust(34), "Status:".ljust(24))
        for restaurante in self.restaurantes:
            print(restaurante)

    def alternar_estado_restaurante(self):
        self.mostrar_subtitulo("Alterando o estado do restaurante".ljust(20))
        self.listarRestaurantes()
        nome_restaurante = input("Digite o nome do Restaurante que desejas alterar: ")
        restaurante_encontrado = False

        for restaurante in self.restaurantes:
            if nome_restaurante == restaurante.nome:
                restaurante_encontrado = True
                mensagem = restaurante.ativar_desativar()
                print(mensagem)
                break

        if not restaurante_encontrado:
            print("O restaurante não foi encontrado.")

        self.voltar_menu_principal()

    def avaliacao(self):
        self.mostrar_subtitulo("Dar estrelas ao Restaurante\n".ljust(20))
        self.listarRestaurantes()

        nome_restaurante = input("Digite o nome do restaurante que deseja dar estrelas: ")
        restaurante_encontrado = False

        for restaurante in self.restaurantes:
            if nome_restaurante == restaurante.nome:
                restaurante_encontrado = True
                while True:
                    nota = int(input("Digite as estrelas de 1 a 5 para este restaurante: "))
                    if 1 <= nota <= 5:
                        restaurante.adicionar_avaliacao(nota)
                        print(f"Você deu estrelas ao restaurante {nome_restaurante} com as estrelas {nota}.")
                        break
                    else:
                        print("Por favor, digite uma estrela válida (entre 1 e 5).")

        if not restaurante_encontrado:
            print("Restaurante não encontrado.")

        self.voltar_menu_principal()

    def ver_media_avaliacoes(self):
        self.mostrar_subtitulo("Média de estrelas dos Restaurantes\n".ljust(20))
        for restaurante in self.restaurantes:
            print(restaurante.calcular_media_avaliacoes())

        self.voltar_menu_principal()

    def cadastrar_novo_restaurante(self):
        nome_do_restaurante = input("Digite o nome do novo restaurante: ")
        categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
        restaurante_novo = Restaurante(nome_do_restaurante, categoria)
        self.restaurantes.append(restaurante_novo)
        print(f"Você cadastrou o restaurante: {nome_do_restaurante}")
