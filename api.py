from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return jsonify({'prompt' : 'Welcome to restful api'})

if __name__ == '__main__':
    app.run(debug=True)