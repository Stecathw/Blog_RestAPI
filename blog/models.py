from django.utils import timezone
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
            return super().get_queryset().filter(status='public')  
    
    options = (
        ('public','Public'),
        ('private', 'Private')
    )     
    
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    sum_up = models.TextField(default='')
    published = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=7, choices=options, default='public')
    
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
    
    #new fields
    score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)
    avg_speed = models.DecimalField(max_digits=3, decimal_places=1, blank=True, default=0)
    max_alt = models.IntegerField(blank=True, default=0)
    vz_max = models.DecimalField(max_digits=3, decimal_places=1, blank=True, default=0)
    take_off = models.CharField(max_length=100, blank=True)
    take_off_time = models.CharField(max_length=100, blank=True)
    landing = models.CharField(max_length=100, blank=True)
    landing_time = models.CharField(max_length=100, blank=True)
    

    def __str__(self):
        return f"{self.TYPE_OF_FLIGHT[self.category][1]} le {self.date} de {self.distance} km"

    def type_of_flight(self):
        """
        Returns type of flight 0, 1 or 2 according to TYPE_OF_FLIGHT
        """
        return self.TYPE_OF_FLIGHT[self.category][0]
    

#New image model   
DIRECTORY_PATH='photos/'

class Photo(models.Model):   
    
    class PublicPhotosObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='public')
         
    options = (
        ('public','Public'),
        ('private', 'Private')
    )
      
    
    title = models.CharField(max_length=250)
    alt = models.TextField(null = True)
    image = models.ImageField(upload_to=DIRECTORY_PATH, default='images/default.jpg')
    slug = models.SlugField(max_length=250, unique_for_date='created')
    created = models.DateTimeField(auto_now=True)
    taken=models.DateField(default=timezone.now)
    altitudeAMSL=models.CharField(max_length=4, default='1000')
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author')
    status = models.CharField(max_length=7, choices=options, default='public')
    
    objects = models.Manager() # The default manager
    publicphotosobjects = PublicPhotosObjects() # The custom manager
