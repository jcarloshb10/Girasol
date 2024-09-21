from flask import Flask, render_template, send_file
from PIL import Image, ImageDraw

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dibujo')
def dibujo():
    # Crear una imagen en blanco
    img = Image.new('RGB', (400, 400), 'black')
    draw = ImageDraw.Draw(img)

    # Agregar el texto
    draw.text((10, 10), "TE AMO MI MONITA", fill='white')

    # Dibujar el tallo
    draw.rectangle([190, 100, 210, 500], fill='green')

    # Dibujar el girasol
    for i in range(16):
        for j in range(18):
            draw.ellipse([100 - j * 6, 100, 200 - j * 6, 200], fill='yellow')
    
    # Centro del girasol
    draw.ellipse([160, 160, 240, 240], fill='brown')

    # Guardar la imagen
    img.save('static/dibujo.png')

    return send_file('static/dibujo.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
