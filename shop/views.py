from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Artist
# Teeno serializers ko import karna zaroori hai
from .serializers import ProductSerializer, ArtistSerializer, ArtistDetailSerializer

@api_view(['GET'])
def product_api(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def artist_list(request):
    # Sabhi artists ki basic list ke liye
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def artist_detail(request, pk):
    # Ek specific artist (jaise Aditya Singh) aur unki saari creations ke liye
    try:
        artist = Artist.objects.get(pk=pk)
        serializer = ArtistDetailSerializer(artist)
        return Response(serializer.data)
    except Artist.DoesNotExist:
        return Response({'error': 'Artist nahi mila'}, status=404)