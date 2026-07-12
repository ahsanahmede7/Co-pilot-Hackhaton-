# 🤖 AI Loan Approval Co-Pilot

An AI-powered Loan Approval Assistant built using Machine Learning, Explainable AI (SHAP), Large Language Models (Groq/OpenAI), PDF report generation, and Human-in-the-Loop approval.

---

## 🚀 Features

- Loan Approval Prediction using Deep Learning (TensorFlow/Keras)
- Explainable AI using SHAP
- AI-generated decision explanation using LLM
- Human-in-the-Loop final approval
- PDF Loan Report Generation
- Interactive Streamlit UI

---

## 📂 Project Structure

```
.
├── app.py
├── prediction.py
├── explain.py
├── llm.py
├── human_loop.py
├── pdf_utils.py
├── best_model.keras
├── preprocessor.pkl
├── background_data.pkl
├── requirements.txt
├── README.md
├── .gitignore
└── .env (Not Included)
```

---

## 🛠 Technologies Used

- Python
- Streamlit
- TensorFlow / Keras
- Scikit-Learn
- SHAP
- Pandas
- NumPy
- OpenAI / Groq API
- ReportLab
- Joblib

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/ahsanahmede7/Co-pilot-Hackhaton-.git
```

Move into project

```bash
cd Co-pilot-Hackhaton-
```

Create virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a file named `.env`

```env
GROQ_API_KEY=your_groq_api_key
```

Do **NOT** upload your `.env` file to GitHub.

---

## ▶ Run Application

```bash
streamlit run app.py
```

---

## AI Workflow

```
User Input
      │
      ▼
Data Preprocessing
      │
      ▼
ANN Prediction
      │
      ▼
SHAP Explanation
      │
      ▼
LLM Decision Explanation
      │
      ▼
Human Review
      │
      ▼
PDF Report
```

---

## Human in the Loop

The bank officer can:

- Approve
- Reject
- Override AI Decision

The final decision is recorded in the generated report.

---

## Explainable AI

SHAP explains:

- Most important features
- Positive impact
- Negative impact
- Feature contribution

---

## Disclaimer

This project is intended for educational and demonstration purposes only and should not be used as the sole basis for real financial decisions.

---

## Author

**Ahsan Ahmed**

GitHub

https://github.com/ahsanahmede7