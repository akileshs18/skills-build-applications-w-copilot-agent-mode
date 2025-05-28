from pymongo import MongoClient

# Initialize MongoDB client
client = MongoClient("mongodb://localhost:27017/")

# Create the octofit_db database
db = client["octofit_db"]

# Create collections with proper structure
# Users collection
users = db["users"]
users.create_index({"email": 1}, unique=True)

# Teams collection
teams = db["teams"]

# Activity collection
activity = db["activity"]

# Leaderboard collection
leaderboard = db["leaderboard"]

# Workouts collection
workouts = db["workouts"]

print("Database and collections initialized successfully.")
