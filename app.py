from flask import Flask, render_template
import turtle

app = Flask(__name__)

@app.route('/')
def index():
    # Configuración de Turtle
    screen = turtle.Screen()
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.speed(20)

    # Agregar el texto en la cabecera
    header_text = "TE AMO MI MONITA"
    t.penup()
    t.goto(-180, 250)
    t.pendown()
    t.color("white")
    t.write(header_text, align="left", font=("Arial", 12, "normal"))

    # Dibujar el tallo verde del girasol
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.color("green")
    t.begin_fill()
    t.rt(90)
    t.fd(400)
    t.lt(90)
    t.fd(20)
    t.lt(90)
    t.fd(400)
    t.lt(90)
    t.fd(20)
    t.end_fill()

    # Dibujar el girasol
    t.penup()
    t.goto(0, 0)
    t.pendown()
    for i in range(16):
        for j in range(18):
            t.color("yellow")  # Todos los pétalos son amarillos
            t.rt(90)
            t.circle(150 - j * 6, 90)
            t.lt(90)
            t.circle(150 - j * 6, 90)
            t.rt(180)
        t.circle(40, 24)

    # Colorear el centro de marrón
    t.penup()
    t.goto(-20, 0)
    t.pendown()
    t.color("brown")
    t.begin_fill()
    t.circle(44)  # Ajustar el radio del centro
    t.end_fill()

    # Guardar el dibujo
    ts = turtle.getscreen()
    ts.getcanvas().postscript(file="static/dibujo.eps")
    
    # Finalizar
    turtle.done()
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
