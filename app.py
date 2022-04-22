from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests
import json

html_text = requests.get('https://www.espncricinfo.com/live-cricket-match-results').text

# print(html_text)
soup = BeautifulSoup(html_text,'lxml')                  
jobs = soup.find_all('div',class_="ds-px-4 ds-py-3");


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/fixture-results")
def score_results():
    arr_score = []
    a=15
    for score in jobs:
        descp = score.find('div',class_='ds-text-tight-xs ds-truncate ds-text-ui-typo-mid')
        if(descp.a.span.text=='Indian Premier League'):
            scores_team = score.find_all('div',class_="ds-text-compact-s ds-text-typo-title")
            score_1 = scores_team[0].strong.text
            score_2 = scores_team[1].strong.text
            link = score.find('a',class_='').get('href')
            twoteams = score.find_all('p',class_='ds-text-tight-m ds-font-bold ds-capitalize')
            winner = score.find('p',class_='ds-text-tight-s ds-font-regular ds-truncate ds-text-typo-title').span.text
            team_1 = twoteams[0]
            team_2 = twoteams[1]
            match_date = descp.text.split(',')[0]
            location = descp.text.split(',')[1]

            info_scores={
                "Match Type" : descp.a.span.text,
                "Match_Result": winner,
                "team1_score":score_1,
                "team2_score":score_2
            }
            arr_score.append({
                "Match Type" : descp.a.span.text,
                "Match_Date" : match_date,
                "Match_Location" : location,
                "Match_Result": winner,
                "team_1":team_1.text,
                "team_2":team_2.text,
                "team1_score":score_1,
                "team2_score":score_2,
            })
    return {"data":arr_score}
    
            

