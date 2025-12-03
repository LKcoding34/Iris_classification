
# 🌸 Iris Flower Classifier  

An interactive **Streamlit web app** that predicts the species of an iris flower (*Setosa, Versicolor, Virginica*) based on user‑provided measurements. The app uses a **Random Forest Classifier** trained on the classic **Iris dataset** and displays species images and typical measurement ranges for better accessibility.  

---

## 🚀 Features  
- **Machine Learning Model**: Random Forest Classifier trained on the Iris dataset  
- **Interactive UI**: User inputs via sliders for sepal and petal measurements  
- **Real‑time Prediction**: Species predicted instantly upon form submission  
- **Visuals & Insights**: Displays flower image and typical measurement ranges for the predicted species  
- **Caching**: Efficient use of `@st.cache_data` and `@st.cache_resource` for dataset and model reuse  

---

## 🛠️ Technologies Used  
- **Python**  
- **Streamlit** – for interactive web app UI  
- **scikit‑learn** – for ML model training and prediction   

---

## 📊 Methods  
- **Dataset**: Iris dataset from `sklearn.datasets`  
- **Train/Test Split**: 80/20 split using `train_test_split`  
- **Model**: RandomForestClassifier (default parameters)   

---

## ▶️ How to Run  

1. Clone the repository:  
   ```bash
   git clone https://github.com/LKcoding34/Iris_classification.git
   cd Iris_classification
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

   *(requirements.txt should include: `streamlit`, `scikit-learn`)*  

3. Run the Streamlit app:  
   ```bash
   streamlit run app.py
   ```

4. Open the local URL shown in the terminal (default: `http://localhost:8501`)  

---

## 📷 Demo  

- Input sepal and petal measurements using sliders  
- Click **Predict** to classify the flower  
- View:  
  - 🌼 Predicted species name  
  - 📸 Image of the flower  
  - 📏 Typical measurement ranges  

---

## 💡 Future Improvements  
- Add multiple ML models for comparison (SVM, KNN, Logistic Regression)  
- Display accuracy metrics and confusion matrix in the UI  
- Deploy on Streamlit Cloud for easy sharing  

---

## 👩‍💻 Author  
Developed by **Lakshmi Kalyani Naraga**  
- 🎓 B.Tech in Computer Science & Engineering (AI Specialization)  
- 🌟 Passionate about ML apps with neat UI & accessibility  
- 🔗 [LinkedIn](https://www.linkedin.com/in/lakshmi-kalyani25/) | [GitHub](https://github.com/LKcoding34)  

---

✨ *This project demonstrates end‑to‑end ML workflow — from dataset exploration to model deployment — with a focus on clarity, neat visuals, and professional polish.*  

---

