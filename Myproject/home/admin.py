from django.contrib import admin
from .models import Department, Employee, Position, Project,ProjectExecution

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_id', 'department_name', 'phone_number', 'room_number')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'last_name', 'first_name', 'middle_name', 'address','phone_number','education','department','position')

class PositionAdmin(admin.ModelAdmin):
    list_display = ('position_id', 'position_name', 'salary', 'bonus_percentage')
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'project_name', 'deadline', 'funding_size')
class ProjectExecutionAdmin(admin.ModelAdmin):
    list_display = ('execution_id', 'project', 'department', 'start_date')
    
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectExecution, ProjectExecutionAdmin)

