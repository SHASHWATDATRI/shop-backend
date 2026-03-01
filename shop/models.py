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
# Purane dono 'Artist' models ko hata kar sirf ye ek rakhein
class Artist(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    artist_type = models.CharField(max_length=100)
    image_url = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

class Creation(models.Model):
    # 'on_delete=models.CASCADE' hona chahiye (dot aayega)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='creations')
    title = models.CharField(max_length=200) 
    medium = models.CharField(max_length=200) 
    dimensions = models.CharField(max_length=100) 
    image_url = models.URLField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return f"{self.title} by {self.artist.name}"
    



    