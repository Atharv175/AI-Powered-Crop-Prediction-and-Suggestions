from flask import Flask, render_template, request
import pandas as pd
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
best_model = joblib.load('best_model.pkl')

# Define normalization function
def normalize(value, min_value, max_value):
    return (value - min_value) / (max_value - min_value)

# Define function to calculate WSI
def calculate_wsi(N, P, K, temperature, humidity, ph, rainfall):
    # Define min and max values for normalization (these should be based on your data)
    min_values = {'N': 0, 'P': 0, 'K': 0, 'temperature': 0, 'humidity': 0, 'ph': 0, 'rainfall': 0}
    max_values = {'N': 100, 'P': 100, 'K': 100, 'temperature': 50, 'humidity': 100, 'ph': 14, 'rainfall': 300}

    # Normalize values
    norm_N = normalize(N, min_values['N'], max_values['N'])
    norm_P = normalize(P, min_values['P'], max_values['P'])
    norm_K = normalize(K, min_values['K'], max_values['K'])
    norm_temperature = normalize(temperature, min_values['temperature'], max_values['temperature'])
    norm_humidity = normalize(humidity, min_values['humidity'], max_values['humidity'])
    norm_ph = normalize(ph, min_values['ph'], max_values['ph'])
    norm_rainfall = normalize(rainfall, min_values['rainfall'], max_values['rainfall'])

    # Assign weights to each parameter
    weights = {'N': 0.1, 'P': 0.1, 'K': 0.1, 'temperature': 0.2, 'humidity': 0.2, 'ph': 0.1, 'rainfall': 0.2}

    # Calculate WSI
    wsi = (weights['N'] * norm_N +
           weights['P'] * norm_P +
           weights['K'] * norm_K +
           weights['temperature'] * norm_temperature +
           weights['humidity'] * norm_humidity +
           weights['ph'] * norm_ph +
           weights['rainfall'] * norm_rainfall)

    return wsi

