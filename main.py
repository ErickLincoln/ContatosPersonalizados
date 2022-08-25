from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/2')
#def rota2():
#    return         

if __name__ == '__main__':
        app.run(debug= True)