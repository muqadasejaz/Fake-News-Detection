# 📰 Fake News Detection 

This project aims to detect and classify news articles as Fake or Real using Natural Language Processing (NLP) and machine learning techniques. With the increasing spread of misinformation online, especially through social media, automated detection systems have become crucial.

Detect whether a news article is **real** or **fake** using a machine learning pipeline based on **TF-IDF vectorization** and a **Gradient Boosting Classifier**. The model achieves an impressive **99% accuracy**.

<img width="1324" height="765" alt="Fake News Detection" src="https://github.com/user-attachments/assets/a6558d26-c560-4f94-a910-79b7f790a3ce" />

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## 🌐 Live Demo

Click here to try the live app 👉 [Fake News Detection App](https://fake-newsdetectionsystem.streamlit.app/)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## 📌 Overview

Fake news has become a major concern in today's digital world. This project leverages **Natural Language Processing (NLP)** techniques like **TF-IDF vectorization** and a supervised learning model (**Gradient Boosting**) to classify news articles as either **FAKE** or **REAL**. 

A clean **Streamlit interface** makes the model easy to use for live news predictions.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🚀 Features

- 🧠 Machine Learning model with 99% accuracy
  
- 📄 TF-IDF vectorizer for transforming raw news text
   
- 📊 Confusion matrix and classification report
  
- 📝 Real-time prediction of custom news input
  
- ✅ Interactive and minimal GUI with Streamlit
   
- 🗂 Easy-to-read modular code  

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🛠 Tools and Technologies

- Python  
- Scikit-learn  
- Pandas  
- NumPy  
- Matplotlib / Seaborn  
- TF-IDF Vectorizer
- Gradient Boosting Classifier  
- Streamlit  
- Joblib  

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🧠 How It Works

1. **Data Preprocessing**  
   - Remove missing values, symbols, and stop words  
   - Convert text to lowercase  

2. **Feature Extraction with TF-IDF**  
   - Converts the news text into numerical features using the **Term Frequency-Inverse Document Frequency (TF-IDF)** technique.  

3. **Model Training**  
   - A **Gradient Boosting Classifier** is trained on the TF-IDF features.  
   - Trained pipeline is saved using `joblib`.  

4. **Deployment**  
   - The saved pipeline (TF-IDF + model) is used in a **Streamlit app** for real-time predictions.  

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📂 Dataset

- **Source:** [Fake and Real News Dataset – Kaggle](https://www.kaggle.com/datasets/jainpooja/fake-news-detection)  
- **Features Used:** `title`, `text`, `subject` , `date`
- **Label Encoding:**  
  - `1` → Real News  
  - `0` → Fake News  

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📈 Results

### ✅ Model Performance:
- **Algorithm:** Gradient Boosting Classifier  
- **Accuracy:** `99%` on test data  

### 📊 Evaluation Metrics:
- **Confusion Matrix:**

  <img width="518" height="393" alt="image" src="https://github.com/user-attachments/assets/a4158cbd-349a-44b6-a289-18ca42f9ed30" />

- **Classification Report:**
  
  <img width="893" height="278" alt="CR" src="https://github.com/user-attachments/assets/1ae8dd33-c5b1-4c67-a4ad-0361d13a5756" />

- **Prediction on new news:**

- Fake News:

<img width="806" height="319" alt="fake_news" src="https://github.com/user-attachments/assets/c3deed4d-c874-4e25-b833-fe51835c929b" />

- Not a Fake News:

<img width="802" height="433" alt="not_fake" src="https://github.com/user-attachments/assets/c8b70779-6143-4dcd-8a30-7ce841355611" />


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📚 References

-  [Fake and Real News Dataset – Kaggle](https://www.kaggle.com/datasets/jainpooja/fake-news-detection)  

- https://www.edps.europa.eu/press-publications/publications/techsonar/fake-news-detection_en

- https://founderz.com/blog/detecting-fake-news-with-ai/

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 👤 Author

Muqadas Ejaz

BS Computer Science (AI Specialization)

AI/ML Engineer

Data Science & Gen AI Enthusiast

📫 Connect with me on [LinkedIn](https://www.linkedin.com/in/muqadasejaz/)  

🌐 GitHub: [github.com/muqadasejaz](https://github.com/muqadasejaz)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📎 License

This project is open-source and available under the [MIT License](LICENSE).
