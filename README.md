# 🧪 Práctica 2 - Flask API

Este proyecto contiene una API sencilla desarrollada con Flask. El objetivo es practicar el manejo de rutas, parámetros de consulta y respuestas HTTP. La colección de Postman incluida permite probar el endpoint de forma rápida.

---

## 🚀 Endpoint disponible

### `GET /user/api/v1/saludo`

- **URL completa:** `http://127.0.0.1:5000/user/api/v1/saludo?id=777`
- **Método:** `GET`
- **Parámetro de consulta:**  
  - `id` (opcional): Si se proporciona, devuelve un mensaje con el ID del usuario. Si no se proporciona, devuelve una lista genérica.

#### 📥 Ejemplo de solicitud con parámetro

```http
GET http://127.0.0.1:5000/user/api/v1/saludo?id=777
```

#### 📤 Ejemplo de respuesta

```text
El id del usuario es 777
```

#### 📥 Ejemplo de solicitud sin parámetro

```http
GET http://127.0.0.1:5000/user/api/v1/saludo
```

#### 📤 Ejemplo de respuesta

```text
Lista de los usuarios.
```

---

## 🛠️ Requisitos

- Python 3.x
- Flask
- Postman (opcional, para pruebas manuales)

---

## ⚙️ Instalación y ejecución

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/practica2-flask.git
   cd practica2-flask
   ```

2. Instala Flask:
   ```bash
   pip install flask
   ```

3. Ejecuta el servidor:
   ```bash
   python main.py
   ```

---

## 🧪 Pruebas con Postman

1. Abre Postman.
2. Ejecuta la solicitud `GET` incluida en la colección.
3. Verifica la respuesta en la pestaña "Body".

---

## 📌 Notas adicionales

- Puedes modificar el valor del parámetro `id` para probar diferentes respuestas.
- Este proyecto es parte de una práctica académica para aprender sobre APIs REST con Flask.
- El servidor corre en modo `debug`, lo que facilita el desarrollo y la depuración.

---

## 👨‍💻 Autor

**Julián Hernández**
