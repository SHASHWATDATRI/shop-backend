from django.db import models
from django.contrib.auth.models import User

# 1. Choices hamesha Models ke upar honi chahiye
# Isse Admin Panel mein Dropdown List banti hai
CATEGORY_CHOICES = [
    ('terracotta', 'Terracotta'),
    ('metal', 'Metal'),
    ('glassart', 'Glass Art'),
    ('premium', 'Premium'),
    ('photography', 'Photography'),
    ('other', 'Other'),
]

# 2. Main Product Model (Ab isme typing nahi, sirf choice hogi)
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=500, null=True, blank=True)
    stock = models.IntegerField(default=10)
    
    # Category field choices ke saath (Dropdown ke liye)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='other'
    )
    
    artist_name = models.CharField(max_length=200, null=True, blank=True)
    dimensions = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        # Admin mein display name dikhane ke liye choice label ka use
        return f"{self.name} - {self.get_category_display()}"

# 3. Multiple Images for Products
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image_url = models.URLField(max_length=500)

    def __str__(self):
        return f"Image for {self.product.name}"

# 4. Artist Profile Model
class Artist(models.Model):
    # Artist login ke liye User se link karein
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='artist_profile', null=True, blank=True)
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    artist_type = models.CharField(max_length=100)
    image_url = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

# 5. Artist Creations Model
class Creation(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='creations')
    title = models.CharField(max_length=200) 
    medium = models.CharField(max_length=200) 
    dimensions = models.CharField(max_length=100) 
    image_url = models.URLField(max_length=500, null=True, blank=True)
    
    # Approval Features
    is_approved = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.title} by {self.artist.name}"