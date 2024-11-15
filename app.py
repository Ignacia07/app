from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from PIL import Image
import base64
import pygame
import io

app = Flask(__name__)
socketio = SocketIO(app)

# Inicializar la música
def iniciar_musica():
    pygame.mixer.init()
    pygame.mixer.music.load("Copia de wedding-song-247747.mp3")  # Ruta a tu archivo de música
    pygame.mixer.music.play(-1)

# Convertir imagen a base64 para pasarla a la web
def convertir_imagen_base64(ruta_imagen):
    with open(ruta_imagen, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("verificar_contraseña")
def handle_verificar_contraseña(data):
    if data["contraseña"] == "chingui":
        emit("mensaje_romantico", {"success": True})
    else:
        emit("mensaje_romantico", {"success": False, "error": "Contraseña incorrecta. ¡Vuelva a intentarlo!"})

@socketio.on("mostrar_boda")
def handle_mostrar_boda():
    iniciar_musica()
    imagen_base64 = convertir_imagen_base64("Copia de FxTQ9avaMAEcAIO.jpg")  # Ruta a tu imagen
    emit("mostrar_boda", {"mensaje": "¡Felicidades por su matrimonio!", "imagen": imagen_base64})

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", debug=True)
