from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
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


# --- 2. PRODUCTS BY CATEGORY SLUG ---
@api_view(['GET'])
def products_by_category(request, category_slug):
    products = Product.objects.filter(category__iexact=category_slug)
    if not products.exists():
        return Response({"message": f"Category '{category_slug}' mein koi products nahi hain."}, status=404)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


# --- 3. PRODUCTS API (QUERY PARAM BASED) ---
@api_view(['GET'])
def product_api(request):
    category_name = request.query_params.get('category', None)
    if category_name:
        products = Product.objects.filter(category__iexact=category_name)
    else:
        products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


# --- 4. ALL ARTISTS LIST ---
@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)


# --- 5. ARTIST DETAIL (PORTFOLIO) ---
@api_view(['GET'])
def artist_detail(request, pk):
    try:
        artist = Artist.objects.get(pk=pk)
        serializer = ArtistDetailSerializer(artist)
        data = serializer.data
        approved_creations = artist.creations.filter(is_approved=True)
        data['creations'] = CreationSerializer(approved_creations, many=True).data
        return Response(data)
    except Artist.DoesNotExist:
        return Response({'error': 'Artist nahi mila'}, status=404)


# --- 6. ARTIST UPLOAD API ---
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def artist_post_creation(request):
    try:
        artist = request.user.artist_profile 
    except (Artist.DoesNotExist, AttributeError):
        return Response({"error": "Aap ek registered artist nahi hain. Admin se profile banwayein."}, status=403)

    serializer = CreationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(artist=artist, is_approved=False)
        return Response({
            "message": "Creation successfully bhej di gayi hai. Admin approval ka intezar karein."
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --- 7. ADMIN PROFILE & STATUS CHECK ---
# Isse aapka friend Next.js mein admin dashboard access de payega
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    user = request.user
    return Response({
        "username": user.username,
        "is_staff": user.is_staff,  # True matlab Admin hai
        "is_superuser": user.is_superuser,
        "email": user.email
    })


# --- 8. PRODUCT VIEWSET (FOR ROUTER) ---
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        if category:
            return Product.objects.filter(category__iexact=category)
        return Product.objects.all()