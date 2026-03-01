from django.contrib import admin
from .models import Product, Artist, Creation # Teeno ko ek saath import karein

# 1. Product registration (Sirf ek baar)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock')

# 2. Artist registration (Aditya Kumar Singh jaise artists ke liye)
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    # 'artist_type' (T ke saath) ko yahan list_display mein rakha hai
    list_display = ('id', 'name', 'designation', 'artist_type')
    search_fields = ('name',)

# 3. Creation registration (PDF wala data: Dependency, Mirage, etc. ke liye)
@admin.register(Creation)
class CreationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'artist', 'medium') # Admin table mein ye columns dikhenge
    list_filter = ('artist', 'medium') # Side mein filter karne ka option
    search_fields = ('title',) # Title se search karne ka option