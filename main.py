from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/api/data')
def data():
    return jsonify({
        "message": "Hello from Google App Engine!",
        "status": "success"
    })

if __name__ == '__main__':
    app.run(debug=True)
