from django.db import models
from django.urls import reverse
#from django.db.models.signals import pre_save, post_save


CATEGORY_CHOICE = (
    ("bus", "Bus"),
    ("avia", "Avia"),
    ("individual", "Individual")
    )
# Create your models here.
class Tours(models.Model):
    head_keywords = models.TextField(null=True, blank=True)
    head_description = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=120) # tour name
    image = models.ImageField(null=True, blank=True)# main image
    short_title = models.TextField(null=True, blank=True)
    title = models.TextField(null=True, blank=True) # main image title
    video_embed = models.TextField(null=True, blank=True)
    dates = models.TextField(null=True, blank=True) 
    description = models.TextField(null=True, blank=True) 
    tour_program = models.TextField(null=True, blank=True)
    included = models.TextField(null=True, blank=True)
    not_included = models.TextField(null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, default='page-slug', blank=True)
    draft = models.BooleanField(default=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICE, default='bus')
    price = models.IntegerField(default=0)

    # python manage.py makemigrations
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tour-detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'tours'
        ordering = ["-timestamp", "-updated"]
