from django.db import models

# Create your models here.
# models.py

class TodoListdata(models.Model):
    nametitle = models.CharField(max_length=255)
    namedescription = models.TextField()
    

    def __str__(self):
        return self.title
