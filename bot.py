from flask import Flask
from mastodon import Mastodon
import schedule
import time


app = Flask(__name__)

def job():
    mastodon = Mastodon (
        access_token = 'token.secret',
        api_base_url = 'https://botsin.space/'
        )
    media = mastodon.media_post("media/thursday.jpg", description="Nadia from the Russian Doll fearing that she would never see a Thursday again says, \"Thursday. What a concept\" while smoking a cigarette")
    mastodon.status_post("Thursday. What a concept.", media_ids=[media])

schedule.every().thursday.at("00:00").do(job)
schedule.every().thursday.at("14:00").do(job)
schedule.every().tuesday.at("23:54").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
