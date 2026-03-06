from django.contrib import admin
from .models import Product, Artist, Creation, ProductImage

# --- 1. Multiple Images Inline ---
# Isse Product ke page par hi multiple images (extra 3 boxes) daalne ka option aayega
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3 

# --- 2. Product Registration ---
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Saari important fields dimensions ke saath
    list_display = ('id', 'name', 'price', 'category', 'artist_name', 'dimensions', 'stock')
    
    # Category aur Artist ke hisaab se filter karne ke liye
    list_filter = ('category', 'artist_name')
    
    # Search bar mein name aur category se search karein
    search_fields = ('name', 'category')
    
    # Multiple images ka section
    inlines = [ProductImageInline]


# --- 3. Artist Registration ---
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'designation', 'artist_type')
    search_fields = ('name',)


# --- 4. Creation Registration (Artist Portfolio & Approval System) ---
@admin.register(Creation)
class CreationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'artist', 'medium', 'is_approved', 'created_at')
    list_filter = ('is_approved', 'artist', 'medium')
    search_fields = ('title',)
    
    # Approval Action: Isse ek click mein bahut saari posts approve ho jayengi
    actions = ['make_approved']

    def make_approved(self, request, queryset):
        rows_updated = queryset.update(is_approved=True)
        if rows_updated == 1:
            message_bit = "1 creation ko"
        else:
            message_bit = f"{rows_updated} creations ko"
        self.message_user(request, f"{message_bit} successfully approve kar diya gaya hai.")
    
    make_approved.short_description = "Selected creations ko approve karein"