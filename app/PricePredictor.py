from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import numpy as np


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
