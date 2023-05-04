from bs4 import BeautifulSoup
import requests
import pprint

res = requests.get('https://swarajyamag.com/section/technology')
soup = BeautifulSoup(res.text, 'html.parser')
stories = soup.select('._2uG-s')

def swaraj_technology_story(stories= stories):
	stories_list = []
	for story in stories:
		stories_title = story.getText()
		stories_link = story.get('href', None)
		stories_list.append({'Title': stories_title,'Links': 'https://swarajyamag.com' + stories_link})

	return stories_list

if __name__ == '__main__':
	for index in swaraj_techology_story(stories):
		pprint.pprint(index)

	
