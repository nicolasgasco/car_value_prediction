from bs4 import BeautifulSoup
import pandas as pd
import requests as requests

DATA_DIRECTORY_PATH = "../data/scraped"


class Scraper:
    def __init__(self, url_options):
        assert "make" in url_options, "Make is required"
        assert "model" in url_options, "Model is required"
        assert "min_year" in url_options, "Min year is required"
        assert "max_year" in url_options, "Max year is required"
        if (url_options["country"] is not None):
            assert url_options["country"] in [
                "es", "de", "fr", "it"], "If provided, country must be one of: es, de, fr, it"

        self.listings = pd.DataFrame({
            'mileage': [],
            'price': []
        })
        self._url = self._build_url(url_options)

    def _format_country(self, country):
        if (country is None):
            return "D%2CA%2CB%2CE%2CF%2CI%2CL%2CNL"

        return {
            "es": "E",
            "de": "D",
            "fr": "F",
            "it": "I"
        }[country]

    def _build_url(self, url_options):
        make, model, min_year, max_year, country = url_options.values()

        model_param = model if model is not None else ""
        return f"https://www.autoscout24.es/lst/{make}/{model_param}?&cy={self._format_country(country)}&damaged_listing=exclude&fregfrom={min_year or ""}&fregto={max_year or ""}&page=1"

    def _parse_price(self, raw_price):
        str_price = raw_price.replace('.', '').replace(
            ',', '').replace('-', '').replace('€', '').strip()
        return float(str_price)

    def _parse_mileage(self, raw_mileage):
        str_mileage = raw_mileage.replace(' km', '').replace('.', '').strip()
        return int(str_mileage)

    def _parse_listing(self, article):
        raw_price = article.find(
            'p', attrs={"data-testid": "regular-price"}).text
        price: float = self._parse_price(raw_price)

        raw_mileage = article.find(
            'span', attrs={"data-testid": "VehicleDetails-mileage_road"}).text
        mileage: int = self._parse_mileage(raw_mileage)

        return {
            'mileage': mileage,
            'price': price
        }

    def _store_listings(self):
        today_date = pd.Timestamp.now().strftime('%Y-%m-%d')

        self.listings.to_csv(
            f"{DATA_DIRECTORY_PATH}/listings_{today_date}.csv", index=False)

    def scrape_listings(self):
        is_last_page: bool = False
        page_num: int = 1

        while not is_last_page:
            paginated_url = self._url.replace('page=1', f'page={page_num}')
            print(paginated_url)
            req = requests.get(paginated_url)

            all_articles = BeautifulSoup(req.text, 'html.parser').find_all(
                'article', attrs={"data-testid": "list-item"})
            len_all_articles = len(all_articles)

            if (len_all_articles == 0):
                is_last_page = True
                continue

            print(f"Found {len_all_articles} listings on page {page_num}")

            for article in all_articles:
                new_listing = self._parse_listing(article)

                self.listings = pd.concat(
                    [self.listings, pd.DataFrame([new_listing])], ignore_index=True)

            page_num += 1

        self.listings.sort_values(by='mileage', inplace=True)
        self._store_listings()
