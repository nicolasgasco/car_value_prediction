from DataHandler import DataHandler
from Plot import Plot
from PricePredictor import PricePredictor

import numpy as np


def main():
    print("Loading raw data...\n")
    data_handler = DataHandler()
    data_handler.load_data()
    listings = data_handler.get_listings()

    print("Training model...\n")
    price_predictor = PricePredictor(listings)
    price_predictor.train()

    [x_prop, y_prop] = listings.columns
    theta1, theta0 = price_predictor.get_thetas()

    print("Plotting data...\n")
    plot = Plot(listings, x_prop, y_prop, theta0, theta1)
    plot.show(linear_regression=True)

    print("Storing predictions for each km...\n")
    price_predictor.store_predictions()


if __name__ == "__main__":
    main()
