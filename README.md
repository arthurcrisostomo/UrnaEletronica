# Urna Eletrônica (Simulação)

Simulação didática de uma urna eletrônica feita em **Python** com **PySide6**. O projeto reproduz o fluxo visual e sonoro de uma urna real: digitar o número, ver o candidato na tela, votar em branco, corrigir e confirmar.

> Projeto educacional. **Nenhum voto é armazenado**: o objetivo é apenas simular o funcionamento da urna.

## Funcionalidades

- Teclado numérico (0 a 9) com som de clique
- Exibição automática do nome do candidato ao digitar o número completo
- Botão **BRANCO**
- Botão **CORRIGE** (limpa o número digitado)
- Botão **CONFIRMA** com tela de **FIM** e som de confirmação
- Reinício automático da tela após a confirmação

## Tecnologias

- [Python 3](https://www.python.org/)
- [PySide6](https://doc.qt.io/qtforpython-6/) (interface gráfica)
- [pygame](https://www.pygame.org/) (apenas o módulo `mixer`, para os sons)

## Como executar

1. Clone o repositório:

```bash
git clone https://github.com/arthurcrisostomo/UrnaEletronica.git
cd UrnaEletronica
```

2. (Opcional) Crie e ative um ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux / macOS
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o programa:

```bash
python main.py
```

## Estrutura do projeto

```
.
├── main.py            # Ponto de entrada da aplicação
├── interface.py       # Janela e widgets (PySide6)
├── logica.py          # Verificações e regras do voto
├── sons/              # Arquivos de áudio (cliques e som de fim)
├── requirements.txt   # Dependências
└── README.md
```

## Personalização

Os candidatos ficam em um dicionário na classe da janela (`número: nome`). Para adicionar ou alterar candidatos, edite-o:

```python
self.dict_candidatos = {
    '22': 'Flavio Bolsonaro',
    '13': 'Lula',
}
```

