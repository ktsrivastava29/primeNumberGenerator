from flask import Flask, request
import primeNoGenerator

app = Flask(__name__)

@app.route("/result", methods = ["POST", "GET"])
def result():
    output = request.get_json()

    if len(output.keys()) < 2:
        return {"Status": "Bad Response"}

    primeNumbers = primeNoGenerator()
    return primeNumbers

if __name__ == '__main__':
    app.run(debug=True, port = 2000)