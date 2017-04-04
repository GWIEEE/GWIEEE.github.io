from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')

def index():
    return render_template("theme index.html")

@app.route("/theme")
def theme():
    return render_template("theme index.html")
@app.route('/home/<name>')
def home(name):
    return "<h1>This is the home page<h1><br/>Hello %s" %name
if __name__ == "__main__":
    app.run(debug=True)
