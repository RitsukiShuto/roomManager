from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<html><body><h1>sample</h1></body></html>'

if __name__ == '__main__':
    # app.run()
    app.run(debug=False, host='192.168.0.11', port=5000)