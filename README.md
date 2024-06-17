# AI-Powered-Crop-Prediction-and-Suggestions
Welcome to the Crop Prediction and Suggestions System! This project aims to predict the best crop to plant based on various environmental factors and provide suggestions to optimize crop yield. This system also includes a unique feature called the Weather Stress Index (WSI) to help farmers better understand and manage weather-related stress on crops.

Table of Contents
Introduction
Features
Dataset
Models Used
Weather Stress Index (WSI)
Installation
Usage
Results
Contributing
License
Introduction
Agriculture is a critical sector that requires innovative solutions to improve crop yield and ensure food security. This project leverages machine learning to predict the most suitable crop for planting based on soil and weather conditions. Additionally, it offers valuable suggestions for crop management and fertilizer usage.

Features
Predicts the best crop to plant based on environmental factors.
Provides suggestions in English, Hindi, and Hinglish.
Unique Weather Stress Index (WSI) feature.
Recommendations for fertilizers based on nutrient deficiencies.
User-friendly web interface for input and result display.
Dataset
The dataset used in this project includes the following features:

Nitrogen (N) level
Phosphorus (P) level
Potassium (K) level
Temperature
Humidity
pH level
Rainfall
Crop Label (target variable)
Weather Stress Index (WSI)
Models Used
The following machine learning models have been implemented and evaluated:

Decision Tree Classifier
Random Forest Classifier
Support Vector Machine (SVM)
K-Nearest Neighbors (KNN) Classifier
Each model was trained and tested to determine the most accurate predictor for crop recommendation.

Weather Stress Index (WSI)
The Weather Stress Index (WSI) is a unique feature that quantifies the stress level on crops due to weather conditions. This index helps farmers understand the potential impact of weather on crop health and make informed decisions to mitigate risks.

Installation
To run this project locally, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/crop-prediction.git
cd crop-prediction
Create and activate a virtual environment:

bash
Copy code
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Run the web application:

bash
Copy code
flask run
Usage
Open the web application in your browser.
Enter the required environmental parameters (N, P, K levels, temperature, humidity, pH, and rainfall).
Click the "Predict" button to get the recommended crop.
View the prediction results, Weather Stress Index, and suggestions in the results section.
Results
The system displays the predicted crop, Weather Stress Index (WSI), and suggestions for crop management. It also provides links to recommended fertilizers based on soil nutrient deficiencies.

Contributing
We welcome contributions from the community! If you would like to contribute, please follow these guidelines:

Fork the repository.
Create a new branch: git checkout -b feature-branch.
Make your changes.
Commit your changes: git commit -m 'Add new feature'.
Push to the branch: git push origin feature-branch.
Submit a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.
