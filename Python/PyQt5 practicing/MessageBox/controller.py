from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMessageBox

def show_message():
    data = Window.lineEdit.text()
    dataStr = (f'Você acaba de se registrar, {data}!')
    Window.lineEdit.setText('')
    if data == "":
        QMessageBox.about(Window,'Alerta!', 'Digite algo na caixa para registrar-se.')
    else:
        QMessageBox.about(Window,'Obrigado!', dataStr)

app = QtWidgets.QApplication([])
Window = uic.loadUi('MessageBox/Window.ui')
Window.pushButton.clicked.connect(show_message)

Window.show()
app.exec()