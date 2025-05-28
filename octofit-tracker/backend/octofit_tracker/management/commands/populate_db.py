from django.core.management.base import BaseCommand
import pymongo

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["octofit_db"]

        # Populate users collection
        users = db["users"]
        users.insert_many([
            {"email": "user1@example.com", "name": "User One", "age": 25},
            {"email": "user2@example.com", "name": "User Two", "age": 30},
        ])

        # Populate teams collection
        teams = db["teams"]
        teams.insert_many([
            {"name": "Team Alpha", "members": ["user1@example.com", "user2@example.com"]},
            {"name": "Team Beta", "members": []},
        ])

        # Populate activity collection
        activity = db["activity"]
        activity.insert_many([
            {"user": "user1@example.com", "type": "running", "duration": 30},
            {"user": "user2@example.com", "type": "cycling", "duration": 45},
        ])

        # Populate leaderboard collection
        leaderboard = db["leaderboard"]
        leaderboard.insert_many([
            {"user": "user1@example.com", "score": 100},
            {"user": "user2@example.com", "score": 150},
        ])

        # Populate workouts collection
        workouts = db["workouts"]
        workouts.insert_many([
            {"name": "Workout A", "difficulty": "easy"},
            {"name": "Workout B", "difficulty": "hard"},
        ])

        self.stdout.write(self.style.SUCCESS('Test data populated successfully'))
