from django.contrib import admin
from .models import Instruction, GPSurgery, GP, Patient, InstructionType


# Registering the models with the Django admin site to manage them through the admin interface.
admin.site.register(Instruction)
admin.site.register(GPSurgery)
admin.site.register(GP)
admin.site.register(Patient)
admin.site.register(InstructionType)