from rest_framework import serializers
from .models import Artist, Product, Creation # Creation model ko bhi import karein

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# 1. Pehle normal Artist list ke liye
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

# 2. Phir Creations (Paintings/Sculptures) ke liye
class CreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creation
        fields = '__all__'

# 3. Phir Artist ki Details aur unki sari Creations dikhane ke liye
class ArtistDetailSerializer(serializers.ModelSerializer):
    # 'creations' wahi naam hona chahiye jo models.py mein 'related_name' hai
    creations = CreationSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ['id', 'name', 'designation', 'artist_type', 'image_url', 'creations']

        
        
