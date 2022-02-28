from PyQt5 import uic,QtWidgets

def list_data():
    data = Window.lineEdit.text()
    Window.listWidget.addItem(data)
    Window.lineEdit.setText('')

def delete_data():
    data = Window.lineEdit.text()
    Window.listWidget.clear()
    Window.lineEdit.setText('')

app=QtWidgets.QApplication([])
Window = uic.loadUi('Window.ui')
Window.pushButton.clicked.connect(list_data)
Window.pushButton_2.clicked.connect(delete_data)

Window.show()
app.exec()