from flask import Flask

app = Flask(__name__) 
"""
__name__ 

O único argumento necessário para o construtor da classe Flask 
é o nome do módulo principal ou do pacote do aplicativo. 
Para a maioria dos aplicativos, a variável __name__ do Python 
é o valor correto para esse argumento.

O argumento __name__ que é passado para o construtor de aplicativos 
Flask é uma fonte de confusão entre os novos desenvolvedores do Flask.

O Flask usa esse argumento para determinar a localização do aplicativo, 
que, por sua vez, permite localizar outros arquivos que fazem parte do 
aplicativo, como imagens e modelos
"""

def index():
    return '<h1>Hello World!</h1>'

app.add_url_rule('/', 'index', index)

"""
O exemplo anterior registra a função index () como o manipulador do URL 
raiz do aplicativo.

Enquanto o decorador app.route é o método preferido para registrar funções 
de exibição, o Flask também oferece uma maneira mais tradicional de configurar 
as rotas de aplicativos com o método app.add_url_rule()

usa três argumentos: a URL, o endpoint name e a função view. 
"""