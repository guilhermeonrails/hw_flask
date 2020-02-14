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
Clientes como navegadores da web enviam solicitações ao servidor da web, 
que por sua vez as envia para a instância do aplicativo Flask.

A instância do aplicativo Flask precisa saber qual código precisa ser 
executado para cada URL solicitada, para manter um mapeamento de URLs 
para as funções do Python. A associação entre uma URL e a função que 
lida com ela é chamada de rota

Decoradores são um recurso padrão da linguagem Python. 
Um uso comum de decoradores é registrar funções como funções de 
manipulador a serem chamadas quando certos eventos ocorrerem.
"""