from DataHandler import DataHandler
from Plot import Plot
from PricePredictor import PricePredictor

import numpy as np


def main():
    data_handler = DataHandler()
    data_handler.load_data()
    data_handler.create_listings_df()
    listings = data_handler.get_listings()

    [x_prop, y_prop] = listings.columns

    x_data = listings[x_prop]
    y_data = listings[y_prop]
    theta1, theta0 = np.polyfit(x_data, y_data, 1)

    plot = Plot(listings, x_prop, y_prop, theta0, theta1)
    plot.show(linear_regression=True)

    price_predictor = PricePredictor(listings)
    price_predictor.train()

    [estimated_price] = price_predictor.predict(50_000)
    print(f"Estimated price for 50,000 {x_prop}: {estimated_price}")


if __name__ == "__main__":
    main()
