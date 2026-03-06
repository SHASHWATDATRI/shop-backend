from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from shop.views import (
    product_api, artist_list, artist_detail, 
    register_user, artist_post_creation, ProductViewSet
)

# ViewSet ke liye router
router = DefaultRouter()
router.register(r'products-viewset', ProductViewSet, basename='product-viewset')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. Products (Isse category filter chalega: /api/products/?category=bronze)
    path('api/products/', product_api, name='product_api'),
    path('api/', include(router.urls)), # Viewset option
    
    # 2. Artist APIs
    path('api/artists/', artist_list, name='artist_list'),
    path('api/artists/<int:pk>/', artist_detail, name='artist_detail'),
    path('api/artist/upload/', artist_post_creation, name='artist_upload'),

    # 3. Auth APIs
    path('api/register/', register_user, name='register_user'),
    path('api/login/', obtain_auth_token, name='api_token_auth'),
]