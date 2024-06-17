


# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from scipy.stats import shapiro, levene
import statsmodels.api as sm
import seaborn as sns
import joblib

# Load data from specified file path
file_path = "C:/Users/HP/Downloads/Crop_recommendation_with_WSI.csv"
data = pd.read_csv(file_path)

# Preprocess data by replacing NA values with the median
for col in data.select_dtypes(include=[np.number]).columns:
    data[col].fillna(data[col].median(), inplace=True)

# Convert categorical variable to factors (equivalent to factor in R)
data['label'] = data['label'].astype('category')

# Train a decision tree model to predict crop type based on environmental conditions
dt_model = DecisionTreeClassifier()
X = data.drop(['label', 'WSI'], axis=1)  # Features excluding the target variable and WSI
y = data['label']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the model
dt_model.fit(X_train, y_train)

# Evaluate the model
y_pred = dt_model.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save the trained model
joblib.dump(dt_model, 'best_model.pkl')

# Load the model for prediction (in case of a new session)
best_model = joblib.load('best_model.pkl')


# Function to take user input for prediction
def get_user_input():
    N = float(input("Enter Nitrogen (N) level: "))
    P = float(input("Enter Phosphorus (P) level: "))
    K = float(input("Enter Potassium (K) level: "))
    temperature = float(input("Enter Temperature: "))
    humidity = float(input("Enter Humidity: "))
    ph = float(input("Enter pH level: "))
    rainfall = float(input("Enter Rainfall: "))

    # Create a DataFrame for the user input
    user_input_df = pd.DataFrame(
        [[N, P, K, temperature, humidity, ph, rainfall]],
        columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
    )
    return user_input_df


# Get user input
user_input_df = get_user_input()

# Make prediction based on user input
prediction = best_model.predict(user_input_df)
print(f"The predicted crop is: {prediction[0]}")
