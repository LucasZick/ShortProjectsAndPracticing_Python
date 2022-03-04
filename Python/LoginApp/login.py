from os import remove
from PyQt5 import uic,QtWidgets
import time
import sqlite3

def chamaTelaLogin():
    telaLogin.show()

def chamaTelaRegistro():
    telaRegistro.show()
    telaLogin.close()
        
def chamaTelaPrincipal():
    telaPrincipal.show()
    telaLogin.close()
    if telaRegistro:
        telaRegistro.close()
    atualizarTabela()

def chamaTelaInserirPessoa():
    telaPrincipal.close()
    telaInserirPessoa.show()

def chamaTelaRemoverPessoa():
    telaPrincipal.close()
    telaRemoverPessoa.show()

def login():
    login_usuario = telaLogin.lineEdit_login.text()
    senha_usuario = telaLogin.lineEdit_senha.text()
    if senha_usuario != '' and login_usuario != '':
        banco = sqlite3.connect('banco_cadastro.db')
        cursor = banco.cursor()   
        try:
            cursor.execute(f"SELECT senha FROM cadastro WHERE login = '{login_usuario}'")
            senha_bd = cursor.fetchall()
            banco.close()
            if senha_usuario == senha_bd[0][0]:
                chamaTelaPrincipal()
            else:
                telaLogin.label_aviso.setText('A senha está incorreta.')
        except:
            telaLogin.label_aviso.setText('Registro incompatível.')
    else:
        telaLogin.label_aviso.setText('Dados insuficientes para realizar o login.')

def logout():
    telaPrincipal.close()
    telaLogin.show()
    telaLogin.lineEdit_login.setText('')
    telaLogin.lineEdit_senha.setText('')
    telaLogin.label_aviso.setText('')

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

            sairRegistro()

        except sqlite3 as erro:
            telaRegistro.label_aviso.setText('Erro ao cadastrar o usuário.', erro)

    else:
        telaRegistro.label_aviso.setText('Cheque se preencheu todos os dados\ne confirme-se que as senhas estão iguais.')

def inserirAluno():
    turno = ''
    van = ''
    try:    
        nome = telaInserirPessoa.lineEdit_nome.text()
        nomePai = telaInserirPessoa.lineEdit_nomePai.text()
        nomeMae = telaInserirPessoa.lineEdit_nomeMae.text()
        telefone = telaInserirPessoa.lineEdit_telefone.text()
        endereco = telaInserirPessoa.lineEdit_endereco.text()
        escola = telaInserirPessoa.lineEdit_escola.text()
        mensalidade = int(telaInserirPessoa.lineEdit_mensalidade.text())
    except ValueError as erro:
        telaInserirPessoa.label_aviso.setText(f'A mensalidade necessita estar em números.\n Ex(250).{erro}')

    #Molda a variável turno
    if telaInserirPessoa.radioButton_manha.isChecked() == True:
        turno = turno+' Manhã.'
    if telaInserirPessoa.radioButton_tarde.isChecked() == True:
        turno = turno+' Tarde. '
    if telaInserirPessoa.radioButton_noite.isChecked() == True:
        turno = turno+' Noite.'

    #Molda a variável van
    if telaInserirPessoa.radioButton_van1.isChecked() == True:
        van = 'Van 1'
    if telaInserirPessoa.radioButton_van2.isChecked() == True:
        van = 'Van 2'

    try:
        if nome != '' and (nomePai != '' or nomeMae != '') and telefone != '' and endereco != '' and escola != '' and mensalidade:
            try:
                banco = sqlite3.connect('banco_alunos.db')
                cursor = banco.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS alunos (nome text, nome_do_pai text, nome_da_mae text, telefone text, endereco text, escola text, mensalidade int, turno text, van text)")
                cursor.execute(f"INSERT INTO alunos(nome,nome_do_pai,nome_da_mae,telefone,endereco,escola,mensalidade,turno,van) VALUES ('{nome}','{nomePai}','{nomeMae}','{telefone}','{endereco}','{escola}',{mensalidade},'{turno}','{van}')")

                banco.commit()
                banco.close

                atualizarTabela()
                sairInsercao()

            except Exception as erro:
                telaInserirPessoa.label_aviso.setText(f'Erro ao cadastrar o aluno.{erro}')

        else:
            telaInserirPessoa.label_aviso.setText('Problema ao inserir aluno, verifique se\n todos os campos foram preenchidos.')
    except:
            telaInserirPessoa.label_aviso.setText(f'A mensalidade necessita estar em números.\n Ex: (100).')

