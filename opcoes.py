from opcoes_restaurante import ProgramaExpresso

class Menu:
    def __init__(self):
        self.programa = ProgramaExpresso()

    def escolher_opcoes(self):
        self.programa.mostrar_subtitulo('''Restaurante Alessandro e Arthur''')
        print("1 - Cadastrar restaurante")
        print("2 - Listar restaurantes")
        print("3 - Ativar/Desativar restaurante")
        print("4 - Dar estrelas ao Restaurante")
        print("5 - Ver as estrelas do Restaurante")
        print("6 - Sair\n")

    def opcao_invalida(self):
        self.programa.mostrar_subtitulo("Opção inválida\n".ljust(20))
        self.programa.voltar_menu_principal()

    def menu_principal(self):
        while True:
            try:
                self.escolher_opcoes()
                opcao_digitada = int(input("Digite a opção desejada: "))
                if opcao_digitada == 1:
                    print("Você escolheu cadastrar restaurante\n")
                    self.programa.cadastrar_novo_restaurante()
                elif opcao_digitada == 2:
                    self.programa.listarRestaurantes()
                    self.programa.voltar_menu_principal()
                elif opcao_digitada == 3:
                    self.programa.alternar_estado_restaurante()
                elif opcao_digitada == 4:
                    self.programa.avaliacao()
                elif opcao_digitada == 5:
                    self.programa.ver_media_avaliacoes()
                elif opcao_digitada == 6:
                    print("Você escolheu sair do aplicativo\n")
                    self.programa.finalizar_app()
                    break
                else:
                    self.opcao_invalida()
            except ValueError:
                print("Por favor, digite um número válido.")
