from django.shortcuts import render
from .models import Employee


def homePageView(request):
    employees = Employee.objects.filter(created__year__lte=2022)
    return render(request, 'list.html', {'employees': employees})