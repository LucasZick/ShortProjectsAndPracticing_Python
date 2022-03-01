from PyQt5 import uic,QtWidgets

def chamaTelaLogin():
    telaLogin.show()

def chamaTelaRegistro():
    telaRegistro.show()
    telaLogin.close()
        
def chamaTelaPrincipal(usuario):
    telaPrincipal.show()
    telaLogin.close()
    if telaRegistro:
        telaRegistro.close()
    telaPrincipal.labelWelcome.setText(f'Bem vindo {usuario}!')

def login():
    login_usuario = telaLogin.lineEdit_login.text()
    senha_usuario = telaLogin.lineEdit_senha.text()
    if login_usuario == 'lucaszick' and senha_usuario == '123456':
        telaLogin.label_aviso.setText('Login realizado!')
        chamaTelaPrincipal(login_usuario)
    else:
        telaLogin.label_aviso.setText(f'A conta {login_usuario} não existe\nou sua senha está incorreta.')

def logout():
    telaPrincipal.close()
    telaLogin.show()

def cadastrar():
    telaRegistro.close()
    telaLogin.show()


app = QtWidgets.QApplication([])
telaLogin = uic.loadUi('LoginWindow.ui')
telaRegistro = uic.loadUi('RegisterWindow.ui')
telaPrincipal = uic.loadUi('MainWindow.ui')

telaLogin.pushButton_login.clicked.connect(login)
telaLogin.pushButton_cadastre.clicked.connect(chamaTelaRegistro)

telaRegistro.pushButton_cadastrar.clicked.connect(cadastrar)

telaPrincipal.pushButton_logout.clicked.connect(logout)


telaLogin.show()
app.exec()