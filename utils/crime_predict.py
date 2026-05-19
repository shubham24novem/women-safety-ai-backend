import joblib

model = joblib.load('models/crime_model.pkl')
encoder = joblib.load('models/label_encoder.pkl')

def predict_crime(latitude, longitude, hour, crime_count):
    prediction = model.predict([[latitude, longitude, hour, crime_count]])
    result = encoder.inverse_transform(prediction)

    return result[0]