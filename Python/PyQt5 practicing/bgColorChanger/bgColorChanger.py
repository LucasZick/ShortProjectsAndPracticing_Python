from PyQt5 import uic, QtWidgets

def main_function():
    if form.radioButton.isChecked():
        print('Verde selecionado')
        form.setStyleSheet('background-color: lightgreen;')
    elif form.radioButton_2.isChecked():
        print('Rosa selecionado')
        form.setStyleSheet('background-color: pink;')
    elif form.radioButton_3.isChecked():
        print('Azul selecionado')
        form.setStyleSheet('background-color: lightblue;')
    elif form.radioButton_4.isChecked():
        print('Amarelo selecionado')
        form.setStyleSheet('background-color: lightyellow;')
    else:
        print('Nada selecionado')

app=QtWidgets.QApplication([])
form = uic.loadUi('Window.ui')
form.pushButton.clicked.connect(main_function)

form.show()
app.exec()