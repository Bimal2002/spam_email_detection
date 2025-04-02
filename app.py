from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

# Load the trained model and vectorizer
with open("spam_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("vectorizer.pkl", "rb") as vec_file:
    vectorizer = pickle.load(vec_file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json  # Get input text from frontend
    text = data.get("text", "")

    # Convert text into TF-IDF features
    text_vectorized = vectorizer.transform([text])

    # Predict spam or ham
    prediction = model.predict(text_vectorized)[0]

    # Return result
    return jsonify({"spam": bool(prediction)})

if __name__ == "__main__":
    app.run(debug=True)
