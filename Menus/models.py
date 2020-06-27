from django.db import models
from django.db.models import Model 

# Create your models here.

class SlideShow(models.Model):
    Image = models.ImageField(upload_to='Menus/Images', blank=True)
    Heading = models.CharField(max_length=100)

    def __str__(self):
        return self.Headings

    class Meta:
        verbose_name_plural = 'SlideShow'

class Team(models.Model):
    Image = models.ImageField(upload_to='Menus/Images', blank=True)
    Name = models.CharField(max_length=100)
    Position = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = 'Team'

class Event(models.Model):
    Name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='Menus/Images', blank=True)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.Name

class Gallery(models.Model):
    Image = models.ImageField(upload_to='Menus/Images', blank=True)

    class Meta:
        verbose_name_plural = 'Gallery'