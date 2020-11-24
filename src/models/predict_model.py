import pathlib
import pickle

import pandas as pd



PROJECT_FOLDER_PATH = pathlib.Path().resolve().parents[1]
FEATURES_FOLDER_PATH = PROJECT_FOLDER_PATH / 'data/processed'
MODELS_FOLDER_PATH = PROJECT_FOLDER_PATH / 'models'


def form_test_data(name):
    features_path = FEATURES_FOLDER_PATH / name
    test_df = pd.read_csv(features_path, index_col=0)
    X = test_df[['station_distance', 'studio', 'n_rooms', 'area', 'floor', 'mcc',
                 'circle', 'center_distance']]
    # X = test_df.drop(columns=['y', 'pub_date'])
    return X

def load_model(name):
    model_path = MODELS_FOLDER_PATH / f'{name}'
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model



X = form_test_data('features_2020-08-01_2020-08-14.csv')
model = load_model('rf_2020-08-11.pickle')
pred = model.predict(X)