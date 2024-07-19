import uuid
from django.db import models


class Holiday(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255, null=True)
    url = models.URLField(max_length=500, null=True)
    image = models.URLField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=255, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    
    def __str__(self):
        return str(self.title)
    

    class Meta:
        ordering = ['-created']