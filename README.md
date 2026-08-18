# Instalar APIs

pip install Flask
pip install pytest

## Como ejecutar

py app.py
py test_app.py

El servidor se iniciará localmente en `http://127.0.0.1:5000/saludar`

## Endpoints disponibles

* **`GET /saludar`**
  * **Descripción:** Retorna un objeto JSON con los textos solicitados.
  * **Ejemplo de respuesta:**
    \`\`\`json
    {
      "mensaje": [
        "saludo",
        "hola"
      ]
    }
    \`\`\`
