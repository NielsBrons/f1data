from home.models import Races, Events, Circuit, Point, Driver, Result, PointMath
import json
import requests
from datetime import datetime, timedelta

def run():
  import_results()

def import_results(season='current', season_round='last', backfill=True):
  res = requests.get(f'http://ergast.com/api/f1/{season}/{season_round}/results.json')
  data = res.json()
  
  data = data['MRData']['RaceTable']['Races'][0]
  
  import_season = int(data['season'])
  import_round = int(data['round'])
  
  # get race event object
  
  race_object = Races.objects.get(season=import_season, round=import_round)
  event_object = Events.objects.get(race=race_object, type=Events.RACE)
  
  for r in data['Results']:
    
    # getting data from json
    
    driver = r['Driver']
    driver_name = driver['givenName'] + " " + driver['familyName']
    driver_number = int(r['number'])
    driver_position = int(r['position'])
    driver_points = int(r['points'])
    driver_permanent_number = int(driver['permanentNumber'])
    driver_nationality = driver['nationality']
    driver_team = r['Constructor']['name']
    
    # time math, must be a better way?
    # add timings later because the api math is relative to the number 1
    driver_time_delta = timedelta(minutes=0, seconds=0)
    #driver_time = r['Time']['time']
    #driver_time_timeobject = datetime.strptime(driver_time, '%H:%M:%S.%f')
    # driver_time_delta = timedelta(hours=driver_time_timeobject.hour, minutes=driver_time_timeobject.minute, 
    #                              seconds=driver_time_timeobject.second, microseconds=driver_time_timeobject.microsecond)
    #driver_fastest_lap = r['FastestLap']['Time']['time']
    #driver_fastest_lap_timeobject = datetime.strptime(driver_fastest_lap, '%M:%S.%f')
    # driver_fastest_lap_delta = timedelta(hours=driver_fastest_lap_timeobject.hour, minutes=driver_fastest_lap_timeobject.minute, 
    #                              seconds=driver_fastest_lap_timeobject.second, microseconds=driver_fastest_lap_timeobject.microsecond)
    
    driver_fastest_lap_delta = timedelta(minutes=0, seconds=0)
    
    
    driver_object, created = Driver.objects.get_or_create(name=driver_name, number=driver_number, permanent_number=driver_permanent_number, team=driver_team, nationality=driver_nationality)
    result_object, created = Result.objects.update_or_create(event=event_object, driver=driver_object,
                                                             defaults={'event' : event_object, 'driver' : driver_object, 'points': driver_points, 
                                                                       'total_time': driver_time_delta, 'fastest_lap': driver_fastest_lap_delta,
                                                                       'position': driver_position})
    
    
    points_object, created = Point.objects.update_or_create(round_number=import_round, season=import_season, driver=driver_object,
                                                           defaults={'points': driver_points})
    
    
    
