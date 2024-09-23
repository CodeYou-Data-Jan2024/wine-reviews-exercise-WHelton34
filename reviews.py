import pandas as pd

df = pd.read_csv('data/winemag-data-130k-v2.csv')

country_summary = df.groupby('country').agg(
    count=('country', 'size'),
    points=('points', 'mean')
).reset_index()
country_summary['points'] = country_summary['points'].round(1)
output_file_path = r'C:\Users\willi\wine-reviews-exercise-WHelton34\data\reviews-per-country.csv'
summary.to_csv('data/reviews-per-country.csv', index=False)
print("Summary data has been written to 'data/reviews-per-country.csv'")