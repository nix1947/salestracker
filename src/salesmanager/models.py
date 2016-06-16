import string, random
from datetime import timedelta
from django.utils import timezone
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

class PaymentStatus(models.Model):
    date = models.DateTimeField();
    paid_value = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.paid_value

class Company(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=9)
    mobile = models.CharField(max_length=10)
    address = models.ForeignKey(Address)
    contact_person = models.ForeignKey(ContactPerson)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('companies:company', kwargs={'pk':self.pk})

    def total_amount(self):
        total_amount = 0
        #grab all the item
        items = self.item_set.all()
        for item in items:
            total_amount += item.price
        return total_amount

    def weekly_sales(self):
        """Calculate weekly sales or last 7 days sales, based on the selling price of an item
        """
        last_seven_day = timezone.now() - timedelta(days=7)
        items = self.item_set.filter(status="sold", updated_at__gte=last_seven_day)
        total_sales = 0
        for item in items:
            total_sales += item.price
        return total_sales

    def monthly_sales(self):
        """Calcualte last 30 days sales based on the selling price assume each month equal to 30 days
        """
        last_thirty_days = timezone.now() - timedelta(days=30)
        items = self.item_set.filter(status="sold", updated_at__gte=last_thirty_days)
        total_sales = 0
        for item in items:
            total_sales += item.price
        return total_sales

    def weekly_benefit(self):
        """Calculate weekly benefit of this company from this day"""
        total_purchase_price = 0
        total_selling_price = 0
        last_seven_day = timezone.now() - timedelta(days=7)
        items = self.item_set.filter(status="sold", updated_at__gte=last_seven_day)
        for item in items:
            total_purchase_price += item.price
            total_selling_price += item.selling_price
        benefit = total_selling_price - total_purchase_price
        return benefit

    def monthly_benefit(self):
        """Calculate monthly benefit from this company from this day """
        """Calculate weekly benefit of this company from this day"""
        total_purchase_price = 0
        total_selling_price = 0
        last_thirty_days = timezone.now() - timedelta(days=30)
        items = self.item_set.filter(status="sold", updated_at__gte=last_thirty_days)
        for item in items:
            total_purchase_price += item.price
            total_selling_price += item.selling_price
        benefit = total_selling_price - total_purchase_price
        return benefit

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
