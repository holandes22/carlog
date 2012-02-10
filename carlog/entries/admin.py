from django.contrib import admin
from carlog.entries.models import Car, CarTreatmentEntry, CarMechanic

admin.site.register(Car)
admin.site.register(CarTreatmentEntry)
admin.site.register(CarMechanic)