from flask import Flask, request, render_template
from sentiment_model import predict_sentiment

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    result = predict_sentiment(text)
    return render_template('result.html', text=text, result=result)

if __name__ == '__main__':
    app.run(debug=True)
