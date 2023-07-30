from django.contrib import admin
from .models import Category, Student


# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, DepartmentAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'mail_id']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20


admin.site.register(Student, StudentAdmin)
