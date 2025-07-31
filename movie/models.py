from django.db import models

# Create your models here.

class Movie(models.Model):
    mid = models.AutoField(primary_key=True)
    mname = models.CharField(max_length=50)
    mdir = models.CharField(max_length=50)
    mcont = models.CharField(max_length=500)
    myear = models.IntegerField()
    mlang = models.JSONField(default=list)
    mtype = models.JSONField(default=list)
    mimg = models.ImageField(upload_to='images/',null=True)
    mvideo = models.FileField(upload_to='videos/',null=True)
    
    def __str__(self):
        return self.mname