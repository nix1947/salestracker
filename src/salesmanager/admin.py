from django.contrib import admin
from .models import Address, Item, Category, Company, ContactPerson


@admin.register
class ItemAdmin(admin.ModelAdmin):
    class Meta:
        pass

admin.site.register(Item)
admin.site.register(Company)
admin.site.register(ContactPerson)
admin.site.register(Address)
admin.site.register(Category)
