import datetime
from taggit.managers import TaggableManager
from datetime import date
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill



class Regione(models.Model):
    codice_regione = models.IntegerField(primary_key=True, verbose_name="codice Istat")
    name = models.CharField(max_length=300, db_index=True, verbose_name='nome')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'regione'
        verbose_name_plural = 'regioni'

class CittaMetropolitana(models.Model):
    codice_cittametropolitana = models.IntegerField(primary_key=True, verbose_name="codice Istat")
    name = models.CharField(max_length=300, db_index=True, verbose_name="nome")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'città metropolitana'
        verbose_name_plural = 'città metropolitane'

class Provincia(models.Model):
    codice_provincia = models.IntegerField(primary_key=True, verbose_name="codice Istat")
    name = models.CharField(max_length=300, db_index=True, verbose_name="Nome")
    codice_targa = models.CharField(max_length=2, db_index=True)
    regione = models.ForeignKey(Regione, db_index=True, on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s' % (self.name, self.regione.name)

    class Meta:
        ordering = ['name']
        verbose_name = 'provincia'
        verbose_name_plural = 'province'


class Comune(models.Model):
    codice_istat = models.IntegerField(db_index=True, unique=True, verbose_name="codice Istat")
    codice_catastale = models.CharField(blank=True, null=True, max_length=50, db_index=True)
    name = models.CharField(max_length=300, db_index=True, verbose_name="nome")
    provincia = models.ForeignKey(Provincia, db_index=True, on_delete=models.PROTECT)
    citta_metropolitana = models.ForeignKey(CittaMetropolitana, null=True, blank=True, db_index=True, on_delete=models.PROTECT)
    is_capoluogo = models.BooleanField(default=False, verbose_name="capoluogo")
    altitudine = models.IntegerField(blank=True, null=True)
    superficie = models.FloatField(blank=True, null=True, verbose_name="superficie (kmq)")
    popolazione = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'comune'
        verbose_name_plural = 'comuni'

    def __str__(self):
        return '%s - %s' % (self.name, self.provincia.name)

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Notizia(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length = 250, null=True, blank=True, unique=True)
    description = models.TextField(null=True,blank=True)
    date = models.DateTimeField()
    # citta = models.ForeignKey('comuni_italiani.Comune', on_delete=models.PROTECT)
    # citta = models.ForeignKey(Country, on_delete=models.CASCADE)
    comune = models.ForeignKey(Comune, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    class Meta:
        ordering = ['-last_modified']
        verbose_name_plural = "Notizie"

    def get_absolute_url(self):
        return reverse("notizia:notizia_list", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs): # new
        date = datetime.date.today()
        if not self.slug:
            self.slug = '%i/%i/%i/%s/%s' % (
            date.year, date.month, date.day, slugify(self.comune.name), slugify(self.title)
            )
        return super().save(*args, **kwargs)



class Images(models.Model):
    note = models.ForeignKey(Notizia, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images', null=True, blank=True)
    image_thumbnail = ImageSpecField(source='image',
                    processors=[ResizeToFill(250, 150)],
                    format='JPEG', options={'quality': 60})

    class Meta:
        verbose_name_plural = "Immagini"

class VideoNotizia(models.Model):
    note = models.ForeignKey(Notizia, on_delete=models.CASCADE)
    video = models.FileField(upload_to='video', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Video"


class News(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=30)
    description = models.TextField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    files = models.ImageField(upload_to='images',null=True,blank=True)
