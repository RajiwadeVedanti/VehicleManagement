from django.contrib import admin
from vehicleapp.models import Vehicle

# Register your models here.
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "type",
        "model",
        "description",
        "created_at",
        "updated_at"
    )

    search_fields = ("number","model")


admin.site.register(Vehicle,VehicleAdmin)