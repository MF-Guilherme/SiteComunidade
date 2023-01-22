from flask import render_template, request, flash, redirect, url_for
from comunidadeimpressionadora import app, database, bcrypt
from comunidadeimpressionadora.forms import FormLogin, FormCriarConta
from comunidadeimpressionadora.models import Usuario
from flask_login import login_user, logout_user, current_user

lista_usuarios = ['Lira', 'Joao', 'Alex', 'Alessandra']


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/contato")
def contato():
    return render_template('contato.html')


@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    # se o formulario foi validado ao submeter E o botão for o 'botao de login' (utilizando o AND pq temos 2 forms na mesma página
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            # exibir mensagem de login bem sucedido
            flash(f'login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
            # redirecionar para a homepage
            return redirect(url_for('home'))
        else:
            flash(f'Falha no login. E-mail ou Senha incorretos.', 'alert-danger')
    if form_criarconta.validate_on_submit() and 'botao_submit_criar_conta' in request.form:
        # instanciar o Usuario
        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_cript)
        # adicionar a sessão
        database.session.add(usuario)
        # commit na sessão
        database.session.commit()
        flash(f'Conta criada para o e-mail: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('home'))
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)


@app.route('/sair')
def sair():
    logout_user()
    flash(f'Logout feito com sucesso!', 'alert-success')
    return redirect(url_for('home'))


@app.route('/perfil')
def perfil():
    return render_template('perfil.html')


@app.route('/post/criar')
def criar_post():
    return render_template('criarpost.html')
