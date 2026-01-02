from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTestCase(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')
        user1 = User.objects.create(email='ironman@marvel.com', username='Iron Man', team=marvel, is_superhero=True)
        user2 = User.objects.create(email='batman@dc.com', username='Batman', team=dc, is_superhero=True)
        Activity.objects.create(user=user1, activity_type='Running', duration=30, date='2026-01-01')
        Workout.objects.create(name='Strength', description='Strength workout')
        Leaderboard.objects.create(team=marvel, points=100)

    def test_user_team(self):
        user = User.objects.get(username='Iron Man')
        self.assertEqual(user.team.name, 'Marvel')

    def test_leaderboard(self):
        marvel = Team.objects.get(name='Marvel')
        leaderboard = Leaderboard.objects.get(team=marvel)
        self.assertEqual(leaderboard.points, 100)
