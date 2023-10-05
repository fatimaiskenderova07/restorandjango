from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    cuisine = models.CharField(max_length=50)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    is_open = models.BooleanField(default=True)

    def str(self):
        return self.name
