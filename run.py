from flask import Flask, render_template


# Instanciar flask

app = Flask(__name__)


# Crear rutas con sus funciones
@app.route('/', methods=['GET'])
def index():
    return render_template('/index.html')


@app.route('/mis-proyectos', methods=['GET'])
def mostrarProyectos():
    return render_template('/mis-proyectos.html')


@app.route('/mi-blog', methods=['GET'])
def miBlog():
    return render_template('/mi-blog.html')


@app.route('/contacto', methods=['GET'])
def contacto():
    return render_template('/contacto.html')


# Ejecucion
if __name__ == '__main__':
    app.run(debug=True)
