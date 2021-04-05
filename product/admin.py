from django.contrib import admin
from .models import Product
from .models import Batch
from .models import Sku


admin.site.register(Product)
admin.site.register(Batch)
admin.site.register(Sku)