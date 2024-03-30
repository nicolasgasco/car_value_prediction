from Scraper import Scraper


def main():
    scraper = Scraper({
        'make': 'ferrari',
        'model': '575',
        'min_year': None,
        'max_year': None,
        'country': None
    })

    scraper.scrape_listings()


if __name__ == "__main__":
    main()
