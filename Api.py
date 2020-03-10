from flask import Flask, escape, request
app = Flask(__name__)
@app.route('/')
def multiplicacion():
    entrada1 = request.args.get("numero1", type=int)
    entrada2 = request.args.get("numero2", type=int)
    resultadomulti = entrada1 * entrada2
    return f'Hello, {escape(resultadomulti)}!'

    