# Servidor Flask - Endpoint Saludar

Este proyecto es un servidor web básico desarrollado en Python utilizando el microframework **Flask**.

## Requisitos previos

Asegúrate de tener instalado **Python** (versión 3.8 o superior) en tu sistema.

## Librerías a instalar

La única dependencia externa necesaria para este proyecto es **Flask**. 

Puedes instalarla ejecutando el siguiente comando en tu terminal:

\`\`\`bash
pip install Flask
\`\`\`

O si prefieres utilizar un archivo de requerimientos, puedes crear un archivo `requirements.txt` con el siguiente contenido:

\`\`\`text
Flask>=3.0.0
\`\`\`

Y luego instalarlo con:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

## Cómo ejecutar el servidor

1. Abre tu terminal en la carpeta del proyecto.
2. Ejecuta el script de Python:
   \`\`\`bash
   python app.py
   \`\`\`
3. El servidor se iniciará localmente en `http://127.0.0.1:5000/saludar`.

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
