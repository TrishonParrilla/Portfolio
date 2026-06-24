from django.db import models

# Create your models here.
class skills(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    year = models.PositiveBigIntegerField()
    repository_link = models.URLField()
    skills = models.ManyToManyField("skills")
    image = models.ImageField(upload_to='imgproject/')

    def __str__(self):
        return self.name