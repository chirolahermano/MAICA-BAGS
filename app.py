from flask import Flask, render_template

app = Flask(__name__)

# Solo necesitamos esta ruta simple para servir tu página
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)