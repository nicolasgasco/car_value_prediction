from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import datetime as datetime
import json as json
import numpy as np
import os as os


class PricePredictor:
    def __init__(self, data):
        self._data = data
        self._X = data.drop("price", axis=1)
        self._y = data["price"]

        self._X_train = None
        self._X_test = None
        self._y_train = None
        self._y_test = None

        self._model = None

    def train(self):
        X_train, X_test, y_train, y_test = train_test_split(
            self._X, self._y, test_size=0.2, random_state=42)

        self._X_train = X_train
        self._X_test = X_test
        self._y_train = y_train
        self._y_test = y_test

        self._model = LinearRegression()

        self._model.fit(X_train, y_train)

    def predict(self, value):
        assert self._model is not None, "Model is not trained"
        return self._model.predict(np.array(value).reshape(-1, 1))

    def store_predictions(self):
        PREDICTIONS_DIRECTORY_PATH = "../data/predictions"

        max_mileage = self._data['mileage'].max()

        predictions_description = {
            'min_value': "0",
            'max_value': f"{max_mileage}",
            'predicted_at': datetime.datetime.now().strftime("%Y-%m-%d"),
            'scraped_at': (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"),
        }

        predictions = {}
        for x in range(0, max_mileage):
            prediction = self.predict(x)[0]
            predictions[x] = f"{int(prediction)}"

        predictions_description['predictions'] = predictions

        predictions_description_json = json.dumps(predictions_description)

        try:
            with open(PREDICTIONS_DIRECTORY_PATH + "/predictions.json", "w") as file:
                file.write(predictions_description_json)
        except Exception as e:
            print(f"An error occurred while trying to write the file: {e}")
