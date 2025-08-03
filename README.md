
# 🌲 Forest Cover Type Prediction - ML Project

[![Made with Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-orange?style=flat-square&logo=streamlit)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

This machine learning project predicts the forest cover type based on cartographic variables such as elevation, slope, aspect, and distances to hydrology, roadways, and fire points. The model is trained on the **Forest Cover Type dataset from the UCI ML Repository** and deployed via **Streamlit** for real-time predictions.

---

## 📊 Project Objective

To predict one of the seven forest cover types (e.g., Spruce/Fir, Lodgepole Pine, etc.) using numerical cartographic features. This solution helps in forest resource management and ecological planning.

---

## 🚀 Tech Stack

- **Python 3.8+**
- **Pandas, NumPy** – Data manipulation
- **Matplotlib, Seaborn** – Visualization
- **Scikit-learn** – Machine Learning (Random Forest)
- **Pickle** – Model serialization
- **Streamlit** – Interactive Web App
- **Git, GitHub** – Version control and hosting

---

## 📁 Project Structure

```

Forest\_Cover\_Type\_Prediction/
├── main.py                         # Streamlit app for prediction
├── Forest\_Cover\_Type.ipynb        # EDA + Model training notebook
├── Model\_for\_forest\_cover.pkl     # Trained model
├── Forest\_Cover\_Dataset\_after\_EDA.csv
├── Forest\_Cover\_Dataset\_before\_EDA.csv
├── style.css                      # Streamlit custom styles
├── Spruce\_Fir.jpg                 # App background image
├── Forest\_Cover\_Type\_Prediction\_Report.pdf
├── Forest\_Cover\_Type\_Prediction\_PPT.pptx
└── README.md                      # Project documentation

````

---

## 💡 Features

- User inputs parameters like elevation, slope, distances to water/roads/fire points, etc.
- Real-time prediction of forest cover type using a trained Random Forest model.
- Clean UI using Streamlit with image and input styling.
- Notebook includes full EDA, preprocessing, feature engineering, and model evaluation.

---

## 🧠 Model Details

- **Algorithm**: Random Forest Classifier
- **Accuracy**: _Replace with your actual model accuracy, e.g., 94.2%_
- **Evaluation**: Confusion Matrix, Classification Report, Cross-Validation

---

## 📷 App Preview

![Spruce_Fir](Spruce_Fir.jpg)

---

## 🛠️ How to Run Locally

```bash
git clone https://github.com/Pragyavashisht08/Forest_Cover_Type_Prediction_Model.git
cd Forest_Cover_Type_Prediction_Model
pip install -r requirements.txt
streamlit run main.py
````

---

## 📚 Dataset Source

* UCI Machine Learning Repository
  🔗 [Forest Cover Type Dataset](https://archive.ics.uci.edu/ml/datasets/Covertype)

---

## 🧭 GitHub Topics

`machine-learning` • `random-forest` • `streamlit` • `python` • `classification` • `geospatial-data` • `scikit-learn` • `uci-dataset` • `data-science` • `forest-cover-type`

> Add these in your GitHub repo topics for better reach.

---

## 📬 Contact

Created by **Pragya Vashisht**
🔗 GitHub: [@Pragyavashisht08](https://github.com/Pragyavashisht08)


---

## 🏷️ License

This project is open-source under the [MIT License](LICENSE).

---

```

