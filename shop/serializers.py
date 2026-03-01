from rest_framework import serializers
from .models import Artist, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist # 'Arlist' nahi, 'Artist' (T ke saath)
        fields = '__all__'