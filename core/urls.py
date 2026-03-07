from django.contrib import admin
from django.urls import path
# JWT Imports
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from shop.views import (
    product_api, products_by_category, artist_list, 
    artist_detail, register_user, artist_post_creation,
    get_user_profile  # Ye wala view add kiya hai
)

urlpatterns = [
    # 1. Django Inbuilt Admin (Browser access: /admin/)
    path('admin/', admin.site.urls),
    
    # 2. JWT Auth (Next.js Login ke liye)
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # 3. User & Admin Profile Check
    # Aapka friend isi URL se check karega ki user Admin hai ya nahi
    path('api/profile/', get_user_profile, name='user_profile'),

    # 4. User Registration
    path('api/register/', register_user, name='register_user'),

    # 5. Products APIs
    path('api/products/', product_api, name='product_api'),
    path('api/products/<str:category_slug>/', products_by_category, name='category_products'),
    
    # 6. Artists APIs
    path('api/artists/', artist_list, name='artist_list'),
    path('api/artists/<int:pk>/', artist_detail, name='artist_detail'),
    path('api/artist/upload/', artist_post_creation, name='artist_upload'),
]