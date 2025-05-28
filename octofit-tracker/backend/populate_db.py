from pymongo import MongoClient

# Initialize MongoDB client
client = MongoClient("mongodb://localhost:27017/")

# Connect to the octofit_db database
db = client["octofit_db"]

# Test data for users
users_data = [
    {"email": "user1@example.com", "name": "User One", "age": 25},
    {"email": "user2@example.com", "name": "User Two", "age": 30},
]

# Test data for teams
teams_data = [
    {"name": "Team Alpha", "members": ["user1@example.com", "user2@example.com"]},
    {"name": "Team Beta", "members": []},
]

# Test data for activities
activities_data = [
    {"user": "user1@example.com", "type": "running", "duration": 30},
    {"user": "user2@example.com", "type": "cycling", "duration": 45},
]

# Test data for leaderboard
leaderboard_data = [
    {"user": "user1@example.com", "score": 100},
    {"user": "user2@example.com", "score": 150},
]

# Test data for workouts
workouts_data = [
    {"name": "Workout A", "difficulty": "easy"},
    {"name": "Workout B", "difficulty": "hard"},
]

# Insert test data into users collection
users = db["users"]
users.insert_many(users_data)

# Insert test data into teams collection
teams = db["teams"]
teams.insert_many(teams_data)

# Insert test data into activity collection
activity = db["activity"]
activity.insert_many(activities_data)

# Insert test data into leaderboard collection
leaderboard = db["leaderboard"]
leaderboard.insert_many(leaderboard_data)

# Insert test data into workouts collection
workouts = db["workouts"]
workouts.insert_many(workouts_data)

print("Test data inserted successfully.")
