from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()

class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    members = serializers.ListField()

class ActivitySerializer(serializers.Serializer):
    user = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()

class LeaderboardSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=100)
    score = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    difficulty = serializers.CharField(max_length=100)