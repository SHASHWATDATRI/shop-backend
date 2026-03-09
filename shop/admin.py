from django.contrib import admin
from .models import Product, Artist, Creation, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3 

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'artist_name', 'dimensions', 'stock')
    
    list_filter = ('category', 'artist_name')
    
    search_fields = ('name', 'category')
    
    inlines = [ProductImageInline]


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'designation', 'artist_type')
    search_fields = ('name',)


@admin.register(Creation)
class CreationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'artist', 'medium', 'is_approved', 'created_at')
    list_filter = ('is_approved', 'artist', 'medium')
    search_fields = ('title',)
    
    actions = ['make_approved']

    def make_approved(self, request, queryset):
        rows_updated = queryset.update(is_approved=True)
        if rows_updated == 1:
            message_bit = "1 creation ko"
        else:
            message_bit = f"{rows_updated} creations ko"
        self.message_user(request, f"{message_bit} successfully approve kar diya gaya hai.")
    
    make_approved.short_description = "Selected creations ko approve karein"