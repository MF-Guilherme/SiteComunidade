from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormLogin, FormCriarConta

app = Flask(__name__)

lista_usuarios = ['Lira', 'Joao', 'Alex', 'Alessandra']

app.config['SECRET_KEY'] = 'fe7d7f6bde3b0ec4e090e64b6384caf1'


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
        # exibir mensagem de login bem sucedido
        flash(f'login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
        # redirecionar para a homepage
        return redirect(url_for('home'))
    if form_criarconta.validate_on_submit() and 'botao_submit_criar_conta' in request.form:
        flash(f'Conta criada para o e-mail: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('home'))
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)


if __name__ == '__main__':
    app.run(debug=True)
