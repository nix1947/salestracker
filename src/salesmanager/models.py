import string, random

from django.db import models
from django.core.urlresolvers import reverse
from core.models import TimeStampedModel
from core.constants import CATEGORY



class Address(models.Model):
    zone = models.CharField(max_length=50)

    def __str__(self):
        return self.zone


class Category(models.Model):
    """Item categories"""
    category_name = models.CharField('Item Category', choices=CATEGORY, default="pant",\
    max_length=100)
    category_description = models.TextField()

    class Meta:
        verbose_name_plural = "Item Category"
    def __str__(self):
        return self.category_name

class ContactPerson(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name + " " + self.last_name



class Company(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=9)
    mobile = models.CharField(max_length=10)
    address = models.ForeignKey(Address)
    contact_person = models.ForeignKey(ContactPerson)

    def __str__(self):
        return self.name

    

class Item(TimeStampedModel):
    """Item model """

    name = models.CharField("Item name", max_length=255)
    tag = models.CharField("Item tag", max_length=30, unique=True)
    category = models.ForeignKey(Category)
    company = models.ForeignKey(Company)
    price = models.DecimalField('Purchase price', max_digits=15, decimal_places=2)
    selling_price = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=4, choices=(
        ('new', 'New'),
        ('sold', 'Sold'),
    ), default='new')




    def __str__(self):
        return self.tag + "-" + self.name

    def get_status(self):
        if 'new' in self.status:
            return "New"
        if self.status == 'sold':
            return 'Sold'
        else:
            return "Unkown"


    def get_absolute_url(self):
        return reverse('items:item', kwargs={'pk':self.pk})
