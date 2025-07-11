from flask import Flask, request

app = Flask(__name__)

@app.route('/user/api/v1/saludo', methods=['GET'])
def saludo_user():
    user_id = request.args.get('id')
    if user_id:
        return f"El id del usuario es {user_id}", 200
    else:
        return "Lista de los usuarios.", 200

if __name__ == '__main__':
    app.run(debug=True)