# Define function to generate detailed suggestions in English, Hindi, and Hinglish
def generate_suggestions(N, P, K, temperature, humidity, ph, rainfall, wsi):
    suggestions = []
    hindi_suggestions = []
    hinglish_suggestions = []

    # Suggestions based on individual parameters
    if N < 20:
        suggestions.append("Nitrogen levels are low. Consider using nitrogen-based fertilizers.")
        hindi_suggestions.append("नाइट्रोजन का स्तर कम है। नाइट्रोजन-आधारित उर्वरकों का उपयोग करने पर विचार करें।")
        hinglish_suggestions.append("Nitrogen ka star kam hai. Nitrogen-based fertilizers ka use karen.")
    elif N > 80:
        suggestions.append("Nitrogen levels are high. Avoid additional nitrogen-based fertilizers.")
        hindi_suggestions.append("नाइट्रोजन का स्तर अधिक है। अतिरिक्त नाइट्रोजन-आधारित उर्वरकों से बचें।")
        hinglish_suggestions.append("Nitrogen ka star zyada hai. Extra nitrogen-based fertilizers se bachen.")

    if P < 20:
        suggestions.append("Phosphorus levels are low. Consider using phosphorus-based fertilizers.")
        hindi_suggestions.append("फास्फोरस का स्तर कम है। फास्फोरस-आधारित उर्वरकों का उपयोग करने पर विचार करें।")
        hinglish_suggestions.append("Phosphorus ka star kam hai. Phosphorus-based fertilizers ka use karen.")
    elif P > 80:
        suggestions.append("Phosphorus levels are high. Avoid additional phosphorus-based fertilizers.")
        hindi_suggestions.append("फास्फोरस का स्तर अधिक है। अतिरिक्त फास्फोरस-आधारित उर्वरकों से बचें।")
        hinglish_suggestions.append("Phosphorus ka star zyada hai. Extra phosphorus-based fertilizers se bachen.")

    if K < 20:
        suggestions.append("Potassium levels are low. Consider using potassium-based fertilizers.")
        hindi_suggestions.append("पोटेशियम का स्तर कम है। पोटेशियम-आधारित उर्वरकों का उपयोग करने पर विचार करें।")
        hinglish_suggestions.append("Potassium ka star kam hai. Potassium-based fertilizers ka use karen.")
    elif K > 80:
        suggestions.append("Potassium levels are high. Avoid additional potassium-based fertilizers.")
        hindi_suggestions.append("पोटेशियम का स्तर अधिक है। अतिरिक्त पोटेशियम-आधारित उर्वरकों से बचें।")
        hinglish_suggestions.append("Potassium ka star zyada hai. Extra potassium-based fertilizers se bachen.")

    if temperature < 10:
        suggestions.append("Temperature is low. Consider using protective measures to maintain warmth.")
        hindi_suggestions.append("तापमान कम है। गर्मी बनाए रखने के लिए सुरक्षात्मक उपायों का उपयोग करने पर विचार करें।")
        hinglish_suggestions.append("Temperature kam hai. Garmi banaye rakhne ke liye protective measures ka use karen.")
    elif temperature > 35:
        suggestions.append("Temperature is high. Ensure adequate watering and consider shading.")
        hindi_suggestions.append("तापमान अधिक है। पर्याप्त पानी दें और छायांकन पर विचार करें।")
        hinglish_suggestions.append("Temperature zyada hai. Pani den aur shading ka vichar karen.")

    if humidity < 30:
        suggestions.append("Humidity is low. Ensure adequate irrigation to maintain soil moisture.")
        hindi_suggestions.append("आर्द्रता कम है। मिट्टी की नमी बनाए रखने के लिए पर्याप्त सिंचाई सुनिश्चित करें।")
        hinglish_suggestions.append("Humidity kam hai. Mitti ki nami banaye rakhne ke liye irrigation ka use karen.")
    elif humidity > 80:
        suggestions.append("Humidity is high. Ensure proper drainage to avoid waterlogging.")
        hindi_suggestions.append("आर्द्रता अधिक है। जलभराव से बचने के लिए उचित जल निकासी सुनिश्चित करें।")
        hinglish_suggestions.append("Humidity zyada hai. Jalbharav se bachne ke liye proper drainage ka use karen.")

    if ph < 5.5:
        suggestions.append("Soil pH is low (acidic). Consider using lime to raise the pH.")
        hindi_suggestions.append("मिट्टी का पीएच कम है (अम्लीय)। पीएच बढ़ाने के लिए चूना का उपयोग करने पर विचार करें।")
        hinglish_suggestions.append("Mitti ka pH kam hai (amli). pH badhane ke liye lime ka use karen.")
    elif ph > 7.5:
        suggestions.append("Soil pH is high (alkaline). Consider using sulfur to lower the pH.")
        hindi_suggestions.append("मिट्टी का पीएच अधिक है (क्षारीय)। पीएच को कम करने के लिए सल्फर का उपयोग करने पर विचार करें।")
        hinglish_suggestions.append("Mitti ka pH zyada hai (kshari). pH kam karne ke liye sulfur ka use karen.")

    if rainfall < 50:
        suggestions.append("Rainfall is low. Ensure adequate irrigation to supplement water needs.")
        hindi_suggestions.append("वर्षा कम है। पानी की आवश्यकताओं को पूरा करने के लिए पर्याप्त सिंचाई सुनिश्चित करें।")
        hinglish_suggestions.append("Rainfall kam hai. Pani ki zarurat ko pura karne ke liye irrigation ka use karen.")
    elif rainfall > 200:
        suggestions.append("Rainfall is high. Ensure proper drainage to prevent waterlogging.")
        hindi_suggestions.append("वर्षा अधिक है। जलभराव को रोकने के लिए उचित जल निकासी सुनिश्चित करें।")
        hinglish_suggestions.append("Rainfall zyada hai. Jalbharav rokne ke liye proper drainage ka use karen.")

    # General suggestions based on WSI
    if wsi < 0.3:
        suggestions.append("Weather conditions are favorable for crop growth.")
        hindi_suggestions.append("मौसम की स्थिति फसल वृद्धि के लिए अनुकूल है।")
        hinglish_suggestions.append("Mausam ki sthiti fasal vridhi ke liye anukool hai.")
    elif 0.3 <= wsi < 0.6:
        suggestions.append("Some weather stress detected. Monitor closely and adjust management practices.")
        hindi_suggestions.append("कुछ मौसम तनाव का पता चला है। निकट से निगरानी करें और प्रबंधन प्रथाओं को समायोजित करें।")
        hinglish_suggestions.append("Kuch mausam tanav ka pata chala hai. Nazdik se nigrani karen aur management practices ko adjust karen.")
    else:
        suggestions.append("High weather stress detected. Take necessary measures such as increased irrigation and shading.")
        hindi_suggestions.append("उच्च मौसम तनाव का पता चला है। आवश्यक उपाय जैसे कि सिंचाई बढ़ाना और छायांकन लेना।")
        hinglish_suggestions.append("High mausam tanav ka pata chala hai. Aavashyak upay jaise irrigation badhana aur shading lena.")

    return suggestions, hindi_suggestions, hinglish_suggestions

# Define route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Define route to handle form submission
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Retrieve user input from the form
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        # Create a DataFrame for the user input
        user_input_df = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]],
                                     columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])

        # Make prediction based on user input
        prediction = best_model.predict(user_input_df)
        predicted_crop = prediction[0]

        # Calculate WSI
        wsi = calculate_wsi(N, P, K, temperature, humidity, ph, rainfall)

        # Generate detailed suggestions based on user input and WSI
        suggestions, hindi_suggestions, hinglish_suggestions = generate_suggestions(N, P, K, temperature, humidity, ph, rainfall, wsi)

        # Pass the prediction result, WSI, and suggestions to the template
        return render_template('index.html', predicted_crop=predicted_crop, wsi=round(wsi, 2), suggestions=suggestions, hindi_suggestions=hindi_suggestions, hinglish_suggestions=hinglish_suggestions)

if __name__ == '__main__':
    app.run(debug=True)
