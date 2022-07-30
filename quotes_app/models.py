from django.db import models

class Quote(models.Model):
    category = models.CharField(max_length=200, null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.body