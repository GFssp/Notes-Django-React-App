from django.db import models

class Notes(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=800)

    def __str__(self):
        return self.title[0:50]
    

