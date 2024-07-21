from django.contrib import admin
from inpatientsystemApp.models import Department, Patient, Doctor, Bed, Operation, OperatingRoom, OperatingRoomSchedule

admin.site.register(Department)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Bed)
admin.site.register(Operation)
admin.site.register(OperatingRoom)
admin.site.register(OperatingRoomSchedule)

# Register your models here.

