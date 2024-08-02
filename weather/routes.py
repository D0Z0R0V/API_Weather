from flask import Flask ,render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def base_index():
    return render_template("base.html")