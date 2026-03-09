from rest_framework import serializers
from .models import Artist, Product, Creation, ProductImage # ProductImage ko import kiya
from django.contrib.auth.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image_url']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'image_url', 
            'stock', 'category', 'artist_name', 'dimensions', 'images'
        ]

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'designation', 'artist_type', 'image_url']

class CreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creation
        fields = ['id', 'artist', 'title', 'medium', 'dimensions', 'image_url', 'is_approved']
        read_only_fields = ['is_approved'] 

class ArtistDetailSerializer(serializers.ModelSerializer):
    creations = CreationSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ['id', 'name', 'designation', 'artist_type', 'image_url', 'creations']