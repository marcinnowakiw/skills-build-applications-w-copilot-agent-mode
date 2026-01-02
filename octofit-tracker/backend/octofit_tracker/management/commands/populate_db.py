from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating teams...'))
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        self.stdout.write(self.style.SUCCESS('Creating users...'))
        ironman = User.objects.create(email='ironman@marvel.com', username='Iron Man', team=marvel, is_superhero=True)
        captain = User.objects.create(email='captain@marvel.com', username='Captain America', team=marvel, is_superhero=True)
        batman = User.objects.create(email='batman@dc.com', username='Batman', team=dc, is_superhero=True)
        superman = User.objects.create(email='superman@dc.com', username='Superman', team=dc, is_superhero=True)

        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        Activity.objects.create(user=ironman, activity_type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=batman, activity_type='Cycling', duration=45, date=timezone.now().date())

        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        w1 = Workout.objects.create(name='Strength', description='Strength workout')
        w2 = Workout.objects.create(name='Cardio', description='Cardio workout')
        w1.suggested_for.set([ironman, batman])
        w2.suggested_for.set([captain, superman])

        self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
        Leaderboard.objects.create(team=marvel, points=200)
        Leaderboard.objects.create(team=dc, points=180)

        self.stdout.write(self.style.SUCCESS('Test data created successfully!'))
