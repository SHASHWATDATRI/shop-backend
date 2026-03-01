from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .models import Artist
from .serializers import ProductSerializer

@api_view(['GET'])
def product_api(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)