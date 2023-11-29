from django.shortcuts import render
from .models import Employee, Project, ProjectExecution, Position, Department

def home(request):
    employees = Employee.objects.all()
    projects = Project.objects.all()
    project_executions = ProjectExecution.objects.all()
    position = Position.objects.all()
    departament = Department.objects.all()

    context = {
        'employees': employees,
        'projects': projects,
        'project_executions': project_executions,
        'position' : position,
        'departament': departament

    }

    return render(request, 'index.html', context)
