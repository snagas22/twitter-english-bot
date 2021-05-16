# Twitter English Learning Bot

A tweet bot that tweets a random English word with definitions both in English and Japanese every 24 hours. Words are retrieved from a Google Sheets file.

## Setup

You will need to have a twitter developers account. If you do not have one already, you can create your own account [here](https://developer.twitter.com/en/apply-for-access). Also, for this time, this uses Google Sheets as its database. If planning on doing the same, you will also need to create a project in the [Google API Console](https://console.developers.google.com/) and obtain API keys to use Google Sheets as your database. Make sure to set environment variables accordingly for these API keys.

Install the requirements with: `$ pip install -r requirements.txt`

#### Required Libraries:

Besides the default python libraries, you will need to install these dependencies:
* `bs4`
* `flask`
* `gspread`
* `oauth2client`
* `requests`
* `tweepy`

## Components

### Twitter_bot class (twitter_bot.py)

There are 3 main functions maintained in the Twitter_bot class:
1. tweets a word with its definitions both in English and Japanese.
2. likes tweets on your account's feed or with a specified keyword
3. follows any follower that you have not followed back yet.

### Sheet_Controller class (sheet.py)

The Sheet_Controller class allows for CRUD operations on Google Sheets. To do so, you need to install `gspread` library. In this specific program, it focuses on retrieving values on the first column of the first worksheet, as the only things stored in the sheet are common English words.

### Scraper class (scraper.py)

The Scraper class is responsible for scraping definitions for the input word. It uses `requests` and `BeautifulSoup` to retrieve the Japanese definition from [Weblio](https://ejje.weblio.jp/). For the English definition and an example sentence, it makes an API call to [Free Dictionary API](https://api.dictionaryapi.dev/api/v2/entries/en_US/).

## Deployment

You can deploy it to Heroku. You will need a Heroku account (you can sign up for free [here](https://signup.heroku.com/) if you do not have one already) to deploy your app.

You can also schedule and run this program locally with `cron` if preferred. In that case, remove the following loop and `time.sleep()` in `tweet.py` and set a schedule with `cron` from your terminal:

```python
while True:
    sheet_name = 'Your Google Sheet name here'
    sheet.open_sheet(sheet_name, 0)
    ...

    Twitter_Bot.tweet(content)
    ...
```

## Example

Here's an example of what an automatically-generated tweet will look like:

![sample tweet](./images/sample_tweet.png "Sample Tweet")