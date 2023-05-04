from notifypy import Notify
from news_scrapping import swaraj_technology_story
import time

save_stories = swaraj_technology_story()

for story in save_stories :
	notification = Notify()
	notification.title = story['Title']
	notification.message = story['Links']
	notification.audio = "./mix.wav"
	notification.send(block= False)
	time.sleep(60)