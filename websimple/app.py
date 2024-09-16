from flask import Flask, send_from_directory

app = Flask(__name__)

# Ruta para servir los archivos estáticos (HTML, CSS, JS)
@app.route('/')
def serve_html():
    return send_from_directory('.', 'index.html')  # Asegúrate de que 'index.html' esté en el mismo directorio que 'app.py'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
