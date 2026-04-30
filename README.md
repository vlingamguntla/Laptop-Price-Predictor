
------------------------------
## 💻 Laptop Price Predictor

An End-to-End Machine Learning Web Application


## 🎯 Project Overview
This project predicts the market price of a laptop based on its hardware specifications (RAM, CPU, GPU, Storage, etc.). It uses a Random Forest Regressor to achieve high accuracy and is deployed as an interactive web app.

* Final Model Accuracy: 89.16% ($R^2$ Score)
* Mean Absolute Error (MAE): ~€163

------------------------------
## 🛠️ The Tech Stack

* Data Analysis: Pandas, NumPy
* Visualization: Matplotlib, Seaborn
* Machine Learning: Scikit-Learn (Pipeline, ColumnTransformer, RandomForestRegressor)
* Deployment: Streamlit
* Version Control: Git & GitHub

------------------------------
## 🧠 Key Features & Logic

* PPI Calculation: Engineered a custom Pixels Per Inch (PPI) feature using the Pythagorean theorem to capture screen quality more effectively than raw resolution.
* Log Transformation: Applied logarithmic scaling to the target variable (Price) to handle right-skewed data and improve model stability.
* Feature Engineering:
   * Simplified 100+ CPU/GPU models into 5 core performance tiers.
   * Extracted hidden binary flags for IPS Panels and Touchscreens.
   * Parsed complex "Memory" strings into dedicated SSD and HDD columns.
* Robust Pipeline: Built a custom Scikit-Learn pipeline that handles both One-Hot Encoding and Random Forest logic, ensuring the app never crashes on unknown inputs.

------------------------------
## 🚀 How to Run Locally

   1. Clone the repository:
   
   git clone https://github.com
   cd laptop-price-predictor
   
   2. Install dependencies:
   
   pip install -r requirements.txt
   
   3. Run the app:
   
   streamlit run app.py
   
   
------------------------------
## 📁 Project Structure

```text
├── Analysis.ipynb       # Full EDA, Feature Engineering, and Model Training
├── app.py               # Streamlit UI and prediction logic
├── MATH_FOUNDATIONS.md  # Deep dive into the math/logic used
├── STUDY_LOG.md         # Detailed day-by-day learning journey
├── pipe.pkl             # Trained ML Pipeline (The Brain)
├── df.pkl               # Cleaned data for the UI dropdowns
└── requirements.txt     # List of required Python libraries
```
------------------------------
## 🔗 Dataset
The data used in this project was sourced from [Kaggle: Laptop Price Dataset](https://www.kaggle.com/datasets/ironwolf437/laptop-price-dataset).
------------------------------
## 🤝 Contact
Name : Vignyatha Lingamguntla
Email: vignyatha.lingamguntla@gmail.com

