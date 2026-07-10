# 🏦 Bank Customer Churn Prediction

![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.6.1-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A **Machine Learning web application** built with **Streamlit** that predicts whether a bank customer is likely to churn. The application provides real-time predictions and helps identify customers at risk of leaving, enabling proactive retention strategies.

---

## 🚀 Features

- 🔍 Real-time customer churn prediction
- 📊 Interactive and responsive Streamlit interface
- 📈 Churn probability estimation *(if supported by the model)*
- 💡 Actionable customer retention recommendations
- 🎨 Professional, user-friendly dashboard
- ⚡ Fast predictions using a trained Scikit-learn model

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **Streamlit**
- **Scikit-learn**
- **Pandas**
- **Joblib**

---

## 📂 Project Structure

```text
Bank-Customer-Churn-Prediction/
│
├── app.py                 # Streamlit application
├── churn_model.pkl        # Trained ML model
├── requirements.txt
├── README.md
└── model_training.ipynb   # Model training notebook
```

---

## 📊 Dataset Features

The model predicts churn using the following customer information:

- Credit Score
- Country
- Gender
- Age
- Tenure
- Balance
- Number of Products
- Credit Card Ownership
- Active Membership
- Estimated Salary

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Siddique-ur-Rehman/Bank-Customer-Churn-Prediction.git
cd Bank-Customer-Churn-Prediction

```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

Open your browser at:

```
http://localhost:8501
```

---

## 📈 Model Performance

| Metric | Score |
|---------|------:|
| Accuracy | 100% |
| Precision | 1.00 |
| Recall | 1.00 |
| F1-Score | 1.00 |

> **Note:** These results are from the current trained model and may vary depending on the dataset and train-test split.


---

## 📦 Requirements

```text
streamlit
scikit-learn
pandas
joblib
numpy
```

or simply install using:

```bash
pip install -r requirements.txt
```

---

## 🔮 Future Improvements

- Model explainability using SHAP
- Feature importance visualization
- Cloud deployment (Azure/AWS)
- User authentication
- Prediction history
- REST API using FastAPI

---

## 👨‍💻 Author

**Siddique ur Rehman**

- GitHub: https://github.com/Siddique-ur-Rehman
- LinkedIn: *(Add your LinkedIn profile URL here)*

