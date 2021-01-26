from django.db import models

# Create your models here.
class Siteinfo(models.Model):
    title = models.CharField(max_length=50,null=True,blank=True)
    logo = models.ImageField(upload_to='logo/',null=True,blank=True)
      
    def __int__(self):
        return self.id