from django.db import models

# Create your models here.

class Task(models.Model):
    taskTitle = models.CharField(max_length=30)
    taskDesc = models.TextField()
    image = models.ImageField(upload_to='uploaded_images',default='default_image.jpg')
    

    def __str__(self):
     return self.taskTitle