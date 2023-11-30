import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from fuzzywuzzy import process
import chardet

pd.set_option('display.max_colwidth', 150)

hotels = 'booking_hotel.csv'

# Визначення кодування файлу
with open(hotels, 'rb') as f:
    result = chardet.detect(f.read())

# Читання файлу з визначеним кодуванням та обробка пропущених значень
df_hotels = pd.read_csv(hotels, usecols=['Hotel Name', 'Location', 'Rating', 'Review Score', 'Number of', 'Room Score', 'Room Type', 'Bed Type', 'Room Price'],
                        dtype={'Hotel Name': 'str', 'Location': 'str', 'Rating': 'float32', 'Review Score': 'str', 'Number of': 'float32', 'Room Score': 'float32', 'Room Type': 'str', 'Bed Type': 'str', 'Room Price': 'float32'},
                        encoding=result['encoding'],
                        index_col=False)

# Обробка пропущених значень у стовпці 'Number of'
df_hotels['Number of'].fillna(0, inplace=True)

hotels_users = df_hotels.pivot(columns='Location', values='Rating').fillna(0)
mat_hotels_users = csr_matrix(hotels_users.values)

model_knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=10)
model_knn.fit(mat_hotels_users)

def hotel_recommender(hotel_name, data, model, n_recommendations):
    model.fit(data)
    idx = process.extractOne(hotel_name, df_hotels['Hotel Name'])[2]
    print('Hotel Selected: ', df_hotels['Hotel Name'][idx], 'Index: ', idx)
    print('Searching for recommendations.....')
    distances, indices = model.kneighbors(data[idx], n_neighbors=n_recommendations)
    for i in indices:
        print(df_hotels['Hotel Name'][i].where(i != idx))

hotel_recommender('FuramaXclusive Sathorn', mat_hotels_users, model_knn, 10)

