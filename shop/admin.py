from django.contrib import admin
from .models import Product, Artist, Creation

# 1. Product Registration
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Category aur Artist Name ab list mein dikhenge
    list_display = ('id', 'name', 'price', 'category', 'artist_name', 'stock')
    list_filter = ('category', 'artist_name') # Filter karne ka option

# 2. Artist Registration
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    # 'artist_type' (T ke saath)
    list_display = ('id', 'name', 'designation', 'artist_type')
    search_fields = ('name',)

# 3. Creation Registration (Artist Portfolio & Approval System)
@admin.register(Creation)
class CreationAdmin(admin.ModelAdmin):
    # Admin panel mein ye columns dikhenge
    list_display = ('id', 'title', 'artist', 'medium', 'is_approved', 'created_at')
    
    # Side mein filter karne ke options
    list_filter = ('is_approved', 'artist', 'medium')
    
    # Title se search karne ka option
    search_fields = ('title',)
    
    # --- Approval Action ---
    # Isse aap ek saath kai creations ko approve kar sakte ho
    actions = ['make_approved']

    def make_approved(self, request, queryset):
        rows_updated = queryset.update(is_approved=True)
        if rows_updated == 1:
            message_bit = "1 creation ko"
        else:
            message_bit = f"{rows_updated} creations ko"
        self.message_user(request, f"{message_bit} successfully approve kar diya gaya hai.")
    
    make_approved.short_description = "Selected creations ko approve karein"