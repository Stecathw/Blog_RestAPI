from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.json import JSONField
from django.template.defaultfilters import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name

    
class Post(models.Model):
    
    class PublicPostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=1)  
    
    STATUS = (
        (0,"Privé"),
        (1,"Publique")
    )       
    
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    sum_up = models.TextField(default='')
    published = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    
    objects = models.Manager() # The default manager
    publicpostobjects = PublicPostObjects() # The custom manager

    class Meta:
        ordering = ('-published',)
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)    
        
    def __str__(self):
        return self.title
    
# New flight track model
class Flight_Track(models.Model):
    
    TYPE_OF_FLIGHT = (
        (0, "Dist 3pts"),
        (1, "Triangle plat"),
        (2, "Triangle FAI"),
    )

    track_json = JSONField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    added_date = models.DateTimeField(auto_now_add=True)
    duration = models.CharField(max_length=100, blank=True)
    distance = models.DecimalField(max_digits=6, decimal_places=2)
    CFD_public_link = models.CharField(max_length=100, blank=True)   
    category = models.IntegerField(choices=TYPE_OF_FLIGHT, default=0)

    def __str__(self):
        return f"{self.TYPE_OF_FLIGHT[self.category][1]} le {self.date} de {self.distance} km"

    def type_of_flight(self):
        """
        Returns type of flight 0, 1 or 2 according to TYPE_OF_FLIGHT
        """
        return self.TYPE_OF_FLIGHT[self.category][0]