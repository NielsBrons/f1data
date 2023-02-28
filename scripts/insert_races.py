from home.models import Races, Events, Circuit
import json
import requests
from datetime import datetime

def run():
    import_races()

# import 2023 races from Ergast API and insert into database
def import_races():
    res = requests.get('http://ergast.com/api/f1/2023.json')
    data = res.json()

    for r in data['MRData']['RaceTable']['Races']:
        circ = Circuit.objects.get_or_create(name=r['Circuit']['circuitName'], country=r['Circuit']['Location']['country'])
        rc = Races.objects.get_or_create(name=r['raceName'], season=r['season'], round=r['round'], circuit=circ[0])
        event = Events.objects.get_or_create(date=r['date'], time=r['time'][:-1], type=Events.RACE, race=rc[0])
        try:
            p1 = r['FirstPractice']
            event = Events.objects.get_or_create(date=p1['date'], time=p1['time'][:-1], type=Events.PRACTICE1, race=rc[0])
        except KeyError:
            print('no q1')
        
        try:
            p2 = r['SecondPractice']
            event = Events.objects.get_or_create(date=p2['date'], time=p2['time'][:-1], type=Events.PRACTICE2, race=rc[0])
        except KeyError:
            print('no q2')

        try:
            p3 = r['ThirdPractice']
            event = Events.objects.get_or_create(date=p3['date'], time=p3['time'][:-1], type=Events.PRACTICE3, race=rc[0])

        except KeyError:
            print('no q3')

        try:
            sprint = r['Sprint']
            event = Events.objects.get_or_create(date=sprint['date'], time=sprint['time'][:-1], type=Events.SPRINT, race=rc[0])
        except KeyError:
            print('no sprint')

        try:
            qualifying = r['Qualifying']
            event = Events.objects.get_or_create(date=qualifying['date'], time=qualifying['time'][:-1], type=Events.QUALIFYING, race=rc[0])
        except KeyError:
            print('no qualifying')
