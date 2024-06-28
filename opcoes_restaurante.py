import os
from ativado.desativado import Restaurante

class Avaliacao:
    def __init__(self, cliente, nota):
        self.cliente = cliente
        self.nota = nota

class Restaurante:
    def __init__(self, nome, categoria, ativo=True):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.avaliacoes = []

    def __str__(self):
        status = '✔' if self.ativo else '✘'
        return f'{self.nome.ljust(27)} {self.categoria.ljust(34)} {status.ljust(24)}'

    def ativar_desativar(self):
        self.ativo = not self.ativo
        return f"Restaurante {'ativado' if self.ativo else 'desativado'}."

    def adicionar_avaliacao(self, cliente, nota):
        self.avaliacoes.append(Avaliacao(cliente, nota))

    def calcular_media_avaliacoes(self):
        if not self.avaliacoes:
            return f"{self.nome}: Nenhuma avaliação"
        media = sum(avaliacao.nota for avaliacao in self.avaliacoes) / len(self.avaliacoes)
        return f"{self.nome}: Média de {media:.2f} estrelas"

class ProgramaExpresso:
    def __init__(self):
        self.restaurantes = [
            Restaurante('Laçador', 'Espeto Corrido', True),
            Restaurante('Outback', 'Steakhouse', False),
            Restaurante('O Hamburgueiro', 'Hamburgueria', False)
        ]

        self.restaurantes[0].adicionar_avaliacao("Cliente 1", 4)
        self.restaurantes[1].adicionar_avaliacao("Cliente 2", 5)
        self.restaurantes[2].adicionar_avaliacao("Cliente 3", 3)
        self.restaurantes[2].adicionar_avaliacao("Cliente 4", 4)

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
                        restaurante.adicionar_avaliacao("Novo Cliente", nota)
                        print(f"Você deu estrelas ao restaurante {nome_restaurante} com as estrelas {nota}.")
                        break
                    else:
                        print("Por favor, digite uma estrela válida (entre 1 e 5).")

                break

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
