from rest_framework import serializers
from .models import Artist, Product, Creation

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