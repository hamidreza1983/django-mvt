from django.db import models



class Serivces(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(default="test")  
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created_at',)
