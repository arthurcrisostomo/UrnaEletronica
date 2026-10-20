
# > Importa classe QApplication responsável por inicializar o Qt e criar o gerenciador de eventos da aplicação
from PySide6.QtWidgets import QApplication

# > Importa submodulo sys que vai ser usado para retornar os parametros de inicialização ao Qt e permite encerrar o programa
import sys

# > Importa a classe responsável por criar a janela principal
from interface import JanelaUrna

def main():
    # > Inicializa o framework Qt(Cria a comunicação SO e Aplicação) e se houver passa os comandos de inicialização
    app = QApplication(sys.argv)

    # > Cria a janela principal
    janela = JanelaUrna()

    # > Exibe a janela
    janela.show()

    # > Inicia o loop de eventos da janela aguardando uma ação do usuário
    sys.exit(app.exec())


if __name__ == '__main__':
    main()