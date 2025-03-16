from flask import Flask, request, jsonify
from src.main import Calculator

app = Flask(__name__)
calc = Calculator()

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    a = data['a']
    b = data['b']
    result = calc.add(a, b)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)