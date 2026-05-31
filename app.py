import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

# Flask para que busque los archivos estáticos (CSS/imágenes) en 'static'
# permitE acceder a ellos(sin cambiar tus rutas de HTML)
app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

# NUMERO DE WHAT
NUMERO_WA = "573215413928"

CONOCIMIENTO = {
    "historia": "Café Los Cerezos nace en la finca El Cerezo, ubicada en San Bernardo, Cundinamarca.",
    "ubicacion": "Estamos ubicados en San Bernardo, una zona ideal para café de alta calidad ☕",
    "precios": """
☕ Café molido 1Kg → $15.000 COP
☕ Bolsa café en grano → $10.000 COP
☕ Café Premium → $18.000 COP
☕ Café Orgánico → $22.000 COP
""",
    "envios": "Realizamos envíos a toda Colombia 🚚",
    "variedades": "Café molido, premium, orgánico y café en grano."
}

def responder(mensaje):
    mensaje = mensaje.lower()
    
    # LINKS DINÁMICOS
    ws_link = f"https://wa.me/{NUMERO_WA}?text=Hola%20Café%20Los%20Cerezos,%20quiero%20hacer%20un%20pedido"
    ig_link = "https://www.instagram.com/cafeloscerezos"

    # 1. Saludos
    if any(p in mensaje for p in ["hola", "buen dia", "buenas", "hey"]):
        return "¡Hola! ☕ Soy Alejandra, tu barista de Café Los Cerezos. ¿Te gustaría conocer nuestra historia, ubicación o ver nuestros productos y precios?"

    # 2. Instagram / Redes
    if any(p in mensaje for p in ["instagram", "redes", "fotos", "ig", "social"]):
        return f"¡Claro! Síguenos en Instagram para ver el día a día en la finca: {ig_link} 📸"

    # 3. Compras y Pedidos
    if any(p in mensaje for p in ["comprar", "pedido", "ordenar", "quiero café"]):
        return f"¡Excelente elección! ☕ Puedes realizar tu pedido directamente en nuestro WhatsApp aquí: {ws_link}"

    # 4. Sobre San Bernardo / Ubicación / Historia
    if any(p in mensaje for p in ["donde", "ubicacion", "quienes", "finca", "san bernardo", "historia"]):
        return f"{CONOCIMIENTO['historia']} {CONOCIMIENTO['ubicacion']}"

    # 5. Precios
    if any(p in mensaje for p in ["precio", "cuanto", "vale", "costo", "valor"]):
        return f"Claro, mira: {CONOCIMIENTO['precios']} ¿Te gustaría que te ayude a armar un pedido por WhatsApp?"

    # 6. Envíos
    if any(p in mensaje for p in ["envio", "domicilio", "mandan", "llega"]):
        return CONOCIMIENTO['envios']

    # 7. Recomendaciones y Variedades
    if any(p in mensaje for p in ["producto", "menu", "recomienda", "tipos", "variedad"]):
        return f"Tenemos opciones para todos los gustos: {CONOCIMIENTO['variedades']} Te recomiendo el Premium si buscas notas frutales."

    # 8. Contacto directo
    if any(p in mensaje for p in ["telefono", "whatsapp", "numero", "celular", "contacto"]):
        return f"¡Claro! Mi WhatsApp es {NUMERO_WA}. O dale clic aquí: {ws_link} 📱"

    # 9. Despedida
    if any(p in mensaje for p in ["gracias", "adios", "chao", "listo"]):
        return "¡Con gusto! Espero que disfrutes de un excelente café Los Cerezos hoy. ☕✨"

    # 10. RESPUESTA POR DEFECTO
    return "No estoy segura de eso, pero puedo contarte sobre nuestros precios, nuestra finca en San Bernardo o darte nuestro Instagram. ☕"



# RUTAS PARA NAVEGAR EN LA PÁGINA WEB


@app.route("/")
@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/productos.html")
def productos():
    return render_template("productos.html")

@app.route("/galeria.html")
def galeria():
    return render_template("galeria.html")

@app.route("/sobrenosotros.html")
def sobre_nosotros():
    return render_template("sobrenosotros.html")

@app.route("/contactenos.html")
def contactenos():
    return render_template("contactenos.html")



# RUTA DEL CHATBOT


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    mensaje = data.get("mensaje", "")
    respuesta = responder(mensaje)
    return jsonify({"respuesta": respuesta})


# Inicio de la aplicación
if __name__ == "__main__":
    # Render asigna el puerto mediante la variable de entorno 'PORT'
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
