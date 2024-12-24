from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/building', methods=['POST', 'GET'])
def coords():
    data = request.form.get('data')
    # process the data using Python code
    if data == 'Kilburn Building':
        return "latitude:59.918; longitude:30.463"
    
if __name__ == "__main__":
    app.run(debug=True)