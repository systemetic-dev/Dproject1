from django.db import models
from django.utils.text import slugify
# Create your models here.

# class post(models.Model):
#     title =models.CharField(max_lenght=200)
#     slug =models.SlugField(unique=True)
#     content= models.textField()
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)
#     is_published = models.BooleanField(default = False)
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.title)
#             super().save(*args, **kwargs)
            
#     def __str__(self):  
#         return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title