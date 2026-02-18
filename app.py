from flask import Flask, request, jsonify
from model import analyze_sentiment

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "Text is required"}), 400

    result = analyze_sentiment(text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
