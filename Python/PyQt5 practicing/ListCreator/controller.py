from PyQt5 import uic,QtWidgets

def list_data():
    data = Window.lineEdit.text()
    if data:
        Window.listWidget.addItem(data)
        Window.lineEdit.setText('')

def delete_data():
    Window.listWidget.clear()

app=QtWidgets.QApplication([])
Window = uic.loadUi('ListCreator/Window.ui')
Window.pushButton.clicked.connect(list_data)
Window.pushButton_2.clicked.connect(delete_data)

Window.show()
app.exec()