def verificarAluno():
    try:
        codigoAluno = telaRemoverPessoa.lineEdit_codigo.text()
        banco = sqlite3.connect('banco_alunos.db')
        cursor = banco.cursor()
        cursor.execute(f"SELECT nome FROM alunos WHERE codigo = {codigoAluno}")
        nome = cursor.fetchall()
        banco.close()
        if nome != '':
            telaRemoverPessoa.label_aviso.setText(f'Realmente deseja remover {nome[0][0]}?')
            telaRemoverPessoa.pushButton_remover.setEnabled(True)
    except:
        telaRemoverPessoa.label_aviso.setText('Erro ao buscar o aluno.\nVerifique se este código existe.')

def removerAluno():
    try:
        codigoAluno = telaRemoverPessoa.lineEdit_codigo.text()
        banco = sqlite3.connect('banco_alunos.db')
        cursor = banco.cursor()
        cursor.execute(f'DELETE FROM alunos WHERE codigo = {codigoAluno}')
        banco.commit()
        banco.close()
        atualizarTabela()
        sairRemocao()
    except:
        telaRemoverPessoa.label_aviso.setText('Erro ao remover aluno.')

def sairRegistro():
    telaRegistro.close()
    telaLogin.show()
    telaRegistro.lineEdit_nome.setText('')
    telaRegistro.lineEdit_loginCadastro.setText('')
    telaRegistro.lineEdit_senhaCadastro.setText('')
    telaRegistro.lineEdit_senhaConfirma.setText('')
    telaRegistro.label_aviso.setText('')


def sairInsercao():
    telaInserirPessoa.close()
    telaPrincipal.show()
    telaInserirPessoa.lineEdit_nome.setText('')
    telaInserirPessoa.lineEdit_nomePai.setText('')
    telaInserirPessoa.lineEdit_nomeMae.setText('')
    telaInserirPessoa.lineEdit_telefone.setText('')
    telaInserirPessoa.lineEdit_endereco.setText('')
    telaInserirPessoa.lineEdit_escola.setText('')
    telaInserirPessoa.lineEdit_mensalidade.setText('')
    telaInserirPessoa.label_aviso.setText('')
    telaInserirPessoa.radioButton_manha.setChecked(False)
    telaInserirPessoa.radioButton_tarde.setChecked(False)
    telaInserirPessoa.radioButton_noite.setChecked(False)
    telaInserirPessoa.radioButton_van1.setChecked(False)
    telaInserirPessoa.radioButton_van2.setChecked(False)

def sairRemocao():
    telaRemoverPessoa.close()
    telaPrincipal.show()
    telaRemoverPessoa.lineEdit_codigo.setText('')
    telaRemoverPessoa.label_aviso.setText('')
    telaRemoverPessoa.pushButton_remover.setEnabled(False)

def atualizarTabela():
    try:
        banco = sqlite3.connect('banco_alunos.db')
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM alunos")
        dadosTabela = cursor.fetchall()
        telaPrincipal.tableWidget_1.setRowCount(len(dadosTabela))
        telaPrincipal.tableWidget_1.setColumnCount(10)

        for i in range(0, len(dadosTabela)):
            for j in range(0,10):
                telaPrincipal.tableWidget_1.setItem(i,j,QtWidgets.QTableWidgetItem(str(dadosTabela[i][j])))
        
        banco.close()

    except:
        return


app = QtWidgets.QApplication([])

#ATRIBUIÇÃO DE INTERFACES
telaLogin = uic.loadUi('LoginWindow.ui')
telaRegistro = uic.loadUi('RegisterWindow.ui')
telaPrincipal = uic.loadUi('MainWindow.ui')
telaInserirPessoa = uic.loadUi('InsertPerson.ui')
telaRemoverPessoa = uic.loadUi('RemovePerson.ui')

#TELA DE LOGIN
telaLogin.pushButton_login.clicked.connect(login)
telaLogin.pushButton_cadastre.clicked.connect(chamaTelaRegistro)

#TELA DE REGISTRO DE USUARIO
telaRegistro.pushButton_cadastrar.clicked.connect(cadastrar)
telaRegistro.pushButton_cancelar.clicked.connect(sairRegistro)

#TELA DO SISTEMA
telaPrincipal.pushButton_logout.clicked.connect(logout)
telaPrincipal.pushButton_inserir.clicked.connect(chamaTelaInserirPessoa)
telaPrincipal.pushButton_remover.clicked.connect(chamaTelaRemoverPessoa)

#TELA DE INSERÇÃO DE ALUNO
telaInserirPessoa.pushButton_cancelar.clicked.connect(sairInsercao)
telaInserirPessoa.pushButton_cadastrar.clicked.connect(inserirAluno)

#TELA DE REMOÇÃO DE ALUNO
telaRemoverPessoa.pushButton_cancelar.clicked.connect(sairRemocao)
telaRemoverPessoa.pushButton_verificar.clicked.connect(verificarAluno)
telaRemoverPessoa.pushButton_remover.clicked.connect(removerAluno)

telaLogin.show()
app.exec()