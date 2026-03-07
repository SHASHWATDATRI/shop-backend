from django.contrib import admin  # Ye import missing tha
from django.urls import path
from shop.views import (
    product_api, products_by_category, artist_list, 
    artist_detail, register_user, artist_post_creation
)

urlpatterns = [
    # Admin path ko hamesha top par rakhein
    path('admin/', admin.site.urls),
    
    # Products APIs
    # Dynamic path (<str:category_slug>) ko niche rakha jata hai 
    # taaki static paths pehle check ho sakein
    path('api/products/', product_api, name='product_api'),
    path('api/products/<str:category_slug>/', products_by_category, name='category_products'),
    
    # Artists APIs
    path('api/artists/', artist_list, name='artist_list'),
    path('api/artists/<int:pk>/', artist_detail, name='artist_detail'),
    path('api/artist/upload/', artist_post_creation, name='artist_upload'),
    
    # Auth APIs
    path('api/register/', register_user, name='register_user'),
]