import requests
import json
from collections import defaultdict

API_URL = "https://api.weather.com/v1"

def fetch_weather(city):
    response = requests.get(f"{API_URL}/current?city={city}")
    if response.status_code == 200:
        return response.json()
    return None

def calculer_moyenne_temp(mesures):
    temperatures = [m['temperature'] for m in mesures]
    return sum(temperatures) / len(temperatures)

def grouper_par_ville(mesures):
    groupes = defaultdict(list)
    for mesure in mesures:
        groupes[mesure['ville']].append(mesure)
    return groupes

def trouver_ville_plus_chaude(mesures):
    groupes = grouper_par_ville(mesures)
    max_temp = 0
    ville_max = None
    for ville, mesures_ville in groupes.items():
        moyenne = calculer_moyenne_temp(mesures_ville)
        if moyenne > max_temp:
            max_temp = moyenne
            ville_max = ville
    return ville_max

def sauvegarder_resultats(resultats, filepath):
    with open(filepath, 'a') as f:
        json.dump(resultats, f, indent=2)

if __name__ == '__main__':
    villes = ['Paris', 'London', 'Berlin']
    toutes_mesures = []
    for ville in villes:
        data = fetch_weather(ville)
        if data:
            toutes_mesures.append({
                'ville': ville,
                'temperature': data['temp'],
                'humidity': data['humidity']
            })
    ville_plus_chaude = trouver_ville_plus_chaude(toutes_mesures)
    sauvegarder_resultats({'ville_plus_chaude': ville_plus_chaude}, 'resultats.json')