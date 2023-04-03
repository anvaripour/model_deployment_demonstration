from flask import Flask, jsonify, request
from transformers import pipeline

app = Flask(__name__)

sentiment_analysis_pipeline = pipeline(
    "text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

@app.route('/api/predict', methods=['POST'])
def predict():
    text = request.json['text']
    result = sentiment_analysis_pipeline(text)[0]
    label = result['label']
    score = result['score']
    response = {'label': label, 'score': score}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
