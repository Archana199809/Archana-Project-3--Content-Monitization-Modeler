# Archana-Project-3--Content-Monetization-Modeler
Youtube Revenue Prediction

📺 Content Monetization Modeler
---
An end-to-end machine learning project that analyzes and predicts YouTube Ad Revenue using engagement metrics (views, likes, comments, etc.).
This project combines data preprocessing, feature engineering, machine learning models, and an interactive Streamlit dashboard to help creators and analysts make data-driven content decisions.


🧩 Business Use Cases
---

**Content Strategy Optimization:** Helps creators determine what type of content yields the highest returns.

**Revenue Forecasting:** Media companies can predict expected income from future video uploads.

**Creator Support Tools:** Can be integrated into platforms offering analytics services to YouTubers.

**Ad Campaign Planning:** Enables advertisers to forecast ROI based on content performance metrics


## 🛠️ Tech Stack

Languages & Libraries: Python, Pandas, NumPy, Scikit-learn

Visualization: Seaborn, Matplotlib, Streamlit

Deployment: Streamlit (dark theme)

Model Persistence: Joblib

**🚀 Project Pipeline**

## 1️⃣ Data Collection & Preparation

Gathered dataset containing YouTube video performance metrics (views, likes, comments, shares, category, device,country,watch_time_minutes....).

Raw Dataset Size: 122,000+ rows (1 lakh+).

Cleaned Dataset: 120,000 rows after removing duplicates ~2%, missing values ~5%, and outliers.

Applied OnehotEncoding for categorical variables (Category, Device,Country).

Applied scaling for numerical features to improve ML model performance.


## 2️⃣ Exploratory Data Analysis (EDA)

📊 Generated correlation heatmaps to explore relationships between engagement metrics and revenue.

📈 Visualized Features Columns to Understand the pattern.

🧹 Identified and highlighted missing values before data cleaning for transparency.



## 3️⃣ Feature Engineering

Selected key features impacting Ad Revenue: Views, Likes, Comments, Shares, Category, Device,..

Applied **OneHotEncoder** for categorical variables.

Used **StandardScaler** to normalize input features for regression models.


## 4️⃣ Machine Learning Models

Implemented and compared multiple ML algorithms:

🔹 Linear Regression

🔹 DecisionTreeRegressor

🔹 RandomForestRegressor

🔹 SVR

🔹 KNeighborsRegressor

✔️ Models evaluated using R² Score, Mean Absolute Error (MAE), Mean Squared Error (MSE),Root Mean Squared Error(RMSE).

✔️  **Linear Regression** achieved the best performance for predicting YouTube ad revenue.

✔️ Final trained model saved with Joblib for deployment.

Best model: Linear Regression

Performance:

R² ≈ 0.9526

RMSE ≈ 13.480

MAE ≈ 3.111

## 5️⃣ Model Deployment with Streamlit

Predicts Ad Revenue in USD instantly
Simple, interactive UI with metrics display

✅ Streamlit App for real-time interaction.

<img width="1920" height="1080" alt="p1" src="https://github.com/user-attachments/assets/39fbc1d6-b558-437c-ba95-bec2602ae3cd" />
<img width="1920" height="1080" alt="p2" src="https://github.com/user-attachments/assets/acd94329-7178-4473-93f6-4d5297599ee0" />
<img width="1920" height="1080" alt="p3" src="https://github.com/user-attachments/assets/89e111ad-6dea-4bad-9641-8723e3c4b951" />

✅ Saved Models & Preprocessors (.pkl files using Joblib).

✅ Professional Documentation README .


🔍 Insights from the Project
--
📈 **Watch_time_minutes** are the** Highest correlected** to revenue → Higher views consistently drive higher monetization.

📊 Category & Device significantly affect ad revenue → Certain categories and devices **(e.g., Mobile-first) yield better ad performance.**

🧹 Data quality improvements **(handling missing values, scaling, encoding)** boosted model accuracy.

🖥️ The Streamlit dashboard makes insights accessible to non-technical users, bridging the gap between creators and data science.

---

⚡ This project bridges the gap between data science and content strategy, giving creators a powerful tool to predict and optimize YouTube revenue.

---

