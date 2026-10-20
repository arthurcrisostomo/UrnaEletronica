
# > Importa modulo QtWidgets responsável pela criação da janela e widgets
from PySide6.QtWidgets import(
    QWidget, # Cria a janela
    QLabel, # Cria um texto
    QHBoxLayout, # Organiza os elementos na Horizontal
    QFrame, # Cria um frame
    QVBoxLayout, # Organiza os elementos na Vertical
    QTextEdit, # Cria um campo de texto
    QGridLayout, # Cria uma tabela de linhas e colunas para posicionar widgets
    QPushButton # Cria um botão
)

# > Importa modulo QtGui que contem elementos gráficos de baixo nivel
from PySide6.QtGui import(
    QFont, # Cria e retorna o objeto que descreve o estilo do texto
    QIcon # Retorna o objeto do icone a ser usado aplicado na aplicação
)

# Importa modulo QtCore que contem funcionalidades não gráficas que servem de apoio para outros modulos
from PySide6.QtCore import(
    Qt, # > Enums e constantes
    QTimer # > Agenda uma chamada de função para daqui a x segundos
)

# > Importa biblioteca responsável pelas verificações
import logica

# > Importa pygame para manipular sons
import pygame

# > Importa os para interagir com o SO
import os

# > Importa sys para obter o caminho da pasta temporaria criada pelo PyInstaller
import sys

def localizar_icone():
    # > Define o nome do arquivo
    nome_arquivo = 'icone-urna.ico'

    # > Retorna o caminho da pasta onde o programa esta rodando
    caminho_local = os.path.dirname(__file__)

    # > Retorna o caminho da pasta temporaria _MEIPASS + nome_arquivo caso exista, se nao retorna o caminho_local + nome_arquivo
    caminho_maipass = os.path.join(str(getattr(sys, '_MEIPASS', caminho_local)), nome_arquivo)

    # > Retorna pra quem o chamou
    return caminho_maipass

def localizar_pasta_sons():
    # > Define o nome da pasta
    nome_pasta = 'sons'

    # Coleta o caminho da pasta onde o programa esta rodando
    caminho_pasta_local = os.path.dirname(__file__)

    # > Retorna o caminho da pasta temporaria _MEIPASS + nome_pasta caso exista, se nao retorna o caminho_pasta_local + nome_pasta
    caminho_maipass = os.path.join(str(getattr(sys, '_MEIPASS', caminho_pasta_local)), nome_pasta)

    # > Retorna para quem o chamou
    return caminho_maipass

