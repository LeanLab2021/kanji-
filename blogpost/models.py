from django.db import models


# Create your models here.
Category=(('男','boy'),('女','girl'))
class  BlogModel(models.Model):
    sex=models.CharField(max_length=50,choices=Category,default='lo')
    birthday=models.CharField(max_length=10, default='jg')
    username=models.CharField(max_length=100,default='g')
    postdate=models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.username

class SampleModel(models.Model):
    title=models.CharField(max_length=100)
    number=models.IntegerField()
