from flask import Flask, render_template, request, jsonify
from PIL import Image
import base64
import pygame
import io
import os

app = Flask(__name__)

# Inicializar la música
def iniciar_musica():
    pygame.mixer.init()
    try:
        pygame.mixer.music.load("Copia de wedding-song-247747.mp3")  # Ruta a tu archivo de música
        pygame.mixer.music.play(-1)
    except pygame.error:
        print("Error: No se pudo cargar el archivo de música. Verifica la ruta.")

# Convertir imagen a base64 para pasarla a la web
def convertir_imagen_base64(ruta_imagen):
    try:
        with open(ruta_imagen, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")
    except FileNotFoundError:
        print("Error: No se pudo cargar la imagen. Verifica la ruta.")
        return None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/verificar_contraseña", methods=["POST"])
def verificar_contraseña():
    data = request.json
    if data["contraseña"] == "chingui":
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "error": "Contraseña incorrecta. ¡Vuelva a intentarlo!"})

@app.route("/mostrar_boda", methods=["POST"])
def mostrar_boda():
    iniciar_musica()
    imagen_base64 = convertir_imagen_base64("Copia de FxTQ9avaMAEcAIO.jpg")  # Ruta a tu imagen
    if imagen_base64:
        return jsonify({"mensaje": "¡Felicidades por su matrimonio!", "imagen": imagen_base64})
    else:
        return jsonify({"mensaje": "¡Felicidades por su matrimonio!", "imagen": ""})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
