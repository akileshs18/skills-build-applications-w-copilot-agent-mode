from pymongo import MongoClient

# Initialize MongoDB client
client = MongoClient("mongodb://localhost:27017/")

# Create the octofit_db database
db = client["octofit_db"]

# Create collections with proper structure
# Users collection
users = db["users"]
users.create_index([("email", 1)], unique=True)

# Create additional collections
teams = db["teams"]
activity = db["activity"]
leaderboard = db["leaderboard"]
workouts = db["workouts"]

# Ensure collections are created by inserting dummy data
teams.insert_one({"name": "Dummy Team"})
activity.insert_one({"type": "Dummy Activity"})
leaderboard.insert_one({"user": "Dummy User", "score": 0})
workouts.insert_one({"name": "Dummy Workout", "difficulty": "easy"})

print("All collections initialized successfully.")
print("Dummy data inserted into all collections.")
