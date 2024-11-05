from django.db import models

# Create your models here.

class Topic(models.Model):

    text = models.charField(max_length=200)
    data_added = models.DateTimeField(auto_now=True)
    def __str__(self):
        """
        Return a string representation of the model
        """        
        return self.text