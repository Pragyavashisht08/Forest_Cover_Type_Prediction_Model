
# 🌲 Forest Cover Type Prediction - ML Project

This machine learning project predicts the forest cover type based on cartographic variables such as elevation, slope, aspect, and distances to hydrology, roadways, and fire points. The model is trained on the **Forest Cover Type dataset from the UCI ML Repository** and is deployed using **Streamlit** for user-friendly interaction.

---

## 📊 Project Objective

To predict one of the seven forest cover types (e.g., Spruce/Fir, Lodgepole Pine, etc.) using numerical cartographic features. This solution can aid forest management authorities in efficient classification and conservation planning.

---

## 🚀 Tech Stack

- **Python 3**
- **Pandas, NumPy** – Data manipulation
- **Matplotlib, Seaborn** – Visualization
- **Scikit-learn** – Machine Learning (Random Forest Classifier)
- **Pickle** – Model serialization
- **Streamlit** – Interactive web app
- **Git & GitHub** – Version control and hosting

---

## 📁 Project Structure

```

Forest\_Cover\_Type\_Prediction/
├── main.py                         # Streamlit app for prediction
├── Forest\_Cover\_Type.ipynb        # EDA + Model training
├── Model\_for\_forest\_cover.pkl     # Trained model file
├── Forest\_Cover\_Dataset\_after\_EDA.csv
├── Forest\_Cover\_Dataset\_before\_EDA.csv
├── style.css                      # Streamlit custom styles
├── Spruce\_Fir.jpg                 # Image used in app
├── Forest\_Cover\_Type\_Prediction\_Report.pdf
├── Forest\_Cover\_Type\_Prediction\_PPT.pptx
└── README.md                      # Project documentation

````

---

## 💡 Features

- Collects user inputs for various forest geography parameters.
- Performs real-time prediction of forest cover type using the trained model.
- Simple and intuitive UI using Streamlit.
- Visualizations and analysis included in the notebook.
- Data preprocessing and transformation steps clearly documented.

---

## 🧠 Model Details

- **Algorithm**: Random Forest Classifier
- **Accuracy**: _add your actual model accuracy here, e.g., 94.2%_
- **Evaluation**: Confusion Matrix, Classification Report, Cross-Validation

---

## 🛠️ How to Run Locally

Clone the repo and run it using Streamlit:

```bash
git clone https://github.com/Pragyavashisht08/Forest_Cover_Type_Prediction_Model.git
cd Forest_Cover_Type_Prediction_Model
pip install -r requirements.txt
streamlit run main.py
````

---

## 📚 Dataset Source

Dataset: [UCI Machine Learning Repository – Forest Cover Type](https://archive.ics.uci.edu/ml/datasets/Covertype)

---

## 📷 App Preview

![Spruce\_Fir](Spruce_Fir.jpg)

---

## 📬 Contact

Created by **Pragya Vashisht**
📫 GitHub: [@Pragyavashisht08](https://github.com/Pragyavashisht08)

---

## 🏷️ Tags

`Machine Learning` `Random Forest` `Streamlit` `Supervised Learning` `Geospatial Data` `Classification` `Forest Cover Type` `UCI Dataset`

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

````

---


```bash
pip freeze > requirements.txt
````


