from flask import Flask, request, render_template, send_from_directory
import os

app = Flask(__name__)



@app.route("/", methods=["GET"])
def first_route():
    return render_template("index.html")

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/projects", methods=["GET"])
def project():
    return render_template("projects.html")
 

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)