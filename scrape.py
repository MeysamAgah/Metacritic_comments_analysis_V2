import os
import re
import requests
from dotenv import load_dotenv

load_dotenv()

user_agent = os.getenv("user_agent")

def scrape_game_comments(
        game_name:str,
        reviewer_type: str,
        platform: str
):
    url = f'https://www.metacritic.com/game/{game_name}/{reviewer_type}-reviews/?platform={platform}'

    headers = {'User-Agent': user_agent}
    response = requests.get(url, headers=headers)

    main_text = re.findall('componentType=ReviewList"}]},items:(.*?);k.footer=b;k.d', str(response.content))[0]
    
    quotes = re.findall(r'quote:"(.*?)",platform', main_text)

    scores = [
        int(s) if s.isdigit() else 0
        for s in re.findall(r',score:(.*?),metaScore:', main_text)
    ]

    dates = re.findall(r',date:"(.*?)",author:', main_text)
    authors = re.findall(r',author:"(.*?)",authorSlug:', main_text)

    return {
        'quotes': quotes,
        'scores': scores,
        'dates': dates,
        'authors': authors
    }


