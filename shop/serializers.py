from rest_framework import serializers
from .models import Product
from .models import Artist

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' # Saari details (name, price, image URL) bhejega

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'