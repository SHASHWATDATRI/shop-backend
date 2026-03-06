from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Product, Artist, Creation
from .serializers import (
    ProductSerializer, 
    ArtistSerializer, 
    ArtistDetailSerializer, 
    CreationSerializer,
    UserRegisterSerializer
)

# --- 1. USER REGISTRATION ---
@api_view(['POST'])
def register_user(request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "User successfully registered! Ab aap login kar sakte hain."
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --- 2. PRODUCTS API (FUNCTION BASED) ---
# Isme category filter aur simple list dono merge kar diye hain
@api_view(['GET'])
def product_api(request):
    # URL se category uthayein (e.g., ?category=photography)
    category_name = request.query_params.get('category', None)
    
    if category_name:
        # Database mein filter karein
        products = Product.objects.filter(category__iexact=category_name)
    else:
        # Agar koi category nahi di, toh sab dikhayein
        products = Product.objects.all()
        
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


# --- 3. ARTIST LIST API ---
@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)


# --- 4. ARTIST DETAIL (PORTFOLIO) ---
@api_view(['GET'])
def artist_detail(request, pk):
    try:
        artist = Artist.objects.get(pk=pk)
        serializer = ArtistDetailSerializer(artist)
        data = serializer.data
        
        # Sirf Approved creations dikhane ka logic
        approved_creations = artist.creations.filter(is_approved=True)
        data['creations'] = CreationSerializer(approved_creations, many=True).data
        
        return Response(data)
    except Artist.DoesNotExist:
        return Response({'error': 'Artist nahi mila'}, status=404)


# --- 5. ARTIST UPLOAD API ---
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def artist_post_creation(request):
    try:
        artist = request.user.artist_profile 
    except (Artist.DoesNotExist, AttributeError):
        return Response({"error": "Aap ek registered artist nahi hain. Pehle admin se profile banwayein."}, status=403)

    serializer = CreationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(artist=artist, is_approved=False)
        return Response({
            "message": "Creation successfully bhej di gayi hai. Admin approval ka intezar karein."
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --- 6. PRODUCT VIEWSET (CLASS BASED) ---
# Router use karne ke liye aapki class bhi niche de di hai
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        if category:
            return Product.objects.filter(category__iexact=category)
        return Product.objects.all()