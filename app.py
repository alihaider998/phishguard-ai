import os
from flask import Flask, render_template, request
from feature_extractor import extract_features
from model import predict

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    probability = None

    if request.method == "POST":
        url = request.form["url"]
        features = extract_features(url)
        result, probability = predict(features)

    return render_template("index.html", result=result, probability=probability)

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
