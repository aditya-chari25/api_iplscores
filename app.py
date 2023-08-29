from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests
import json

from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

html_text = requests.get('https://www.espncricinfo.com/live-cricket-match-results').text
live_text = requests.get('https://www.espncricinfo.com/live-cricket-score').text
all_text = requests.get('https://www.espncricinfo.com/series/indian-premier-league-2022-1298423/match-results').text

# print(html_text)
soup = BeautifulSoup(html_text,"html.parser")                  
jobs = soup.find_all('div',class_="ds-flex ds-px-4 ds-border-b ds-border-line ds-py-3");

soup_live = BeautifulSoup(live_text,"html.parser")
live_job = soup_live.find_all('div',class_="ds-px-4 ds-py-3");

soup_all = BeautifulSoup(all_text,"html.parser")
all_job = soup_all.find_all('div',class_="ds-px-4 ds-py-3");

app = Flask(__name__)

@app.route("/")
@cross_origin(supports_credentials=True)
def hello_world():
    return "<h2>Welcome to the IPL API</h2>"

@app.route("/fixture-results")
@cross_origin(supports_credentials=True)
def score_results():
    print("normal")
    arr_score = []
    a=15
    for score in jobs:
        # descp = score.find('div',class_='ds-text-tight-xs ds-truncate ds-text-ui-typo-mid')
        descp = score.find('span',class_='ds-text-title-xs ds-font-bold ds-text-typo')
        # print("haha" , descp)
        if(descp!=None):
            if(descp.span.text=="Andhra Premier League"):
                arr_score.append({"Andhra Premier League":descp.text})
                return {"haha ": arr_score}
        # if(descp.a.span.text=='Andhra Premier League'):
        #     scores_team = score.find_all('div',class_="ds-text-compact-s ds-text-typo-title")
        #     score_1 = scores_team[0].strong.text
        #     score_2 = scores_team[1].strong.text
        #     link = score.find('a',class_='').get('href')
        #     twoteams = score.find_all('p',class_='ds-text-tight-m ds-font-bold ds-capitalize')
        #     winner = score.find('p',class_='ds-text-tight-s ds-font-regular ds-truncate ds-text-typo-title').span.text
        #     team_1 = twoteams[0]
        #     team_2 = twoteams[1]
        #     match_date = descp.text.split(',')[0]
        #     location = descp.text.split(',')[1]

        #     info_scores={
        #         "Match Type" : descp.a.span.text,
        #         "Match_Result": winner,
        #         "team1_score":score_1,
        #         "team2_score":score_2
        #     }
        #     arr_score.append({
        #         "Match_Type" : descp.a.span.text,
        #         "Match_Date" : match_date,
        #         "Match_Location" : location,
        #         "Match_Result": winner,
        #         "team_1":team_1.text,
        #         "team_2":team_2.text,
        #         "team1_score":score_1,
        #         "team2_score":score_2,
        #     })
    return {"IPL_data":arr_score}

@app.route("/live-score")
@cross_origin(supports_credentials=True)
def live_results():
    arr_score = []
    a=15
    for score in live_job:
        descp = score.find('div',class_='ds-text-tight-xs ds-truncate ds-text-ui-typo-mid')
        match_date = descp.text.split(',')[0]
        location = descp.text.split(',')[1]
        scoring_team = score.find_all('div',class_="ds-text-compact-s ds-text-typo-title")
        if(descp.a.span.text=='Indian Premier League'):
             twoteams = score.find_all('p',class_='ds-text-tight-m ds-font-bold ds-capitalize')
             team_1 = twoteams[0]
             team_2 = twoteams[1]
             winner = score.find('p',class_='ds-text-tight-s ds-font-regular ds-truncate ds-text-typo-title').span.text
             if(len(scoring_team)):
                score_1 = scoring_team[0].strong.text
                score_2 = scoring_team[1].strong.text
                print(score_1)
                print(score_2)
             else:
                score_1=0
                score_2=0
                print(score_1)
                print(score_2)

             arr_score.append({
                "Match_Type" : descp.a.span.text,
                "Match_Date" : match_date,
                "Match_Location" : location,
                "Match_Result": winner,
                "team_1":team_1.text,
                "team_2":team_2.text,
                "team1_score":score_1,
                "team2_score":score_2,
            })
    return {"Live_IPL_data":arr_score}

@app.route("/all-match-results")
@cross_origin(supports_credentials=True)
def allmatch_results():
    arr_score = []
    a=15
    for score in all_job:
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
                "Match_Type" : descp.a.span.text,
                "Match_Date" : match_date,
                "Match_Location" : location,
                "Match_Result": winner,
                "team_1":team_1.text,
                "team_2":team_2.text,
                "team1_score":score_1,
                "team2_score":score_2,
            })
    return {"Match_Results":arr_score}


    
            

