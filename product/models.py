from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    price = models.DecimalField(max_digits=11, decimal_places=2)
    wage = models.DecimalField(max_digits=8, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    code = models.CharField(max_length=20)
    cutie = models.DecimalField(max_digits=3, decimal_places=0)
    color = models.CharField(max_length=100)
    stock = models.BooleanField(default=True)
    # stock = models.PositiveIntegerField()
    # available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return f"{self.name}-{self.price}"
    
    # def get_absolute_url(self):
    #     return f'/{self.category.slug}/{self.slug}/'
    
    # def get_image(self):
    #     if self.image:
    #         return 'http://127.0.0.1:8000' + self.image.url
    #     return ''
    
    # def get_thumbnail(self):
    #     if self.thumbnail:
    #         return 'http://127.0.0.1:8000' + self.thumbnail.url
    #     else:
    #         if self.image:
    #             self.thumbnail = self.make_thumbnail(self.image)
    #             self.save()

    #             return 'http://127.0.0.1:8000' + self.thumbnail.url
    #         else:
    #             return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail