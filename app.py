from flask import Flask, render_template, request
from model import predict_website

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    url = request.form.get("url", "").strip()

    if not url:
        result = "Please enter a website URL."
    else:
        prediction = predict_website(url)

        if prediction == "phishing":
            result = "⚠️ Potential Phishing Website"
        else:
            result = "✅ Likely Legitimate Website"

    return render_template(
        "result.html",
        url=url,
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)