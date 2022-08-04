from django.contrib import admin
from .models import Dept, Role, Employee


# class DeptAdmin(admin.ModelAdmin):
#     list_display = ('name', 'location')

# class RoleAdmin(admin.ModelAdmin):
#     list_display = ('name')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('f_name', 'l_name', 'dept', 'salary',
                    'bonus', 'role', 'phone', 'hire_date')


admin.site.register(Dept)
admin.site.register(Role)
# admin.site.register(Dept, DeptAdmin)
# admin.site.register(Role, RoleAdmin)
