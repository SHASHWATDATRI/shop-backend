from django.urls import path, include
from shop.views import (
    product_api, products_by_category, artist_list, 
    artist_detail, register_user, artist_post_creation
)

urlpatterns = [
    # ... baki admin/auth paths ...
    
    # Ye hai aapka dynamic category path
    path('api/products/<str:category_slug>/', products_by_category, name='category_products'),
    
    # Ye purana query param path
    path('api/products/', product_api, name='product_api'),
    
    # Artists
    path('api/artists/', artist_list, name='artist_list'),
    path('api/artists/<int:pk>/', artist_detail, name='artist_detail'),
    path('api/artist/upload/', artist_post_creation, name='artist_upload'),
    
    # Auth
    path('api/register/', register_user, name='register_user'),
]