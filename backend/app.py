from flask import Flask, request, jsonify
import pickle
import re
from flask_cors import CORS
import string

# Load the vectorizer and models
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)
with open("logistic_model.pkl", "rb") as f:
    logistic_model = pickle.load(f)
with open("decision_tree.pkl", "rb") as f:
    decision_tree_model = pickle.load(f)
with open("gradient_boost.pkl", "rb") as f:
    gradient_boost_model = pickle.load(f)
with open("random_forest.pkl", "rb") as f:
    random_forest_model = pickle.load(f)

# Define model accuracies
model_accuracies = {
    "Logistic Regression": 0.986,  
    "Decision Tree": 0.995,
    "Gradient Boosting": 0.994,
    "Random Forest": 0.991,
}

def clean_text(text):
    """Apply the same preprocessing as in training."""
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(rf'[{re.escape(string.punctuation)}]', '', text)
    text = re.sub(r'\n', '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    return text

def predict_news(news):
    """Run predictions for all models and calculate fakeness percentage."""
    processed_news = clean_text(news)
    transformed_text = vectorizer.transform([processed_news])
    
    predictions = {}
    fake_models = []
    
    # Get predictions from all models
    for model_name, model in [
        ("Logistic Regression", logistic_model),
        ("Decision Tree", decision_tree_model),
        ("Gradient Boosting", gradient_boost_model),
        ("Random Forest", random_forest_model),
    ]:
        pred = model.predict(transformed_text)[0]
        predictions[model_name] = "Fake News" if pred == 0 else "Not Fake News"
        if pred == 0:  # If the model says "Fake News"
            fake_models.append(model_name)
    
    # Calculate fakeness percentage
    total_models = len(predictions)
    if fake_models:
        avg_accuracy = sum(model_accuracies[model] for model in fake_models) / len(fake_models)
        fakeness_percentage = (len(fake_models) / total_models) * avg_accuracy * 100
    else:
        fakeness_percentage = 0.0
    
    # Add fakeness percentage to the results
    predictions["Fakeness Percentage"] = f"{fakeness_percentage:.2f}%"
    
    return predictions

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    return "Welcome to the Fake News Detection API. Use the `/predict` endpoint to check news content."

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    news = data.get("news", "")
    if not news:
        return jsonify({"error": "No news content provided"}), 400
    predictions = predict_news(news)
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True)
