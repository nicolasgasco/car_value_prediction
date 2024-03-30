from DataHandler import DataHandler
from Plot import Plot


def main():
    data_handler = DataHandler()
    data_handler.load_data()
    data_handler.create_listings_df()
    listings = data_handler.get_listings()

    [x_prop, y_prop] = listings.columns
    plot = Plot(listings, x_prop, y_prop)
    plot.show(linear_regression=False)


if __name__ == "__main__":
    main()
