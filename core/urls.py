from django.contrib import admin
from django.urls import path
# JWT Imports jo missing the
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from shop.views import (
    product_api, products_by_category, artist_list, 
    artist_detail, register_user, artist_post_creation
)

urlpatterns = [
    # 1. Django Inbuilt Admin (Browser access: /admin/)
    path('admin/', admin.site.urls),
    
    # 2. JWT Auth (Next.js Login ke liye)
    # Next.js isi URL par username/password bhejega
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # 3. User Registration
    path('api/register/', register_user, name='register_user'),

    # 4. Products APIs
    path('api/products/', product_api, name='product_api'),
    path('api/products/<str:category_slug>/', products_by_category, name='category_products'),
    
    # 5. Artists APIs
    path('api/artists/', artist_list, name='artist_list'),
    path('api/artists/<int:pk>/', artist_detail, name='artist_detail'),
    path('api/artist/upload/', artist_post_creation, name='artist_upload'),
]