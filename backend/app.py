from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import syntax_triples.main
import sentiment.main

app = Flask(__name__)

@app.route('/')
def main():
    return 'Einherjar Online.'

@app.route('/parse', methods=['POST'])
def parse():
    return jsonify({
        'factCheck': parseFactCheck(request.json['textPayload']),
        'sentiment': parseSentimentAnalysis(request.json['textPayload']) 
    })

def parseFactCheck(text_payload):
    # Get triplets through syntax_triples
    triplets = syntax_triples.main.parseText(text_payload)
    for i in range(0, len(triplets)):
        # Check factually to fact check
        teamURL = "https://www.gov.sg/factually/all/"+triplets[i][2]+"/page-1"
        
        headers = requests.utils.default_headers()
        headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        })

        link = requests.get(teamURL, headers=headers)

        soup = BeautifulSoup(link.content, 'html.parser')
        newsitems = soup.select('.noresults')
        if not newsitems:
            return True
    return False

def parseSentimentAnalysis(text_payload):
    score, magnitude = sentiment.main.analyzeText(text_payload)
    return [score, magnitude]