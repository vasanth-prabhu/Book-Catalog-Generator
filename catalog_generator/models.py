from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=122)
    author = models.CharField(max_length=122)
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.title