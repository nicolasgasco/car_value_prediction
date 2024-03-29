from DataHandler import DataHandler


def main():
    data_handler = DataHandler()
    data_handler.load_data()
    data_handler.create_listings_df()


if __name__ == "__main__":
    main()
