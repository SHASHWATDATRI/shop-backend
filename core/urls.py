from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
# Saare views ko ek hi line mein import karein
from shop.views import product_api, artist_list, artist_detail, artist_post_creation,register_user, artist_post_creation

urlpatterns = [
    # 1. Admin Panel
    path('admin/', admin.site.urls),
    
    # 2. Public APIs (Sabke liye)
    path('api/products/', product_api, name='product_api'),
    path('api/topartists/', artist_list, name='artist_list'),
    path('api/artists/<int:pk>/', artist_detail, name='artist_detail'),

    # 3. Authentication (Artist Login ke liye)
    # Yahan username aur password bhejoge toh ek 'Token' milega
    path('api/login/', obtain_auth_token, name='api_token_auth'), 

    # 4. Artist Specific Actions (PDF wala data upload karne ke liye)
    path('api/artist/upload/', artist_post_creation, name='artist_upload'),

    path('api/register/', register_user, name='register_user'),
    path('api/login/', obtain_auth_token, name='api_token_auth'),
    path('api/artist/upload/', artist_post_creation, name='artist_upload'),
]
