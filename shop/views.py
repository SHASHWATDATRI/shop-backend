from rest_framework import status
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


@api_view(['POST'])
def register_user(request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "User successfully registered! Ab aap login kar sakte hain."
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --- 1. Products API ---
@api_view(['GET'])
def product_api(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# --- 2. All Artists List API ---
@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_api(request):
    # URL se category uthayein (e.g., ?category=photography)
    category_name = request.query_params.get('category', None)
    
    if category_name:
        # Database mein filter karein
        products = Product.objects.filter(category=category_name.lower())
    else:
        # Agar koi category nahi di, toh sab dikhayein
        products = Product.objects.all()
        
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# --- 3. Specific Artist Portfolio (Approved Only) ---
@api_view(['GET'])
def artist_detail(request, pk):
    try:
        artist = Artist.objects.get(pk=pk)
        
        # Artist ka basic data serialize karein
        serializer = ArtistDetailSerializer(artist)
        data = serializer.data
        
        # Yahan filter lagaya hai taaki sirf Admin se Approved creations hi dikhein
        approved_creations = artist.creations.filter(is_approved=True)
        data['creations'] = CreationSerializer(approved_creations, many=True).data
        
        return Response(data)
    except Artist.DoesNotExist:
        return Response({'error': 'Artist nahi mila'}, status=404)
        

# --- 4. Artist Login & Post API (For Artists Only) ---
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def artist_post_creation(request):
    # Check karein ki logged-in user ke paas artist profile hai ya nahi
    try:
        # User model se connected Artist profile dhoond rahe hain
        artist = request.user.artist_profile 
    except (Artist.DoesNotExist, AttributeError):
        return Response({"error": "Aap ek registered artist nahi hain. Pehle admin se profile banwayein."}, status=403)

    serializer = CreationSerializer(data=request.data)
    if serializer.is_valid():
        # Artist automatically set ho jayega aur is_approved default (False) rahega
        serializer.save(artist=artist, is_approved=False)
        return Response({
            "message": "Creation successfully bhej di gayi hai. Admin approval ka intezar karein."
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)