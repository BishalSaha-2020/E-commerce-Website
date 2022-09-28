from django.contrib import admin

from .models import Items
admin.site.register(Items)

from .models import Contact
admin.site.register(Contact)

from .models import Orders
admin.site.register(Orders)

from .models import OrderUpdate
admin.site.register(OrderUpdate)