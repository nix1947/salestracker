"""
This models.py files define all the abstract class used all over the django
apps models
"""

from django.db import models

class TimeStampedModel(models.Model):
    """Abstract class  which contains the created_at and updated_at fields these
    will be common all over the django apps model if the models are inherited
    from TimeStampedModel class
    """
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
