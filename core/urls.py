from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from shop.views import (
    product_api, products_by_category, artist_list, 
    artist_detail, register_user, artist_post_creation,
    get_user_profile, admin_pending_list, admin_approve_action # Naye views import kiye
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', register_user, name='register_user'),

    path('api/profile/', get_user_profile, name='user_profile'),

    path('api/admin/pending/', admin_pending_list, name='admin_pending'),
    path('api/admin/approve/<int:pk>/', admin_approve_action, name='admin_approve_action'),

    path('api/products/', product_api, name='product_api'),
    path('api/products/<str:category_slug>/', products_by_category, name='category_products'),
    
    path('api/artists/', artist_list, name='artist_list'),
    path('api/artists/<int:pk>/', artist_detail, name='artist_detail'),
    path('api/artist/upload/', artist_post_creation, name='artist_upload'),
]