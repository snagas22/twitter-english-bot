import time
from scraper import Scraper
from twitter_bot import Twitter_bot
from sheet import Sheet_Controller


def main():
    interval = 60 * 60 * 8

    # opening up the google sheet
    sheet = Sheet_Controller()
    sheet.authorize_access()
    scraper = Scraper()
    Twitter_Bot = Twitter_bot()

    while True:
        sheet_name = 'English Useful Contents'
        sheet.open_sheet(sheet_name, 0)
        sheet.open_sheet(sheet_name, 1)
        term = sheet.get_value()

        # grab data for the term
        content_json = scraper.crawl(term)

        jpn = content_json['jpn']
        eng = content_json['meanings'][0]['definitions'][0]['definition']
        example = content_json['meanings'][0]['definitions'][0]['example']

        content = "今日の単語: " + term + "\n\n意味: " + jpn + "\ndef: " + eng + "\n例: " + example

        Twitter_Bot.tweet(content)

        # likes tweets on the feed as well as with keywords in them
        Twitter_Bot.favorite_tweets(location='global', count=100, keyword='英語')
        Twitter_Bot.favorite_tweets(location='feed', count=100)

        # folllow anyone who's following you
        Twitter_Bot.follow_followers()

        # tweets only once a day
        time.sleep(interval)
        # print(content)


if __name__ == '__main__':
    main()