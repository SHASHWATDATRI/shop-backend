from rest_framework import serializers
from .models import Artist, Product, Creation
from django.contrib.auth.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # Password dikhega nahi, sirf write hoga

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Password ko hash (encrypt) karke save karne ke liye 'create_user' use hota hai
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

# 1. Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# 2. Artist List Serializer (Basic info ke liye)
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'designation', 'artist_type', 'image_url']

# 3. Creation Serializer (Artist isi se upload karega)
class CreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creation
        # Artist ko sirf ye 4 cheezein bhejne ki permission hogi
        fields = ['id', 'artist', 'title', 'medium', 'dimensions', 'image_url']
        # 'is_approved' ko yahan nahi rakha taaki artist khud ko approve na kar sake
        read_only_fields = ['is_approved'] 

# 4. Artist Detail Serializer (Full Portfolio ke liye)
class ArtistDetailSerializer(serializers.ModelSerializer):
    # 'creations' field views.py mein filter ho kar aayegi
    creations = CreationSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ['id', 'name', 'designation', 'artist_type', 'image_url', 'creations']