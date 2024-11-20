# Sentiment Analysis with Emotion Classification

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-v2.0+-green)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Transformers-orange)

This repository hosts a Flask-based web application for performing **sentiment analysis** and **emotion classification** on text data. Powered by the Hugging Face Transformers library, this application provides real-time insights into the sentiment and emotion of user-provided text.



-----  
### Technologies Used

- **Flask**: Lightweight web framework for Python.
- **Hugging Face Transformers**: Pre-trained NLP models for sentiment analysis.
- **Bootstrap**: Front-end framework for responsive design.

-----
## Features
- **Real-time Sentiment Analysis**: Analyze whether the input text has a positive, negative, or neutral sentiment.
- **Emotion Classification**: Detect the primary emotion conveyed by the text.
- **Confidence Scores**: Provides a confidence level for both sentiment and emotion predictions.
- **User-Friendly Interface**: Built with Bootstrap for a modern, responsive design.

-----

## Live Demo
Run the application locally and access it via [http://127.0.0.1:5000](http://127.0.0.1:5000).

-----

## Repository Contents
- `app.py`: Flask server and application routing logic.
- `sentiment_model.py`: NLP model logic using Hugging Face's Transformers pipeline.
- `templates/index.html`: Homepage with a form for user input.
- `templates/result.html`: Result page displaying the analysis output.

-----

## Installation

### Prerequisites
- Python 3.8 or higher
- `pip` (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/NIrmalpat3l/Senitment-Analysis.git
   ```
   
2. go to Senitment-Analysis directory
   ```bash
   cd Senitment-Analysis
   ```

3. run the following command
   ```bash
   python app.py
   ```
-----

### Open your web browser and navigate to:

http://127.0.0.1:5000

-----

### Example Usage

- Enter your text in the input box on the homepage.
- Click Analyze Sentiment to process the input.
- View the sentiment, emotion, and confidence scores on the result page.
