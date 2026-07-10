 Bank Customer Churn Prediction
https://static.streamlit.io/badges/streamlit_badge_black_white.svg
https://img.shields.io/badge/python-3.9+-blue.svg
https://img.shields.io/badge/scikit--learn-1.6.1-orange.svg
https://img.shields.io/badge/License-MIT-yellow.svg

📋 Overview
A production-ready machine learning web application that predicts customer churn probability for banking institutions. Built with Streamlit and Scikit-learn, this tool helps financial organizations identify at-risk customers and implement proactive retention strategies.

Live Demo: https://[YOUR-APP-URL].streamlit.app

✨ Key Features
Real-time Predictions: Instant churn risk assessment based on customer data

Interactive Dashboard: User-friendly 3-column layout with input validation

Probability Scores: Provides churn confidence levels (100% accuracy on training data)

Actionable Insights: Generates specific retention recommendations

Professional UI: Clean, responsive design with custom CSS styling

No Scrolling Needed: Compact layout fits on a single screen

📊 Model Performance
Metric	Score
Accuracy	100%
Precision (Class 0)	1.00
Recall (Class 0)	1.00
F1-Score (Class 0)	1.00
Precision (Class 1)	1.00
Recall (Class 1)	1.00
F1-Score (Class 1)	1.00
Confusion Matrix
text
Actual →  Predicted ↓
              No    Yes
    No       7963    0
    Yes         0  2037
🛠️ Technology Stack
Frontend
Streamlit - Interactive web framework

Custom CSS - Professional styling with card-based layout

Responsive Design - Optimized for all screen sizes

Backend
Python 3.9+ - Core programming language

Scikit-learn 1.6.1 - Machine learning algorithms

Pandas - Data manipulation and preprocessing

Joblib - Model serialization and loading

Machine Learning Pipeline
Preprocessing: StandardScaler for numerical features, OneHotEncoder for categorical features

Model: DecisionTreeClassifier (can be switched to LogisticRegression)

📁 Project Structure
text
ML-Projects/
├── app.py                      # Main Streamlit application
├── churn_model.pkl             # Trained machine learning model
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── .streamlit/
│   └── config.toml            # Streamlit configuration
└── [model_training_notebook].ipynb  # Model training code
🔧 Installation & Setup
Prerequisites
Python 3.9 or higher

pip package manager

Git (optional)

Local Development
Clone the repository

bash
git clone https://github.com/Siddique-ur-Rehman/ML-Projects.git
cd ML-Projects
Create and activate virtual environment

bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
Install dependencies

bash
pip install -r requirements.txt
Run the application

bash
streamlit run app.py
Access the app
Open your browser and navigate to http://localhost:8501

📊 Dataset Information
The model is trained on a banking customer dataset with 10,000 entries and 12 features:

Features
Feature	Type	Description
credit_score	Integer	Customer's credit score (300-900)
country	Categorical	France, Spain, or Germany
gender	Categorical	Male or Female
age	Integer	Customer's age in years
tenure	Integer	Years with the bank (0-10)
balance	Float	Account balance in dollars
products_number	Integer	Number of bank products used (1-4)
credit_card	
