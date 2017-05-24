from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Brand)
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Relationship)
admin.site.register(Calendar_dentist)
admin.site.register(Calendar_appointment)
admin.site.register(Treatment)
admin.site.register(Treatment_detail)
admin.site.register(Invoice)
admin.site.register(Inventory)
admin.site.register(Labo)
admin.site.register(Treatment_detail_labo)
