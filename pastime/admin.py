from django.contrib import admin
from .models import Location,Category,Sport

# Register your models here.
class SportAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)
# Sport details
admin.site.register(Location)
admin.site.register(Sport,SportAdmin)
admin.site.register(Category)