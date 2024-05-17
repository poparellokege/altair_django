from django.db import models
from django.utils.safestring import mark_safe
from django.forms import ModelForm, TextInput,EmailInput
# Create your models here.

class Setting(models.Model):
     STATUS = (
         ('True', 'True'),
         ('False', 'False'),
     )
     title = models.CharField(max_length=150)
     keywords = models.CharField(max_length=255)
     description = models.CharField(max_length=255)
     company = models.CharField(max_length=50)
     address = models.CharField(blank=True, max_length=100)
     phone = models.CharField(blank=True, max_length=15)
     fax = models.CharField(blank=True, max_length=50)
     email = models.CharField(blank=True, max_length=50)
     header_logo = models.ImageField(blank=True, upload_to='images/')
     footer_logo = models.ImageField(blank=True, upload_to='images/')
     facebook = models.URLField(blank=True, max_length=50)
     instagram = models.URLField(blank=True, max_length=50)
     twitter = models.URLField(blank=True, max_length=50)
     youtube = models.URLField(blank=True, max_length=50)
     aboutus = models.TextField(blank=True)
     contact = models.TextField(blank=True)
     references = models.TextField(blank=True)
     status = models.CharField(max_length=10,choices=STATUS)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     def __str__(self):
         return self.title


class Slider(models.Model):
   title = models.CharField(max_length=150)
   short_description = models.CharField(max_length=250)
   image = models.ImageField(blank=True, upload_to='slider_images/')
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
        return self.title

   def imageurl(self):
       if self.image:
           return self.image.url
       else:
            return ""

   def image_tag(self):
        return mark_safe('<img src="{}" heights="80" width="60" />'.format(self.image.url)) 
   image_tag.short_description = 'Image'


class Category(models.Model):
    STATUS = (
        ('True','True'),
        ('False','False'),
    )
    title = models.CharField(max_length=250)
    image = models.ImageField(blank=True, upload_to='category/')
    details = models.TextField()
    status = models.CharField(max_length=20, choices = STATUS)
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
         return self.title    

    def imageurl(self):
       if self.image:
           return self.image.url
       else:
            return ""

    def image_tag(self):
        return mark_safe('<img src="{}" heights="80" width="60" />'.format(self.image.url)) 
    image_tag.short_description = 'Image'


class Project(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    details = models.TextField()
    image = models.ImageField(blank=True, upload_to='projects/')
    architects = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    area = models.FloatField()
    manufactures = models.CharField(max_length=200)
    details = models.TextField()
    status = models.CharField(max_length=20, choices = STATUS)
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
         return self.title

    def imageurl(self):
        if self.image:
            return self.image.url
        else:
            return ""
    
    def image_tag(self):
        return mark_safe('<img src="{}" heights="70" width="60" />'.format(self.image.url)) 
    image_tag.short_description = 'Image'



class Service(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)
    details = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title    




class Team(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    facebook_url = models.URLField(max_length=200, blank=True,null=True)
    instagram_url = models.URLField(max_length=200, blank=True,null=True)
    twitter_url = models.URLField(max_length=200, blank=True,null=True)
    linkedin_url = models.URLField(max_length=200, blank=True,null=True)
    image = models.ImageField(upload_to='team/')
    details = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__(self):
         return self.name

    def imageurl(self):
        if self.image:
            return self.image.url
        else:
            return ""
    
    def image_tag(self):
        return mark_safe('<img src="{}" heights="70" width="60" />'.format(self.image.url)) 
    image_tag.short_description = 'Image'


class Testimonial(models.Model):
    client_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='client/')
    designation = models.CharField(max_length=200)
    short_description = models.TextField()

    def __str__(self):
         return self.client_name


class Sponsor(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='sponsor/')

    def __str__(self):
         return self.title



class Contact(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=40)
    subject = models.CharField(max_length=1000, blank=True)
    message = models.TextField()
    status = models.CharField(max_length=40, choices=STATUS, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name':TextInput(attrs={'class':'input', 'placeholder':'Enter Your Name'}),
            'email':EmailInput(attrs={'class':'input', 'placeholder':'Enter Your Email'}),
            'message':TextInput(attrs={'class':'input', 'placeholder':'Message'}),
        }