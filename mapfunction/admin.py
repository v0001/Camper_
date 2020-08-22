from django.contrib import admin
from .models import MyPlace
from import_export.admin import ImportExportModelAdmin


class MyPlaceAdmin(ImportExportModelAdmin):
    pass


admin.site.register(MyPlace, MyPlaceAdmin)
# Register your models here.
