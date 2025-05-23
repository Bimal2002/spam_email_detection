# 📧 Spam Email Detection using Machine Learning

This project is a Machine Learning-based web application to detect whether a given email is **spam** or **not spam**. It uses Natural Language Processing (NLP) techniques and classification algorithms like **Random Forest**, trained on a labeled dataset of spam/ham emails. A custom frontend was developed to allow users to test the model with their own text.

---

## 🔍 Features

- Train and evaluate multiple models (Naive Bayes, Logistic Regression, SVM, Random Forest)
- Text preprocessing using TF-IDF vectorization
- Spam/ham prediction via a deployed web interface
- Frontend built with HTML, CSS, JavaScript
- Flask backend for inference
- Deployed live using Render

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (Python)
- **ML Models:** Scikit-learn (Random Forest, Logistic Regression, Naive Bayes, SVC)
- **NLP:** TF-IDF Vectorization
- **Deployment:** Render

---

## 🚀 Live Demo

🔗 Web App: [Spam Email Detector](https://spam-email-detection-1-rjjl.onrender.com/)

---


---

## 📊 Model Performance

Among all tested classifiers, **Random Forest** delivered the best performance with the highest accuracy and lowest false positive rate.

| Model               | Accuracy |
|--------------------|----------|
| Naive Bayes        | 0.95     |
| Logistic Regression| 0.97     |
| SVC                | 0.97     |
| **Random Forest**  | **0.98** |

---

## ✨ How It Works

1. User enters email text in the web app.
2. The frontend sends the input to the Flask backend (`/predict` route).
3. Text is vectorized using the saved TF-IDF vectorizer.
4. The model predicts whether it's spam or not.
5. The result is displayed to the user.

---

## 🧪 Example Inputs

### Spam
  Subject: 🎉 Congratulations! You’ve Won a Free iPhone!  

Dear User,  

You have been selected as the lucky winner of a brand-new iPhone 15 Pro! 🎁 To claim your prize, simply click the link below and enter your details:  

👉 [Claim Your Prize Now](http://scam-link.com)  

Hurry! This offer expires in 24 hours.  

Best Regards,  
The Rewards Team  

### NOT spam
Not Spam (Legitimate Email) Example: 
Subject: Meeting Reminder – Project Discussion at 3 PM  

Hi Team,  

Just a reminder that we have a project discussion meeting scheduled for today at 3 PM. Here’s the agenda:  

1. Progress updates  
2. Upcoming deadlines  
3. Team feedback  

Please join via the meeting link: [Zoom Meeting](http://company-meeting.com)  

Best,  
John Doe  
Project Manager  





---

## 💻 Run Locally

```bash
git clone https://github.com/Bimal2002/spam_email_detection.git
cd spam_email_detection
pip install -r requirements.txt
python app.py


