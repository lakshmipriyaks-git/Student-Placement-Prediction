import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv('placement_data.csv')

X = df.drop('Placed', axis=1)
y = df['Placed']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# We increased n_estimators to 200 for slightly better accuracy
model = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print(f"Model trained with an improved accuracy of: {accuracy * 100:.2f}%")

with open('placement_model.pkl', 'wb') as file:
    pickle.dump(model, file)
    
print("Updated model saved!")