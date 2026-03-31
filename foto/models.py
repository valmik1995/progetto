import datetime
from django.db import models
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from django.contrib.auth.models import User, Group
from django.utils.timezone import now

class Categoria(models.Model):
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorie'
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(max_length=255)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/%/' % self.slug
    
class TaggedGalleria(TaggedItemBase):
    content_object = models.ForeignKey('Galleria', on_delete=models.CASCADE)
    class Meta:
        ordering = ['-content_object_id']

class Galleria(models.Model):
    class Meta:
        verbose_name = 'Galleria'
        verbose_name_plural = 'Gallerie'
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=False)
    date = models.DateTimeField(default=datetime.date.today, blank=True)
    image = models.ImageField(upload_to='galleria/originale', null=True, blank=True)
    image_thumbails = models.ImageField(upload_to='galleria/thumbails', null=True, blank=True)
    image_watermarks = models.ImageField(upload_to='galleria/watermarks', null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    tags = TaggableManager(through=TaggedGalleria, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    gruppo = models.CharField(max_length=100, blank=True)



    def __str__(self):
        return self.description

    def save(self, *args, **kwargs): # new
        date = datetime.date.today()
        return super().save(*args, **kwargs)



class Download(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    content_object = models.ForeignKey(Galleria, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
