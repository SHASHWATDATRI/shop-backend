from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    image_url = models.URLField(max_length=500, null=True, blank=True)
    stock = models.IntegerField(default=10)

    def __str__(self):
        return self.name

# Naya Artist Table
class Artist(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    artist_type = models.CharField(max_length=100)
    image_url = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name
    
    from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200) # Jaise 'Sculptor' ya 'Painter'
    artist_type = models.CharField(max_length=100)
    image_url = models.URLField(max_length=500, null=True, blank=True) # Artist ki photo

    def __str__(self):
        return self.name

# Naya model har artist ki creations ke liye
# shop/models.py

class Creation(models.Model):
    # 'ForeignKey' se har work (jaise 'Dependency') ek artist se jud jayega
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='creations')
    title = models.CharField(max_length=200) # Jaise 'DEPENDENCY' [cite: 3]
    medium = models.CharField(max_length=200) # Jaise 'Brass' [cite: 4]
    dimensions = models.CharField(max_length=100) # Jaise '11x3.5x11 cm' [cite: 5]
    image_url = models.URLField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return f"{self.title} by {self.artist.name}"
    



    