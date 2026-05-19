import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

df = pd.read_csv('dataset/crime_data.csv')

encoder = LabelEncoder()
df['label'] = encoder.fit_transform(df['label'])

X = df[['latitude', 'longitude', 'hour', 'crime_count']]
y = df['label']

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, 'models/crime_model.pkl')
joblib.dump(encoder, 'models/label_encoder.pkl')

print("Crime model trained successfully")