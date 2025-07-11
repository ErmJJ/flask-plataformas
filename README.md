# 🧪 Práctica 2 - Flask API

Este proyecto contiene una colección de Postman para probar un endpoint desarrollado con Flask. El objetivo es realizar una solicitud `GET` que devuelve un saludo personalizado basado en un parámetro `id`.

## 🚀 Endpoint disponible

### `GET /user/api/v1/saludo`

- **URL completa:** `http://127.0.0.1:5000/user/api/v1/saludo?id=777`
- **Método:** `GET`
- **Parámetro de consulta:**  
  - `id` (obligatorio): Identificador del usuario para generar el saludo.

#### 📥 Ejemplo de solicitud

```http
GET http://127.0.0.1:5000/user/api/v1/saludo?id=777
```

#### 📤 Ejemplo de respuesta esperada

```json
{
  "saludo": "Hola, usuario con ID 777"
}
```

> ⚠️ Asegúrate de que el servidor Flask esté corriendo en `localhost:5000` antes de realizar la solicitud.

---

## 🛠️ Requisitos

- Python 3.x
- Flask
- Postman (opcional, para pruebas manuales)

## 🧰 Instalación y ejecución

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/practica2-flask.git
   cd practica2-flask
   ```

2. Instala las dependencias:
   ```bash
   pip install flask
   ```

3. Ejecuta el servidor Flask:
   ```bash
   python app.py
   ```

4. Abre Postman y carga la colección `Practica 2 - Flask.postman_collection.json`.

---

## 📂 Estructura del proyecto

```
Practica2-Flask/
├── app.py
├── Practica 2 - Flask.postman_collection.json
└── README.md
```

---

## 🧪 Pruebas con Postman

1. Abre Postman.
2. Importa el archivo `Practica 2 - Flask.postman_collection.json`.
3. Ejecuta la solicitud `GET` incluida en la colección.
4. Verifica la respuesta en la pestaña "Body".

---

## 📌 Notas adicionales

- Puedes modificar el valor del parámetro `id` para probar diferentes respuestas.
- Este proyecto es parte de una práctica académica para aprender sobre APIs REST con Flask.

---

## 📜 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.

---

## 👨‍💻 Autor

**Julián Hernández** 
