
------------------------------
## Technical Documentation: # Laptop Price Predictor: Mathematical Foundations
Objective: To build a machine learning pipeline that predicts laptop prices with high accuracy using hardware specifications.
------------------------------
## 1. Data Engineering & Preprocessing (Day 1-3)
Before modeling, the raw data required significant "Feature Extraction" to make it machine-readable.

* Feature Extraction: Derived new columns (CPu_Type,Touchscreen, IPS, ppi) from messy strings in ScreenResolution.
* Memory Parsing: Split the Memory column into four distinct numerical features: SSD, HDD, Flash, and Hybrid.
* Skewness Correction: Applied Log Transformation ($y = \log(x)$) to the Price column.
* Significance: This handled the right-skewed distribution caused by premium laptops, ensuring the model treats percentage-based price increases linearly.

------------------------------
## 2. Statistical Foundations (Day 4-5)
Algorithm: Multiple Linear Regression
Math Logic: $Y = b_0 + b_1X_1 + b_2X_2 + \dots + \epsilon$

* Ordinary Least Squares (OLS): Used to minimize the sum of squared residuals to find the line of best fit.
* One-Hot Encoding: Categorical variables (Brand, Type) were converted into binary "Dummy Variables" ($0$ or $1$) so the algebraic formula could process text.
* Evaluation Metrics:
* R2 Score (0.85): Indicated that 85% of price variance was explained by the features.
   * MAE: Determined the average "real-world" error in Euros.

------------------------------
## 3. Model Optimization: Random Forest (Day 6)
To improve accuracy, we moved from a linear model to an Ensemble Learning approach.

* Logic: A "Forest" of 100 Decision Trees. Each tree "votes" on the price, and the average is taken to reduce Variance and prevent Overfitting.
* Key Hyperparameters:
* n_estimators=100: The number of voters.
   * max_samples=0.5: Diversity; each tree only sees 50% of the data.
   * max_depth=15: Complexity control to stop trees from "memorizing" the training set.
* Result: Accuracy increased from 85% to 89%.

------------------------------
## 4. Deployment & Troubleshooting (Day 7)
The model was deployed using Streamlit. During this phase, two critical production errors were solved:
## A. The Shape Mismatch (Feature Alignment)

* Problem: The model expected 15 columns (from the training pipeline) but the web app was only passing 12.
* Solution: Ensured the input dictionary in app.py contained every single feature used during training, in the exact same order.

## B. Numpy vs. DataFrame Error

* Problem: Passing a raw Numpy array caused a ValueError because the ColumnTransformer was looking for specific "Column Names."
* Solution: Reframed the user input into a Pandas DataFrame using dictionary mapping:

query = pd.DataFrame([{'Company': company, 'TypeName': type, ...}])


------------------------------
## 5. Summary of Results

| Metric | Baseline (Linear) | Optimized (Random Forest) |
|---|---|---|
| R2 Score | 0.85 | 0.89 |
| Mean Absolute Error | ~€197 | ~€163 |

------------------------------
## 6. Tech Stack

* Languages: Python (Pandas, Numpy, Scikit-Learn)
* Visualization: Matplotlib, Seaborn
* Deployment: Streamlit
* Model Persistence: Pickle (.pkl)


