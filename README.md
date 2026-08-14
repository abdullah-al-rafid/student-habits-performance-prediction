# 📊 Student Habits & Academic Performance Prediction

A machine learning project that analyzes student lifestyle and academic behavior data to predict exam scores.

The project includes data preprocessing, exploratory analysis, feature selection, regression model comparison, model evaluation, and a Streamlit-based prediction application.

---

## 🎯 Project Overview

Student academic performance can be influenced by different behavioral and lifestyle factors such as study time, attendance, sleep, social media usage, mental health, and part-time work.

This project uses machine learning regression techniques to learn relationships between selected student habits and exam performance, then provides a simple web interface for predicting an exam score from user-provided inputs.

---

## ✨ Key Features

- 📂 Student performance dataset analysis
- 🧹 Missing-value handling
- 🔎 Duplicate-value checking
- 🔢 Categorical feature encoding
- 📊 Exploratory data analysis
- 🎯 Correlation-based feature analysis
- 🤖 Multiple regression models
- 🔧 5-fold GridSearchCV
- 📈 RMSE and R² evaluation
- 💾 Trained model saved with Joblib
- 🌐 Streamlit prediction application

---

## 📁 Dataset

The project uses:

`student_habits_performance.csv`

The original dataset contains:

- **1,000 rows**
- **16 columns**

The target variable is:

`exam_score`

The dataset contains student-related attributes including study habits, attendance, sleep, social media usage, part-time work, mental health, and other academic/lifestyle factors.

During preprocessing, `parental_education_level` contained **91 missing values**. The notebook removes rows containing missing values, resulting in **909 records** for the modeling stage. No duplicate rows were found during the duplicate check.

---

## 🧹 Data Preprocessing

The notebook performs the following preprocessing steps:

1. Loads the dataset using Pandas
2. Inspects dataset structure and dimensions
3. Checks missing values
4. Removes rows containing missing values
5. Checks for duplicate records
6. Encodes categorical variables using `LabelEncoder`
7. Removes `age` and `student_id`
8. Examines feature relationships with the target variable
9. Selects the final modeling features

---

## 🎯 Selected Features

The final model uses six input features:

| Feature | Description |
|---|---|
| `study_hours_per_day` | Daily study time |
| `attendance_percentage` | Student attendance percentage |
| `mental_health_rating` | Mental health rating |
| `sleep_hours` | Daily sleep duration |
| `part_time_job` | Whether the student has a part-time job |
| `social_media_hours` | Daily social media usage |

Target variable:

`exam_score`

The final feature list is explicitly defined in the notebook before model training. 

---

## 🤖 Machine Learning Models

Three regression approaches were evaluated:

### 1. Linear Regression

A baseline linear regression model was trained to estimate exam scores from the selected features.

### 2. Decision Tree Regressor

A decision-tree-based regression model was evaluated with hyperparameter tuning.

### 3. Random Forest Regressor

A Random Forest regression model was evaluated using different combinations of:

- `n_estimators`
- `max_depth`

---

## 🔧 Model Selection & Hyperparameter Tuning

The project uses:

**GridSearchCV with 5-fold cross-validation**

The models were evaluated using:

- RMSE — Root Mean Squared Error
- R² — Coefficient of Determination

The dataset was divided using an **80/20 train-test split** with `random_state=45`.

After preprocessing:

- Training samples: **727**
- Testing samples: **182**

---

## 📈 Model Performance

| Model | RMSE | R² |
|---|---:|---:|
| 🥇 Linear Regression | **6.118** | **0.855** |
| Random Forest | 7.223 | 0.798 |
| Decision Tree | 9.279 | 0.667 |

Based on the notebook's evaluation, **Linear Regression achieved the lowest RMSE and highest R² among the evaluated models**.

The selected Linear Regression model was saved as:

`best_model.pkl`

---

## 🌐 Streamlit Application

The project includes a Streamlit application that loads the trained model and allows users to enter:

- Study hours per day
- Attendance percentage
- Mental health rating
- Sleep hours per night
- Social media hours
- Part-time job status

The application then returns a predicted exam score.

### Application File

`app.py`

### Trained Model

`best_model.pkl`

---

## 🚀 Run the Application Locally

### 1. Clone the Repository

`git clone https://github.com/abdullah-al-rafid/student-habits-performance-prediction.git`

`cd student-habits-performance-prediction`

### 2. Install Dependencies

`pip install pandas numpy scikit-learn matplotlib seaborn streamlit joblib`

### 3. Run the Streamlit App

`streamlit run app.py`

The application will open in your browser.

---

## 📂 Project Structure

- `app.py` — Streamlit prediction application
- `best_model.pkl` — Trained Linear Regression model
- `codes.ipynb` — Data analysis, preprocessing, feature selection, model training and evaluation
- `student_habits_performance.csv` — Dataset
- `README.md` — Project documentation

---

## 🧠 Machine Learning Workflow

**Dataset**

↓

**Data Inspection**

↓

**Missing Value Handling**

↓

**Duplicate Check**

↓

**Categorical Encoding**

↓

**Feature Selection**

↓

**Train-Test Split**

↓

**Model Training**

↓

**5-Fold GridSearchCV**

↓

**RMSE & R² Evaluation**

↓

**Best Model Selection**

↓

**Model Serialization**

↓

**Streamlit Prediction App**

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit
- Jupyter Notebook

---

## 📌 Project Limitations

- The model is trained on the available dataset and its performance may not generalize to other student populations.
- The prediction should be treated as a machine learning estimate rather than a guaranteed exam result.
- The current application uses the six selected features used during model training.
- Categorical variables were encoded using `LabelEncoder` during the notebook workflow.

---

## 🔮 Future Improvements

- [ ] Add a dedicated `requirements.txt`
- [ ] Deploy the Streamlit application
- [ ] Add interactive data visualizations
- [ ] Improve categorical feature encoding
- [ ] Compare additional regression algorithms
- [ ] Add cross-validation performance visualization
- [ ] Add prediction confidence or uncertainty information
- [ ] Improve the Streamlit UI
- [ ] Add automated model retraining workflow

---

## 👨‍💻 Author

**Abdullah Al Rafid**

Computer Science & Engineering Student  
Daffodil International University

GitHub: [@abdullah-al-rafid](https://github.com/abdullah-al-rafid)

LinkedIn: [Abdullah Al Rafid](https://www.linkedin.com/in/abdullah-al-rafid)