class JanelaUrna(QWidget):
    def __init__(self):
        # > Chama o construtor da classe QWidget responsável por criar a janela
        super().__init__()

        # > Define o titulo da janela
        self.setWindowTitle('Urna Eletronica')

        # > Define o icone da janela
        self.setWindowIcon(QIcon(localizar_icone()))

        # > Inicializa o sistema de audio do pygame
        pygame.mixer.init()

        # > Define os sons som_botao e som_fim
        self.som_botao = pygame.mixer.Sound(os.path.join(localizar_pasta_sons(), 'clique-botao.wav'))
        self.som_fim = pygame.mixer.Sound(os.path.join(localizar_pasta_sons(), 'fim-sound.mp3'))

        # > Define o titulo da janela
        self.setWindowTitle('Urna Eletrônica')

        # > Define o tamanho da janela
        self.resize(800, 500)

        # > Cria o ID #janela para se referir a janela principal
        self.setObjectName('janela')

        # > Define a cor do background com o #id da jenala principal
        self.setStyleSheet("""
            #janela {
                background-color: #101d29;
            }
        """)

        # > Armazena o voto atual
        self._numero_voto = ''

        # > Dicionario que armazena chave-valor de cada presidente
        self.dict_candidatos = {
            '22': 'Flavio Bolsonaro',
            '13': 'Lula'
        }

        estilo_fonte = QFont('Segoe UI', 16, QFont.Weight.Bold)

        # > Organiza os elementos e frames da janela principal na Horizontal
        organizador_janela_principal = QVBoxLayout(self)

        # > Cria o frame responsável por exibir o local da urna dentro do organizador da tela principal
        frame_local_urna = QFrame()

        # > Adiciona o frame_local_urna ao organizador da janela principal
        organizador_janela_principal.addWidget(frame_local_urna)

        # > Cria o organizador do frame_local_urna responsável por organizar os elementos pela vertical
        organizador_frame_local_urna = QVBoxLayout(frame_local_urna)

        # > Cria o texto URNA ELETRONICA FORTALEZA-CE
        label_local_urna = QLabel('URNA ELETRÔNICA FORTALEZA-CE\nPYTHON')

        # Define o estilo da fonte do texto
        label_local_urna.setFont(QFont(estilo_fonte))

        label_local_urna.setStyleSheet('''
            color: #FFFFFF;
        ''')

        # > Adiciona o texto ao organizador do frame_local_urna
        organizador_frame_local_urna.addWidget(label_local_urna)

        # > Cria o frame_tela_urna
        frame_tela_urna = QFrame()

        # > Cria o organizador do frame_tela_urna
        organizador_frame_tela_urna = QHBoxLayout(frame_tela_urna)

        # > Adiciona o frame_tela_urna ao organizador da tela principal
        organizador_janela_principal.addWidget(frame_tela_urna)

        # > Mola que usa o espaço disponivel do lado esquerdo para centralizar a urna
        organizador_frame_tela_urna.addStretch(1)

        # > Cria o campo texto somente para leitura
        self.campo_texto = QTextEdit(readOnly=True)

        # > Define o estilo do campo texto
        self.campo_texto.setStyleSheet("""
            QTextEdit {
                background-color: #f2f5f7;
                border-radius: 8px;
                padding: 10px;
            }
        """)

        # > Define a altura e largura fixas do campo_texto
        self.campo_texto.setFixedSize(450, 300)

        # > Define os textos personalizados inicias do campo texto
        self.atualizar_tela('')

        # > Adiciona o campo texto ao organizador_frame_tela_urna
        organizador_frame_tela_urna.addWidget(self.campo_texto)

        # > Cria o frame vertical
        frame_vertical = QFrame()

        # > Cria o organizador do frame vertical que organiza os elementos pela Vertical
        organizador_frame_vertical = QVBoxLayout(frame_vertical)

        # > Adiciona o frame_vertical ao organizador_frame_tela_urna
        organizador_frame_tela_urna.addWidget(frame_vertical)

        # > Mola que usa o espaço disponivel do topo para centralizar os elementos
        organizador_frame_vertical.addStretch(1)

        # > Cria o frame_painel_buttons
        frame_painel_buttons = QFrame()

        # > Define o #ID do frame
        frame_painel_buttons.setObjectName('painel')

        # > Personaliza o frame_painel_buttons a partir do ID criado
        frame_painel_buttons.setStyleSheet('''
            #painel {
                background-color: #14181E;
                border-radius: 8px;
            }
        ''')

        # > Define a altura e largura fixas do frame_painel_buttons
        frame_painel_buttons.setFixedSize(230, 250)

        # > Cria o organizador de elementos na Vertical do frame_painel_buttons
        organizador_painel = QVBoxLayout(frame_painel_buttons)

        # > Adiciona o frame_painel_buttons de forma centralizada dentro do organizador_frame_tela_urna
        organizador_frame_vertical.addWidget(
            frame_painel_buttons,
            alignment=Qt.AlignmentFlag.AlignHCenter
        )

        # > Cria a grade de linhas e colunas
        grade_digitos = QGridLayout()

        # > Define 8px de espaço entre cada celula da grade
        grade_digitos.setSpacing(8)

        # > Lista de tuplas que contem| Texto do botão, linha, coluna
        digitos_numericos = [('1', 0, 0), ('2', 0, 1), ('3', 0, 2),
                             ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
                             ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
                             ('0', 3, 1)]

        # > Itera sobre cada tupla da lista e faz o unpacking da tupla nas variaveis texto, linha e coluna
        for texto, linha, coluna in digitos_numericos:

            # > Cria o botão com com o texto atual
            botao = QPushButton(texto)

            # > Define o estilo do botão
            botao.setFont(QFont('Segoe UI', 12, QFont.Weight.Bold))

            # > Define cor de fundo, borda e cor da fonte do botao
            botao.setStyleSheet('''
                background-color: #1e222a;
                color: #FFFFFF;
                border-radius: 8px;
            ''')

            # > Define a altura e largura do botão
            botao.setFixedSize(45, 45)

            # _ > Parametro descartavel que recebe o valor boolean do connect
            # num > Argumento padrão que recebe o texto atual e passa pra função ao ser clicado
            botao.clicked.connect(lambda _, num=texto: self.botao_acionado(num))

            # > Adiciona o widget botão na linha, coluna especificadas
            grade_digitos.addWidget(botao, linha, coluna)

        # > Adiciona a grade ao organizador_painel
        organizador_painel.addLayout(grade_digitos)

        # > Cria o frame dos botões (BRANCO, CORRIGE , CONFIRMA)
        frame_botoes_resultado = QFrame()

        # > Cria o organizador do frame_botoes_resultado
        organizador_botoes_resultado = QHBoxLayout(frame_botoes_resultado)

        # > Zera o espaçamento do segundo conjunto de Frame + Organizador Layout
        organizador_botoes_resultado.setContentsMargins(0, 0, 0, 0)

        # > Adiciona o frame_botoes_resultado dentro do organizador_frame_vertical
        organizador_frame_vertical.addWidget(frame_botoes_resultado)

        # > Cria e define o estilo do botão BRANCO
        botao_branco = QPushButton('BRANCO')
        botao_branco.setFont(QFont('Segoe UI', 11))
        botao_branco.setStyleSheet('''
            background-color: #FFFFFF;
            color: #000000;
            border-radius: 2px;
            padding: 8px 5px 8px 5px;
        ''')

        # > Conecta o click do botão branco a função self.branco
        botao_branco.clicked.connect(self.branco)

        # > Adiciona o botão branco
        organizador_botoes_resultado.addWidget(botao_branco)

        # > Cria e define o estilo do botão CORRIGE
        botao_corrige = QPushButton('CORRIGE')
        botao_corrige.setFont(QFont('Segoe UI', 11))
        botao_corrige.setStyleSheet('''
            background-color: #ff7424;
            color: #000000;
            border-radius: 2px;
            padding: 8px 5px 8px 5px;
        ''')

        # > Conecta o click do botão corrige a função self.corrige
        botao_corrige.clicked.connect(self.corrige)

        # > Adiciona o botão corrige ao organizador_botoes_resultado
        organizador_botoes_resultado.addWidget(botao_corrige)

        # > Cria e define o estilo do botão CONFIRMA
        botao_confirma = QPushButton('CONFIRMA')
        botao_confirma.setFont(QFont('Segoe UI', 11))
        botao_confirma.setStyleSheet('''
            background-color: #02a620;
            color: #000000;
            border-radius: 2px;
            padding: 8px 5px 8px 5px;
        ''')

        # > Conecta o click do botão  CONFIRMA a função self.confirma
        botao_confirma.clicked.connect(self.confirma)

        # > Adiciona o botão confirma ao organizador_botoes_resultado
        organizador_botoes_resultado.addWidget(botao_confirma)

        # > Mola que usa o espaço disponivel inferior para centralizar os elementos
        organizador_frame_vertical.addStretch(1)

        # > Mola que usa o espaço disponivel do lado direito para centralizar a urna
        organizador_frame_tela_urna.addStretch(1)

    @property
    def voto(self):
        return self._numero_voto

    @voto.setter
    def voto(self, numero):
        self._numero_voto = numero
        self.atualizar_tela(self._numero_voto)

    def botao_acionado(self, numero: str):
        # > Toca o som do botão
        self.som_botao.play()

        # > Chama e passa o argumento numero para a função responsável por atribuir o voto do usuario
        self.atribuir_voto(numero)

    def atribuir_voto(self, numero: str):
        # > Verifica se é possivel adicionar numeros ao voto
        if logica.verificar_add(self._numero_voto):

            # > Passa para o setter adicionar o numero atual ao getter
            self.voto += numero

    def atualizar_tela(self, voto: str):
        # Cham a função responsável por
        candidato = logica.localizar_candidato(voto, self.dict_candidatos)

        # > Define o texto na tela da urna
        self.campo_texto.setHtml(
            '<span style="color: #808080; font-weight: bold; font-size: 8pt; font-family: Segoe UI;">SEU VOTO PARA</span>'
            '<br>'
            '<span style="color: #0a0a0a; font-weight: bold; font-size: 13pt; font-family: Segoe UI;">PRESIDENTE</span>'
            '<br>'
            '<br>'
            '<span style="color: #808080; font-weight: bold; font-size: 8pt; font-family: Segoe UI;">VOTO</span>'
            '<br>'
            f'<span style="color: #000000; font-weight: bold; font-size: 14pt; font-family: Segoe UI;">{voto}</span>'
            '<br>'
            '<br>'
            f'<span style="color: #000000; font-weight: bold; font-size: 16pt; font-family: Segoe UI;">{candidato}</span>'
        )

    def corrige(self):
        # > Passa para o setter o voto como vazio
        self.voto = ''

    def branco(self):
        # > Passa para o setter o voto como BRANCO
        self.voto = 'BRANCO'

    def confirma(self):
        if len(self._numero_voto) >= 2:
            # Chama a função responsável por verficiar se todos os campos foram preenchidos ou não e caso não tenha encontrado self._numero_voto recebe NULO
            self._numero_voto = logica.verificacao_confirma(self._numero_voto, self.dict_candidatos)

            # > Chama a função responsável por exibir a animação final de votação
            self.animacao_final()

            # > Agenda uma chamada para a função self.resetar daqui a 1.5s
            QTimer.singleShot(1500, self.resetar)

    def animacao_final(self):
        # > Define o texto FIM na tela da urna
        self.campo_texto.setText(f'''
            {'<br>' * 7}
            <span style="color: #000000; font-weight: bold; font-size: 26pt; font-family: Segoe UI;">ㅤㅤㅤㅤㅤFIM</span>
        ''')

        # > Toca o audio final
        self.som_fim.play()

    def resetar(self):
        # Passa para o setter o voto atual como vazio
        self.voto = ''