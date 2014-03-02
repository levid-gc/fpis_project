from django.db import models


class Suggestion(models.Model):
    title = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    link = models.URLField(blank=True)
    description = models.TextField(blank=True)
    time_sensitive = models.BooleanField()
    approved = models.BooleanField()

    def __unicode__(self):
        return self.title
