from flask import Flask, jsonify, request
app = Flask(__name__)

languages = [{'name' : 'Javascript'}, {'name' : 'Python'}, {'name' : 'Ruby'}]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'prompt' : 'Welcome to restful api'})

@app.route('/lang', methods=['GET'])
def returnAll():
    return jsonify({'languages' : languages})

@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
    langs = [language for language in languages if language['name'] == name]
    return jsonify({'language' : langs[0]})

@app.route('/lang', methods=['POST'])
def addOne():
    addition ={'name' : request.get_json(['name'])}

    languages.append(addition)
    return jsonify({'languages' : languages})  

if __name__ == '__main__':
    app.run(debug=True)