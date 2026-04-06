import pandas as pd
import numpy as np

np.random.seed(42)

data = {
    'CGPA': np.round(np.random.uniform(6.0, 10.0, 500), 2),
    'Internships': np.random.randint(0, 4, 500),
    'Projects': np.random.randint(0, 5, 500),
    'Aptitude_Score': np.random.randint(50, 100, 500),
    'Soft_Skills_Rating': np.random.randint(1, 6, 500),
    'Coding_Skills_Rating': np.random.randint(1, 6, 500) 
}

df = pd.DataFrame(data)


def calculate_placement(row):
    score = (row['CGPA'] * 10) + (row['Internships'] * 15) + (row['Projects'] * 12) + \
            (row['Aptitude_Score'] * 0.5) + (row['Soft_Skills_Rating'] * 4) + \
            (row['Coding_Skills_Rating'] * 8)
    return 1 if score > 175 else 0

df['Placed'] = df.apply(calculate_placement, axis=1)

df.to_csv('placement_data.csv', index=False)
print("Updated dataset created successfully!")