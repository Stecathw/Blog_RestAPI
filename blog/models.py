from django.db import models
from django.contrib.auth.models import User
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