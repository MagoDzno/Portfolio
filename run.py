from flask import Flask


# Instanciar flask

app = Flask(__name__)

# Crear rutas con sus funciones

@app.route('/')
def HolaMundo():
    return 'Hola mundo!'


@app.route('/mis-proyectos')
def mostrarProyectos():
    return  'Estos son mis proyectos'


# ejecucion
if __name__ == '__main__':
    app.run(debug=True)
