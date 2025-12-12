from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)  

@app.route("/contact/")
def MaPremiereAPI():
    return render_template("contact.html")

@app.route("/histogramme/")
def monhistogramme():
    return render_template("histogramme.html")

@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")

@app.route('/tawarano/')
def meteo():
    response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('main', {}).get('temp') - 273.15  
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html')
@app.route('/commits/')
def page_commits():
    return render_template("commits.html")


@app.route('/api/commits/')
def get_commits_data():
    # REMPLACE CI-DESSOUS PAR TON PSEUDO ET LE NOM DE TON REPO !
    # Exemple : https://api.github.com/repos/JeanDupont/Metriques/commits
    url = "https://api.github.com/repos/Ethann-ISEP/5MCSI_Metriques/commits"
    
    try:
        response = urlopen(url)
        raw_content = response.read()
        json_content = json.loads(raw_content.decode('utf-8'))
        minutes_list = []
        for commit_element in json_content:
            date_string = commit_element['commit']['author']['date']
            date_object = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ')
            minutes_list.append([date_object.minute]) 
        return jsonify(results=minutes_list)
  
if __name__ == "__main__":
  app.run(debug=True)
