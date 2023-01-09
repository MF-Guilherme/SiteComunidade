from main import app, database
from models import Usuario, Post


# with app.app_context():
#     database.create_all()

# with app.app_context():
#     usuario = Usuario(username="Guilherme", email="guilherme@teste.com", senha="123456")
#     usuario2 = Usuario(username="Joao", email="joao@teste.com", senha="123456")
#     database.session.add(usuario)
#     database.session.add(usuario2)
#     database.session.commit()

# with app.app_context():
#     usuario_teste = Usuario.query.filter_by(id=2).first()
#     print(usuario_teste.email)
    # meus_usuarios = Usuario.query.all()
    # print(meus_usuarios)
    # primeiro_usuario = Usuario.query.first()
    # print(primeiro_usuario.id)
    # print(primeiro_usuario.username)
    # print(primeiro_usuario.email)
    # print(primeiro_usuario.senha)
    # print(primeiro_usuario.posts)

# with app.app_context():
#     meu_post = Post(titulo="Primeiro posto do Guilherme", corpo="Guilherme voando", id_usuario=1)
#     database.session.add(meu_post)
#     database.session.commit()
#
# with app.app_context():
#     post = Post.query.first()
#     print(post.titulo)
#     print(post.corpo)
#     print(post.autor.email)

with app.app_context():
    database.drop_all()
    database.create_all()

