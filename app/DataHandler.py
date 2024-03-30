import json as json
import os as os
import pandas as pd
import re as re

DATA_DIRECTORY_PATH = "../data/scraped"


class DataHandler:
    def __init__(self):
        self._listings = pd.DataFrame({
            'mileage': [],
            'price': []
        })

    def load_data(self):
        """
        Load data from CSV files in the specified directory and concatenate them into a single DataFrame.

        Returns:
            None
        """

        for filename in os.listdir(DATA_DIRECTORY_PATH):
            if filename.endswith(".csv"):
                file_path = os.path.join(DATA_DIRECTORY_PATH, filename)

                with open(file_path, "r") as file:
                    file_listings = pd.read_csv(file_path)

                    file_listings['price'] = file_listings['price'].astype(
                        float)
                    file_listings['mileage'] = file_listings['mileage'].astype(
                        int)

                    self._listings = pd.concat(
                        [self._listings, file_listings], ignore_index=True)

    def get_listings(self):
        return self._listings
