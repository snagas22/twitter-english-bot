from bs4 import BeautifulSoup
import requests


class Scraper:
    def __init__(self):
        self.USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        self.URL = "https://ejje.weblio.jp/content/"
        self.API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"

    def crawl(self, term):        
        # get request for english contents for the input term from WordsAPI
        data = self.get_definition(term)

        # get Japanese definition
        jpn_def = self.get_definition_jpn(term)

        data['jpn'] = jpn_def
        return data

    # extract japanese definition from Weblio
    def get_definition_jpn(self, term):
        try:
            self.URL += term
            req = requests.get(self.URL, headers={'user-agent': self.USER_AGENT})
            soup_jpn = BeautifulSoup(req.content, 'html.parser')
        except Exception as e:
            print(f"@Error with url: {self.URL}")
            print(f"\tError message: {e}")
            exit(1)

        definitions = soup_jpn.find_all('td', class_="content-explanation ej")
        for definition in definitions:
            return definition.text
    
    # access dictionaryAPI
    def get_definition(self, term):
        self.API_URL += term
        resp = requests.get(self.API_URL, headers={'user-agent': self.USER_AGENT})
        # raise error if not 200
        if resp.status_code != 200:
            raise ApiError('GET /words/ {}'.format(resp.status_code))
        data = resp.json()[0]
        return data


# def main():
#     scraper = Scraper()
#     json = scraper.crawl('academic')
#     print(json)

# if __name__ == "__main__":
#     main()