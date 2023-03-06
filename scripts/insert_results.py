from home.models import Races, Events, Circuit, Point, Driver, Results, PointMath
import json
import requests
from datetime import datetime

def run():
  import_results()

def import_results(season='current', season_round='last', backfill=True):
  res = requests.get(f'http://ergast.com/api/f1/{season}/{current}/results.json')
  data = res.json()
  
  data = data['MRData']['RaceTable']['Races'][0]
  
  import_season = data['season'] 
  import_round = data['round']
  
  for r in data['Results']:
    
    # getting data from json
    
    driver = r['Driver']
    driver_name = driver['givenName'] + " " + driver['familyName']
    driver_number = r['number']
    driver_position = r['position']
    driver_points = r['points']
    driver_permanent_number = driver['permanentNumber']
    driver_nationality = driver['nationality']
    driver_team = driver['Constructor']['name']
    driver_time = r['Time']['time']
    driver_fastest_lap = r['FastestLap']['Time']['time']
    
    
    driver_object = Driver.objects.get_or_create(name=driver_name, number=driver_number, permanent_number=driver_permanent_number, team=driver_team)
    
    
