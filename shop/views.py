from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .models import Artist
# shop/views.py ki line 4-5 ke paas ye sahi karein
from .serializers import ProductSerializer, ArtistSerializer # ArtistSerializer ko yahan add karein

@api_view(['GET'])
def product_api(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def artist_list(request):
    # 'Arlist' ko badal kar 'Artist' kijiye
    artists = Artist.objects.all() 
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)