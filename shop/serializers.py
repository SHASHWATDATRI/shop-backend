from rest_framework import serializers
from .models import Artist, Product, Creation, ProductImage # ProductImage ko import kiya
from django.contrib.auth.models import User

# --- 1. User Registration Serializer ---
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

# --- 2. Multiple Product Images Serializer ---
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image_url']

# --- 3. Product Serializer (With Dimensions & Multiple Images) ---
class ProductSerializer(serializers.ModelSerializer):
    # 'images' field multiple photos dikhayega (Related Name in models)
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        # Saari fields including new ones (category, artist_name, dimensions)
        fields = [
            'id', 'name', 'description', 'price', 'image_url', 
            'stock', 'category', 'artist_name', 'dimensions', 'images'
        ]

# --- 4. Artist List Serializer ---
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'designation', 'artist_type', 'image_url']

# --- 5. Creation Serializer (Artist Uploads) ---
class CreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creation
        fields = ['id', 'artist', 'title', 'medium', 'dimensions', 'image_url', 'is_approved']
        # Artist khud ko approve nahi kar sakta, sirf Admin karega
        read_only_fields = ['is_approved'] 

# --- 6. Artist Detail Serializer (Full Portfolio) ---
class ArtistDetailSerializer(serializers.ModelSerializer):
    creations = CreationSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ['id', 'name', 'designation', 'artist_type', 'image_url', 'creations']