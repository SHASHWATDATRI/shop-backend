from django.contrib import admin
from .models import Product, Artist  # Dono ko import karna zaroori hai

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock')

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    # 'arlist_type' ko hata kar 'artist_type' (T ke saath) likhiye
    list_display = ('id', 'name', 'designation', 'artist_type')