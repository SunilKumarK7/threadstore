from django.contrib import admin

# Register your models here.
from store.models import Size,Brand,Category,Product,Tag

admin.site.register(Size)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Product)