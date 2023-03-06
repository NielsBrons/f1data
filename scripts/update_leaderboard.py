from home.models import Races, Events, Circuit, Point, Driver, Result, PointMath
from django.db.models import Sum

CURRENT_SEASON = 2023

def run():
  update_leaderboard()
  
def update_leaderboard(season=CURRENT_SEASON):
  scores = Point.objects.filter(season=CURRENT_SEASON).annotate(total_points=Sum('points').values('driver', 'total_points'))
