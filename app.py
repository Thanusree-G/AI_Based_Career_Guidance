from flask import Flask, render_template, request
from career_model import recommend_path

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    education = request.form["education"]
    coding = int(request.form["coding"])
    math = int(request.form["math"])
    communication = int(request.form["communication"])
    interest = request.form["interest"]

    result = recommend_path(
        education,
        coding,
        math,
        communication,
        interest
    )

    return render_template(
        "result.html",
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)