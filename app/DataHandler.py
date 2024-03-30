import json as json
import os as os
import pandas as pd
import re as re

DATA_DIRECTORY_PATH = "../data/scraped"


class DataHandler:
    def __init__(self):
        self._raw_listings = []
        self._listings = []

    def load_data(self):
        """
        Loads data from JSON files in the specified directory and stores it in the `_raw_listings` attribute.

        Returns:
            None
        """

        raw_listings = []
        for filename in os.listdir(DATA_DIRECTORY_PATH):
            if filename.endswith(".json"):
                file_path = os.path.join(DATA_DIRECTORY_PATH, filename)

                with open(file_path, "r") as file:
                    file_data = file.read()
                    parsed_file_data = json.loads(file_data)

                    file_raw_listings = parsed_file_data["pageProps"]["listings"]
                    raw_listings.extend(file_raw_listings)

        self._raw_listings = raw_listings

    def _transform_listing(self, listing):
        """
        Transforms a car listing into a dictionary containing the price and mileage.

        Args:
            listing (dict): A dictionary representing a car listing.

        Returns:
            dict: A dictionary containing the price and mileage of the car listing.
        """

        raw_price = listing["price"]["priceFormatted"]
        raw_price = raw_price.replace(".", "")
        price = float(re.sub(r"[^\d.]", "", raw_price))

        mileage = int(listing["tracking"]['mileage'])

        return {"mileage": mileage, "price": price}

    def create_listings_df(self):
        """
        Creates a DataFrame from the raw listings data.

        Returns:
            pandas.DataFrame: The DataFrame containing the formatted listings data.
        """

        formatted_listings = map(self._transform_listing, self._raw_listings)

        df = pd.DataFrame(formatted_listings)
        self._listings = df

        print(max(df['mileage']))

    def get_listings(self):
        return self._listings
