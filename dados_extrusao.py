import pandas as pd
import sys
from PyQt5.QtWidgets import QApplication, QComboBox, QLineEdit, QLabel, QVBoxLayout, QWidget

class TabelaMateriais(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Abrir o arquivo CSV em um DataFrame
        self.df = pd.read_csv('./Tabelas/materiais_extrusao.csv')

        # Criar uma comboBox para listar os itens da coluna "A"
        self.comboMateriais = QComboBox(self)
        self.comboMateriais.addItems(list(self.df['Material']))

        # Criar dois lineEdits para mostrar os valores das colunas "B" e "C"
        self.lineEditTemperatura = QLineEdit(self)
        self.lineEditVelocidade = QLineEdit(self)

        # Criar labels para cada campo
        labelMateriais = QLabel('Selecione um material:')
        labelTemperatura = QLabel('Temperatura:')
        labelVelocidade = QLabel('Velocidade:')

        # Configurar um layout vertical para os widgets
        vbox = QVBoxLayout()
        vbox.addWidget(labelMateriais)
        vbox.addWidget(self.comboMateriais)
        vbox.addWidget(labelTemperatura)
        vbox.addWidget(self.lineEditTemperatura)
        vbox.addWidget(labelVelocidade)
        vbox.addWidget(self.lineEditVelocidade)
        self.setLayout(vbox)

        # Conectar o sinal de mudança de seleção da comboBox a uma função
        self.comboMateriais.currentIndexChanged.connect(self.atualizarValores)

        # Atualizar os valores dos lineEdits com o primeiro item da tabela
        self.atualizarValores()

    def atualizarValores(self):
        # Obter o índice do item selecionado na comboBox
        idx = self.comboMateriais.currentIndex()

        # Obter os valores correspondentes nas colunas "B" e "C"
        valorTemperatura = str(self.df.loc[idx, 'Temperatura'])
        valorVelocidade = str(self.df.loc[idx, 'Velocidade'])

        # Atualizar os valores nos lineEdits
        self.lineEditTemperatura.setText(valorTemperatura)
        self.lineEditVelocidade.setText(valorVelocidade)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tabelaMateriais = TabelaMateriais()
    tabelaMateriais.show()
    sys.exit(app.exec_())