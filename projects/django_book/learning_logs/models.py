from django.db import models # type: ignore

# Create your models here.

class Topic(models.Model):

    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now=True)
    def __str__(self):
        """
        Return a string representation of the model
        """        
        return self.text
    
class Entry(models.Model):

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a simple string representing the entry.

        Returns:
            str: beginning of the text
        """
        return f"{self.text[:50]}..."