import pickle
from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

with open(file='model.pkl', mode='rb') as model_file:
    model = pickle.load(model_file)

with open(file='vectorizer.pkl', mode='rb') as vectorizer_file:
    vectorize = pickle.load(vectorizer_file)


# Define the /predict endpoint
@app.route("/")
def root():
    return jsonify({"author" : "sambhavmehta"})

@app.route("/predict", methods=["GET", "POST"]) 
def predict():
    if request.method == "POST":
        # Get the input text
        data = request.json
        review_text = data.get("review_text")

        if not review_text:
            return jsonify({"error": "No review_text provided"}), 400
        
        review_tfidf = vectorize.transform([review_text])

        prediction = model.predict(review_tfidf)
        return jsonify({"sentiment_prediction": prediction[0]})
    
    elif request.method == "GET":
        # For testing purposes, return a simple message
        return "Send a POST request with 'review_text' to get a sentiment prediction."
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

