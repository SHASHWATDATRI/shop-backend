from django.contrib import admin
from .models import Product, Artist  # Dono ko import karna zaroori hai

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock')

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    # 'arlist_type' ko hata kar 'artist_type' (T ke saath) likhiye
    list_display = ('id', 'name', 'designation', 'artist_type')

    from django.contrib import admin
from .models import Product, Artist, Creation # Creation ko yahan import karna zaroori hai

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock')

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'designation')

# Ye niche wali lines 'Creation' ko admin panel mein layengi
@admin.register(Creation)
class CreationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'artist', 'medium') # Admin table mein ye columns dikhenge
    list_filter = ('artist', 'medium') # Side mein filter karne ka option aayega
    search_fields = ('title',) # Title se search karne ka option