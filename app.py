from flask import Flask, request, render_template
import os

app = Flask(__name__, )



@app.route("/", methods=["GET"])
def first_route():
    return render_template("index.html")

@app.route("/projects", methods=["GET", "POST"])
def projects():
    return render_template("projects.html")
 

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)