from re import match
from rest_framework import serializers
from .models import User, FavMovies

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate(self, data):
        if len(data['username'])<3:
            raise serializers.ValidationError("Username must be at least 3 characters long.")
        
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not match(email_regex, data['email']):
            raise serializers.ValidationError("Invalid email format.")

        if len(data['password'])<8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        
        return data
    

class FavMoviesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavMovies
        fields = '__all__'
    
    def validate(self,data):
        return data
    