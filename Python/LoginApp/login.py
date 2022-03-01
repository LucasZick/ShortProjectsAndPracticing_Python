from PyQt5 import uic,QtWidgets
import sqlite3

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
    if senha_usuario != '' and login_usuario != '':
        banco = sqlite3.connect('banco_cadastro.db')
        cursor = banco.cursor()   
        try:
            cursor.execute(f"SELECT senha FROM cadastro WHERE login = '{login_usuario}'")
            senha_bd = cursor.fetchall()
            print(senha_bd[0][0])
            banco.close()
        except:
            telaLogin.label_aviso.setText('Registro incompatível.')
    else:
        telaLogin.label_aviso.setText('Dados insuficientes para realizar o login.')

def logout():
    telaPrincipal.close()
    telaLogin.show()

def cadastrar():
    nome = telaRegistro.lineEdit_nome.text()
    login = telaRegistro.lineEdit_loginCadastro.text()
    senha = telaRegistro.lineEdit_senhaCadastro.text()
    senhaConfirma = telaRegistro.lineEdit_senhaConfirma.text()

    if (login != '' and nome != '' and senha == senhaConfirma):
        try:
            banco = sqlite3.connect('banco_cadastro.db')
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text, login text, senha text)")
            cursor.execute("INSERT INTO cadastro VALUES ('"+nome+"','"+login+"','"+senha+"')")

            banco.commit()
            banco.close

            telaRegistro.close()
            telaLogin.show()

        except sqlite3 as erro:
            telaRegistro.label_aviso.setText('Erro ao cadastrar o usuário.', erro)

    else:
        telaRegistro.label_aviso.setText('Cheque se preencheu todos os dados e reescreva as senhas de modo que fiquem iguais!')


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