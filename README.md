# 📩 Spam Detection App

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/NLTK-4EA94B?style=for-the-badge&logo=python&logoColor=white"/>
</p>

<p align="center">
  A machine learning–powered web app that classifies messages as <strong>Spam</strong> or <strong>Ham</strong> in real time — built with Python, NLTK, and Streamlit.
</p>

<p align="center">
  <a href="https://github.com/Ammarahmed-git/SpamDetectionApp">
    <img src="https://img.shields.io/github/stars/Ammarahmed-git/SpamDetectionApp?style=social" />
  </a>
  &nbsp;
  <a href="https://github.com/Ammarahmed-git/SpamDetectionApp/issues">
    <img src="https://img.shields.io/github/issues/Ammarahmed-git/SpamDetectionApp?color=red" />
  </a>
</p>

---

## 🚀 Live Demo

> ▶️ Try it out: **[SpamDetectionApp on Streamlit Cloud](https://spamdetectionapp.streamlit.app)**  
> *(Paste any SMS or email and get an instant prediction)*

---

## ✨ Features

- 🔍 **Real-time spam classification** — instant results as you type
- 🧹 **Text preprocessing pipeline** — lowercasing, punctuation removal, stopword filtering, stemming
- 📊 **Confidence score** — see how certain the model is
- 🧠 **Trained ML model** — Naive Bayes / TF-IDF vectorizer
- 🖥️ **Clean Streamlit UI** — no setup required, runs in the browser

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.10+ |
| UI Framework | Streamlit |
| NLP | NLTK (stopwords, stemming, tokenization) |
| ML | scikit-learn (Naive Bayes, TF-IDF) |
| Deployment | Streamlit Cloud |

---

## 📁 Project Structure

```
SpamDetectionApp/
├── app.py               # Main Streamlit application
├── model.pkl            # Trained ML model
├── vectorizer.pkl       # Fitted TF-IDF vectorizer
├── requirements.txt     # Python dependencies
└── README.md
```

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Ammarahmed-git/SpamDetectionApp.git
cd SpamDetectionApp
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Download NLTK data

```python
import nltk
nltk.download('stopwords')
nltk.download('punkt')
```

### 4. Run the app

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 🧪 How It Works

```
User Input
    ↓
Text Preprocessing (lowercase → remove punctuation → remove stopwords → stem)
    ↓
TF-IDF Vectorization
    ↓
Naive Bayes Classifier
    ↓
✅ Ham  or  🚨 Spam
```

---

## 📦 Requirements

```
streamlit
nltk
scikit-learn
```

---

## 🙌 Author

**Ammar Ahmed**  
[![GitHub](https://img.shields.io/badge/GitHub-Ammarahmed--git-181717?style=flat&logo=github)](https://github.com/Ammarahmed-git)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">
  Made with ❤️ and Python
</p>
